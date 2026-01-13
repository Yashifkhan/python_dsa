print("learn oops in python!")


# 1 question create a class of car with two argument is model or brand 
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    

# my_car=Car('MG','heactor')
# print(my_car.brand)
# print(my_car.model)

# class Login:
#     def __init__(self,userName,userPass):
#         self.userName=userName
#         self.userPass=userPass

# userInfo=Login('yashif','12345')
# print(userInfo.userName)
# print(userInfo.userPass)


# 2 question add a method to return the full the name of car 
# class Car:
#     def __init__(self,brand,name):
#         self.brand=brand
#         self.name=name

#     def full_name(self):
#         return self.brand +"," + self.name

# mycar=Car('mahindra','thar')
# print(mycar.full_name())


# 3 question inheritence 

# parents feature come in son that is the inheritence 
# class Car:
#     def __init__(self,brand,name):
#         self.brand=brand
#         self.name=name

#     def full_name(self):
#         return self.brand +"," + self.name

# class ElectricCar(Car):
#     def __init__(self,brand,name,bettery):
#         super().__init__(brand,name)
#         self.bettery=bettery
#     def all_features(self):
#         return self.brand + " " + self.name + " " + self.bettery

# my_new_car=ElectricCar('tasla','model 5','800KWH')
# print(my_new_car.all_features())


# 4 incapcilation 
# private the varibalr do not direct accex the value 
# class Car:
#     def __init__(self,brand,name):
#         self.__brand=brand
#         self.name=name

#     def get_brand(self):
#         return self.__brand

#     def full_name(self):
#         return self.brand +"," + self.name

# my_car=Car('mahindra','thar')
# print(my_car.get_brand())


# 5 question 
# polymore fisem ,person one work many 
# exampke + operater one think to handle the stirng or number 
# in this question careate a functionone or use with multy perpose 
# class Car:
#     def __init__(self,brand,name):
#         self.brand=brand
#         self.name=name

#     def full_name(self):
#         return self.brand +"," + self.name

#     def fuel_type(self):
#         return 'petrol or diesel'


# class ElectricCar(Car):
#     def __init__(self,brand,name,bettery):
#         super().__init__(brand,name)
#         self.bettery=bettery
#     def all_features(self):
#         return self.brand + " " + self.name + " " + self.bettery
#     def fuel_type(self):
#         return 'Electronic charg'


# simple_car=Car('mahindra','thar')
# Ele_car=ElectricCar('tasla','model 5','800KWH')
# print(simple_car.fuel_type())
# print(Ele_car.fuel_type())

# 6 question , static method 
# this are use to private the function we do not direct access the function after the create a object to class access the value direct use class name ,or in which we do not need to ue the self key word 

# class Car:
#     def __init__(self,brand,name):
#         self.brand=brand
#         self.name=name

#     # def full_name(self):
#     #     return self.brand +"," + self.name

#     # def fuel_type(self):
#     #     return 'petrol or diesel'

#     @staticmethod
#     def car_des():
#         return "this car speed is very highe"


# my_car=Car('mahindra','thar')
# print(my_car.car_des())
# print(Car.car_des())


# multipu inheritenc 
# create two class battery and engine and let the ElectricCar class inherit the both demonstring
# class Battery:
#     def battery_info(self):
#         return "ths is the battery"

# class Engine:
#     def engine_info(self):
#         return "this is the engine info"

# # this class enherit the multi class 
# class ElectricCar(Battery,Engine):
#     pass

# my_new_car=ElectricCar()
# print(my_new_car.battery_info())
# print(my_new_car.engine_info())

