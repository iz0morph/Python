class Singleton(type):
    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
        return cls.a


class Check(metaclass=Singleton):
    pass


obj_1 = Check()
obj_2 = Check()
print(obj_1)
print(obj_2)
