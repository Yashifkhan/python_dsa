# 1 count the positive number 
# given a list of numbers count the how many positive number 

# insert value in list use this :
# append(i) ,insert(5) ,,list=list+6 ,+=value

# myList =[1,-2,3,4-5,-6,7,-8,-9]

# countList=[]
# for i in myList:
#     if i>0:
#         countList.append(i)
    
# print("Count of positive value in list",len(countList))

#2 sum of even number given a number 
# number=int(input("enter the number : "))
# evenNumber=0
# for i in range(number+1):
#     # print("i",i),
#     if i %2==0:
#         print('i',i)
#         evenNumber+=i

# print("sum of even values",evenNumber)


# 3 print the multiplication table 
# given number but skip the five iteration 
# tableNumber=int(input("enter number of table : "))

# for i in range(11):
#     if i == 5:
#         continue
#     print(tableNumber ,"*", i, "=",tableNumber * i)

# 4 revers a str using the loop
# strvalue=input("enter value : ")
# newstr=""
# for i in strvalue:
#     newstr = i+newstr
# print(newstr)

# 5 find the non repeted char in str 
# str1="yashiyfkhan"
# mydict={}
# for i in str1:
#     if i in mydict:
#         mydict[i]+=1
#     else:
#         mydict[i] =1   

# for x,y in mydict.items():
#     if y ==1:
#         print("first non repet value is : ",x)
#         break

# print(mydict)  
 
    
# 6 factoril of number 

# number=int(input("enter the number : "))

# fect=1
# for i in range(1,number+1):
#     fect*=i
# print("fact of", number,fect )


# enter a valid number from user 
# while True: 
#     number =int(input("enter a number b/w 1 to 10 : "))
#     if number >1 and number <=10:
#         print("thanks")
#         break
#     else:
#         print("tray again")    


# prime number chekcker 
# number =int(input("enter you number"))

# for i  in range(2,number):
#     if number % i==0:
#         print("this is not prime number")
#         break
# else:
#     print("this is prime number")    
  
# 9 check all element are uniq or not in list 
# add value in list add() update()


# mylist=['apple','banana','mango','apple']
# uniqeset=set()
# for i in mylist:
#     if i in uniqeset:
#         print("duplicat value",i)
#         break
#     uniqeset.add(i)    
    

# encrement the time when user try ti many time add value or task 
# import time


# wait_time=1
# max_attemptes=5
# attempts=0

# while attempts<max_attemptes:
#     print("attempts",attempts +1,"wait for fiew minutes",wait_time)
#     time.sleep(wait_time)
#     wait_time *=2
#     attempts+=1
    
# import time

# number=1
# max_number=10
# while number <= max_number:
#     user_numbers = int(input(f"enter you {number} number :"))
#     number+=1
#     time.sleep(number)

# print("use numbers",user_numbers)

