class Factory:
    def __init__(self, confidence, threshold):
        self.__confidence = confidence
        self.__threshold = threshold

    def setConfidence(self, val):
        self.__confidence = val
    
    def getConfidence(self):
        return self.__confidence

    def setThreshold(self, val):
        self.__threshold = val
    
    def getThreshold(self):
        return self.__threshold