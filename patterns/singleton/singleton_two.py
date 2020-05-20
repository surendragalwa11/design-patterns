class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class SingletonClass(metaclass=Singleton):
    pass

if __name__ == '__main__':
    try:
        s1 = SingletonClass()
        s2 = SingletonClass()
        print(s1, '\n', s2, '\n', s1 == s2, '\n')

    except Exception as e:
        print('Exception:', e)