class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls,*args , **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args,**kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]
    
class DataBaseHandler(metaclass = SingletonMeta):

    def __init__(self , name , password):
        
        self.name = name
        self.password = password

    def login(self):
        print(f"Login with {self.name}")


if __name__ == "__main__":

    db = DataBaseHandler(name = 'mthk' , password='mthk')
    db.login()
    db2 = DataBaseHandler(name = 'myo' , password='mthk')
    db2.login()
    if id(db) == id(db2):
        print("Singleton Successful")
    else:
        print("Singleton Failed")