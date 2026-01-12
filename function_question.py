# print("learn python function")

# 1 WAF to return squre of number 
# def squre_number(n):
#     return n*n

# print(squre_number(5))

# 2 WAP  to accept two argument as parameter and return the sum 
# def sum_of_number(x,y):
#     return x+y

# print(sum_of_number(5,5))

# 3 WAF to polymorphism in function to multiply two number but accepta as string 
# def multiply(x,y):
#     return x * y

# print(multiply(5,7))
# print(multiply('yashif',3))
# # print(multiply('4','4'))
# print(multiply('4',4))

# 4 WAF to return the both area or circurmference of a circle give redis
# import math 
# def area_circurm(r):
#     area= math.pi * r ** 2
#     circurmference= 2 * math.pi *r
#     return area , circurmference
# area,circurmference =(area_circurm(7)) 
# print("area is : ",area)
# print("circurmference is : ",circurmference)


# 5 WAP to return a name if not privide then default 
# def name(myname = "greets"):
#     return f"you name is {myname}"

# print(name())

# 6 WAf to return the cube of number using lambada function 

#7 cube_of_number = lambda x: x ** 3 
# print(cube_of_number(5))

#8 # WAF to print the number 1 to n useing the lambda function 
# numbers= lambda x :[i+1 for i in range(x)]
# print(numbers(10))


# 9 how to handle the multy paramets have no aide to then hoe to handle 
# single *args accept multivalues only  
# useing the (*args)

# def multiargs(*args):
#     return sum(args)

# print(multiargs(1,2,3,4,5,5,6)) 

# 10 print the value accept as multi in key or value form 

#11 dubble **args accept key or value multi 
# def key_value(**args):
#     for x,y in args.items():
#         print(f'key : {x} or value : {y}')

# key_value(name='yashif',age='23')

# 12 WAF to genrate the even value useing the yield keyword 
# yeild key word rember the function path in memory ,and when am ask new value then rember the prev value function path or refrence 

# def yield_fun(limit):
#     for i in range(2,limit+1,2):
#         yield i

# # print(yield_fun(10))
# for num in yield_fun(10):
#     print(num)


# WAF to calculate the factoril of number 
# def fect(n):
#     if n == 1:
#         return  1
#     return  n*fect(n-1)
# print(fect(5))