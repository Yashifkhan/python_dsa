print("learn array in python")

# array use in python we have two ways blow explain two 

# first ----  import with  module in this way am get some feature ,and tell the data type when we create the array 
# feature like -- append ,remove , index 
# this is store only homogeneous (same data type)

# import array as arr
# my_array=arr.array('i',[1,2,3,4,5,6])
# for i in my_array:
#     print(i*2)


# second ------ import the numpy libary ,this give extra feaure and we do not need to tell me type in which who many type of data enter 
# feature --- 
# this is store only heterogeneous (mixed data types)








# Print only elements greater than 10
# arr = [4, 12, 7, 18, 3, 25]

# def num_is_grater(arr):
#     for i in arr:
#         if i > 10:
#             print(i)

# num_is_grater(arr)

# Update all even numbers in the array to 0
# arr = [3, 6, 9, 12, 15, 18]
# def up_even(arr):
#     for i in range(len(arr)):
#         if arr[i] %2 == 0:
#             arr[i]= 0
#     return arr
# print(up_even(arr))


# 1. find The max element in array 
# arr= [3, 7, 2, 9, 4]
# def find_max_item(arr):
#     max=arr[0]
#     for i in arr:
#         if max<i:
#             max=i
#     return max
# result=find_max_item(arr)
# print("max value is :", result)

# 2. Rotate Array Left by 1
# Given a list, rotate it left by one position.

# arr = [1, 2, 3, 4, 5]
# def rotate_arr(arr):
#     first_val=arr[0]
#     arr.pop(0)
#     arr.append(first_val)
#     return arr 

# result=rotate_arr(arr)
# print(result)

# day 2 
# 1.Count Even Numbers 

# arr = [1, 2, 3, 4, 6, 7, 8]
# def count_even(arr):
#     count=0
#     for i in arr:
#         if i%2 == 0:
#             count+=1
#     return count
# result=count_even(arr)
# print(result)

# 2: Find Second Largest Element
# arr = [10, 13, 20, 8, 15,6,9]
# arr = [10, 20, 15]
# def second_larg_num(arr):
#     max1=0
#     max2=0
#     for num in arr:
#         if num > max1:
#             max2=max1
#             max1=num
#         elif num > max2 and num != max1:
#             max2 = num
#     return max2

# result=second_larg_num(arr)
# print(result)


# convert simple array to  prefix array 
# arr=[1,2,3,4]

# def prefix_arr(arr):
#     sum_of_num=0
#     result=[]
#     for i in arr:
#         sum_of_num+=i
#         result.append(sum_of_num)
#     return result
# print(prefix_arr(arr))

# conver prefix array to simple array
# arr=[3,8,14,20]
# def simple_arr(arr):
#     result=[]
#     new_num=0   
#     for i in arr:
#         new_num=i-new_num
#         result.append(new_num) 
#         new_num=i
#     return result
# print(simple_arr(arr))






# # sliding window 
# arr = [2, 1, 5, 1, 3, 2]
# k = 3

# # first window 
# [2, 1, 5]

# 2 + 1 + 5 = 8

# # second window 
# [1, 5, 1]

# 1 + 5 + 1 = 7

# # thred window 
# [5, 1, 3]

# 5+ 1 +3=9


# # four window 
# [1, 3, 2]
# 1+ 3 +2 =6

