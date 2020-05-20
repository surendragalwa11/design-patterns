class Singleton:
    __instance = None
    __counter = 0
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
    
    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    @staticmethod
    def setCounter(val):
        Singleton.__instance.__counter = val

    @staticmethod
    def getCounter():
        return Singleton.__instance.__counter

 