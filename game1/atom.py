import const
from time import time, strftime, localtime


# Minimum unit that users interact with
class Atom(object):
    game = None

    def __init__(self, game=None):
        self.eventListener = {}
        self.timer = {}

        if game:
            Atom.game = game
        self.game = Atom.game

    def addEventListener(self, type, cb):
        if type not in self.eventListener:
            self.eventListener[type] = []
        self.eventListener[type].append(cb)

    def dispatchEvent(self, event):
        self.__dispatchEvent(event.type, event)
        if const.DEBUG_MODE:
            now = strftime("%M:%S", localtime())
            print("[%s] (%s) Event: %s" % (now, self.__class__.__name__, event.type))

    def __dispatchEvent(self, type, event):
        if type in self.eventListener:
            for cb in self.eventListener[type]:
                cb(event)

    def removeEventListener(self, type, cb):
        if type in self.eventListener:
            self.eventListener[type].remove(cb)

    def setTimeout(self, cb, delay=1):
        return self.game.gameTimer.setTimeout(cb, delay)

    def clearTimeout(self, symbol):
        return self.game.gameTimer.clearTimeout(symbol)
