class car:
    total_cars = 0
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        car.total_cars+=1
    
    @staticmethod
    def general_info():
        print("car is a four wheeler vehicle")

    def get_brand(self):
        return self.__brand
    
    @property  # This makes model accessible as mercedes.model instead of mercedes.model()
    def model(self):
        return self.__model    # Returns private attribute in a controlled way
    
    def set_brand(self,new_brand):
        print(new_brand)
        if new_brand == "":
            raise ValueError("Brand name cannot be empty")
        else:
            self.__brand = new_brand
        
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "petrol/diesel"


class ElectricCar(car):
    def __init__(self,brand,model,batterysize):
         super().__init__(brand,model)
         self.batterysize=batterysize
    def fuel_type(self):
        return "electric"
    
print(car.general_info())
tata=ElectricCar("tata","Nexon",50)
print(isinstance(tata,car))
print(isinstance(tata,ElectricCar)) # True
# mercedes = car("mercedes","benz")
# # mercedes.model= "q1"
# print(car.total_cars)
# print(mercedes.model)
# print(tata.fuel_type())
# print(tata.fullname())
# print(tata.get_brand())
# try:
#  tata.set_brand("hero-honda")
# except ValueError as e:
#     print(e)


class battery:
    def battery_info(self):
        return ("battery is used to store energy")

class engine:
    def engine_info(self):
        return ("engine is used to convert fuel into energy")


class ev(battery,engine,car):
    pass
    
newcar=ev("tata","Nexon")
print(newcar.fullname())
print(newcar.battery_info())
print(newcar.engine_info())