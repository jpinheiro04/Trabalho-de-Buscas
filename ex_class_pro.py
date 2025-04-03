
class People:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        self.name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age: int):
        self._age = new_age

ana = People("Ana", 13)
print(f"Eu sou {ana.name} e tenho {ana.age} anos!")

ana.name = "Ana Maria"
ana.age = 18
print(f"Eu sou {ana.name} e tenho {ana.age}!!")