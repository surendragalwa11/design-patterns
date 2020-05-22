class UKZone:
    def __init__(self):
        self.__confidence = 8
        self.__threshold = 7

    def setConfidence(self, val):
        self.__confidence = val
    
    def getConfidence(self):
        return self.__confidence

    def setThreshold(self, val):
        self.__threshold = val
    
    def getThreshold(self):
        return self.__threshold