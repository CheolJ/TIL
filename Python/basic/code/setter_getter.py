class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def setter(self, first_name):
        print("setter")
        if len(first_name) >= 3:
            self.first_name = first_name
        else:
            print('error')
    
    def getter(self, first_name):
        print("getter")
        return self.first_name.upper()
    
    
    def disp(self):
        print(self.first_name, self.last_name)
    
    name = property(getter, setter)
    
    

user1 = User("andy", "kim")
user1.disp()

user1.first_name = 'jhon'