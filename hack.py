
class Counter:
    def __init__(self, count):
        self.__count = count

    def setCount(self, count):
        self.__count = count
    
    def getCount(self):
        return self.__count

# class MyClass:

if __name__ == '__main__':
    try:
        c = Counter(1)
        print(c.getCount(), end='\n')

        c.setCount(22)
        print(c.getCount(), end='\n')

        # modify priate variavle?
        c.__count = 29
        # print(c.getCount(), end='\n')

        # access private variable?
        # print(c.__count, end='\n')

        # where is the hack?
        # python performs name mangling on private attributes
        # Every member with a double underscore will be changed to _object._class__variable
        c._Counter__count = 12
        print(c.getCount())

    except Exception as e:
        print('Exception:', e)