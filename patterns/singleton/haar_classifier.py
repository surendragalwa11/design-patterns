import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

defaultFile = 'haar_frontal_face.xml'

class HaarClassifier:
    __instance = None
    __frontal_face = None
    
    def __init__(self):
        if HaarClassifier.__instance is None:
            HaarClassifier.__instance = self

    @staticmethod
    def getInstance():
        if HaarClassifier.__instance is None:
            HaarClassifier()
        return HaarClassifier.__instance

    @staticmethod
    def setFaceCascade(fName):
        HaarClassifier.__frontal_face = cv2.CascadeClassifier(fName)

    @staticmethod
    def getFaceCascade():
        return HaarClassifier.__frontal_face

























# class HaarClassifier:
#     __frontal_face = None
    
#     def __init__(self):
#         if HaarClassifier.__frontal_face is None:
#             HaarClassifier.__frontal_face = cv2.CascadeClassifier(defaultFile)

#     @staticmethod
#     def setFaceCascade(fName):
#         HaarClassifier.__frontal_face = cv2.CascadeClassifier(fName)

#     @staticmethod
#     def getFaceCascade():
#         return HaarClassifier.__frontal_face
