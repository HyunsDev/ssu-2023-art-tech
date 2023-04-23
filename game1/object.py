from event import CollisionEvent
from atom import Atom
import const


# Abstract Class
class Object(Atom):
    def __init__(self, x, y, width, height, isDraw=True, isDeleted=False):
        super(Object, self).__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isDraw = isDraw

        # TODO: remove this, add global context
        self.isDeleted = isDeleted

    @classmethod
    def collision(cls, game, object1, object2):
        if not isinstance(object1, Object) or not isinstance(object2, Object):
            raise TypeError("object1 or object2 is not Object")

        isCollision = cls.__getIsCollision(object1, object2)
        if not isCollision:
            return

        collision_direction = cls.__getCollisionDirection(object1, object2)
        event = CollisionEvent(
            object1,
            object2,
            collision_direction,
            cls.reverseDirection(collision_direction),
        )
        object1.dispatchEvent(event)
        object2.dispatchEvent(event)
        game.dispatchEvent(event)

    def draw(self):
        pass

    def drawHitbox(self):
        hitbox = self.getHitbox()
        noFill()
        stroke("#ff0000")
        strokeWeight(1)
        rect(hitbox["x"], hitbox["y"], hitbox["width"], hitbox["height"])

    def getHitbox(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}

    @staticmethod
    def __getIsCollision(object1, object2):
        object1Hitbox = object1.getHitbox()
        object2Hitbox = object2.getHitbox()

        if (
            # left
            object2Hitbox["x"] <= object1Hitbox["x"] + object1Hitbox["width"]
            # right
            and object2Hitbox["x"] + object2Hitbox["width"] >= object1Hitbox["x"]
            # top
            and object2Hitbox["y"] <= object1Hitbox["y"] + object1Hitbox["height"]
            # bottom
            and object2Hitbox["y"] + object2Hitbox["height"] >= object1Hitbox["y"]
        ):
            return True
        return False

    @staticmethod
    def __getCollisionDirection(object1, object2):
        object1Hitbox = object1.getHitbox()
        object2Hitbox = object2.getHitbox()

        left_distance = object1Hitbox["x"] + object1Hitbox["width"] - object2Hitbox["x"]
        right_distance = -(
            object1Hitbox["x"]
            - object1Hitbox["width"]
            - object2Hitbox["x"]
            - object2Hitbox["width"]
        )
        top_distance = object1Hitbox["y"] + object1Hitbox["height"] - object2Hitbox["y"]
        bottom_distance = -(
            object1Hitbox["y"]
            - object1Hitbox["height"]
            - object2Hitbox["y"]
            - object2Hitbox["height"]
        )
        min_distance = min(left_distance, right_distance, top_distance, bottom_distance)

        if min_distance == left_distance:
            # object2 is left of object1
            return "left"
        elif min_distance == right_distance:
            return "right"
        elif min_distance == top_distance:
            return "top"
        elif min_distance == bottom_distance:
            return "bottom"
        return None

    @staticmethod
    def reverseDirection(direction):
        if direction == "left":
            return "right"
        elif direction == "right":
            return "left"
        elif direction == "top":
            return "bottom"
        elif direction == "bottom":
            return "top"
        return None


# Abstract Class
class Block(Object):
    def __init__(self, *args, **kwargs):
        super(Block, self).__init__(*args, **kwargs)


# Abstract Class
class Entity(Object):
    def __init__(self, *args, **kwargs):
        super(Entity, self).__init__(*args, **kwargs)
        self.canBreakBlock = True
