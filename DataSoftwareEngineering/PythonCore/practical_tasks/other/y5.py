class Sun:
    _instance = None

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    

s1 = Sun.inst()
s2 = Sun.inst()
print(s1 is s2)