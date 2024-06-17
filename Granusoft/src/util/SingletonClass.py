class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
            print("NEW SENSOR")
        return cls.instance