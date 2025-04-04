class car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    
    def get_brand(self):
        return self.__brand
    
    def set_brand(self,new_brand):
        print(new_brand)
        if new_brand == "":
            raise ValueError("Brand name cannot be empty")
        else:
            self.__brand = new_brand
        
    def fullname(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(car):
    def __init__(self,brand,model,batterysize):
         super().__init__(brand,model)
         self.batterysize=batterysize

tata = ElectricCar("tata","Nexon",50)
print(tata.fullname())
print(tata.get_brand())
try:
 tata.set_brand("hero-honda")
except ValueError as e:
    print(e)
