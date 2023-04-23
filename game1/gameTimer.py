import const
from time import time, strftime, localtime


class GameTimer:
    def __init__(self):
        # [{ time: number, cb: func, isInterval: boolean, interval: number }]
        self.__symbol = 0
        self.__timers = {}

    def __getSymbol(self):
        self.__symbol += 1
        return self.__symbol - 1

    def setTimeout(self, cb, delay=1):
        symbol = self.__getSymbol()
        _time = frameCount + delay * const.FRAME_RATE
        self.__timers[symbol] = {
            "time": _time,
            "cb": cb,
            "isInterval": False,
        }

        print("Timer", self.__timers)
        return symbol

    def clearTimeout(self, symbol):
        del self.__timers[synbol]

    def tick(self):
        for symbol in self.__timers:
            timer = self.__timers[symbol]
            if timer["time"] <= frameCount:
                timer["cb"]()
                del self.__timers[symbol]

                if const.DEBUG_MODE:
                    now = strftime("%M:%S", localtime())
                    print("[%s] Timer: %s" % (now, symbol))
