from patterns.singleton.singleton_one import Singleton as s
from patterns.singleton.haar_classifier import HaarClassifier

class Normal:
    def __init__(self):
        pass

# class MyClass:

if __name__ == '__main__':
    try:
        s1 = s().getInstance()
        s2 = s().getInstance()
        print(s1, '\n', s2, '\n', s1 == s2, '\n')

        # instanceOne = s()
        # instanceTwo = s()
        # instanceOne.setCounter(20)
        # print(instanceOne.getCounter(), instanceTwo.getCounter())

        # n1 = Normal()
        # n2 = Normal()
        # print(n1, '\n', n2, '\n', n1 == n2)

        # file = 'haar_frontal_face.xml'

        # h1 = HaarClassifier()
        # h1.setFaceCascade(file)
        # c1 = h1.getFaceCascade()

        # h2 = HaarClassifier()
        # c2 = h2.getFaceCascade()

        # print(c1 == c2)

    except Exception as e:
        print('Exception:', e)