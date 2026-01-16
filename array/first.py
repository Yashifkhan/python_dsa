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
arr = [3, 6, 9, 12, 15, 18]
def up_even(arr):
    for i in range(len(arr)):
        if arr[i] %2 == 0:
            arr[i]= 0
    return arr
print(up_even(arr))