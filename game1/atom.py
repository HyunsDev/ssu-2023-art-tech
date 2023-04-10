
# Minimum unit that users interact with
class Atom(object):
    game = None
    def __init__(self, game = None):
        self.eventListener = {}

        if game: Atom.game = game
        self.game = Atom.game

    def addEventListener(self, type, cb):
        if type not in self.eventListener:
            self.eventListener[type] = []
        self.eventListener[type].append(cb)

    def dispatchEvent(self, event):
        self.__dispatchEvent(event.type, event)

    def __dispatchEvent(self, type, event):
        if type in self.eventListener: 
            for cb in self.eventListener[type]:
                cb(event)
    
    def removeEventListener(self, type, cb):
        if type in self.eventListener: 
            self.eventListener[type].remove(cb)

    