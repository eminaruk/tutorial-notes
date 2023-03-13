# -*- coding: utf-8 -*-
# From EMIS Technology

######## NUMPY  ###########

import numpy as np

arr_by_list = np.array([1,2,3,4,5,6,7])

arr_by_tuple = np.array((1,3,5,7,9))

np.__version__


### Dimension of Arrays

# 0-D Array

zero_d_array = np.array(42)

# 1-D Array (Most common and basic array)

one_d_array = np.array([2,4,6,8,10])

# 2-D Array (Martix)

two_d_array = np.array([[1,3,5,7,9],[2,4,6,8,10]])

# 3-D Array (Matrices)

three_d_array = np.array([[[1,3,5,7,9],[2,4,6,8,10],[1,3,5,7,9],[2,4,6,8,10]]])

# The Number of The Dimensions

zero_d_array.ndim
one_d_array.ndim

# Choose dimention your own

arr = np.array([1,2,3,4,5], ndmin=3)
arr.ndim

### Array Indexing

arr = np.array([1,2,3,4,5])

arr[2]

# Acess 3-D Array Element

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

arr[0, 1, 2]

#! You can also do indexing by negative way!

### Array Slicing

arr = np.array([1,2,3,4,5,6,7,8,9])
arr[2:6]

# Slicing by step

arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
arr[1, 1::2] #! It jumps two-two over numbers

# Get common indexes from different dimentions

arr = np.array([[1,2,3,4],[5,6,7,8]])
arr[0:2, 2:4]

### Numpy Data Types

"""
    i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )

"""

# Check arrays datatype

arr = np.array([1,2,3,4,5])
arr.dtype

arr = np.array(["turkey","america", "japan"])
arr.dtype

# Create an array with defined datatype

arr = np.array(["adiyaman","istanbul","izmir"], dtype="S")
arr.dtype

arr = np.array([1,2,3,4,5], dtype="i4")
arr #!!! There is a understanding problem with me (why even we defined the size, command show all the elements)

# Typical value error

arr = np.array([1,"a",5]) #! If we add  dtype="i" argument in function, we'll get value error
arr

# Convert dataype of existing array

arr = np.array([1.2,4.7,6.8])
copy_of_arr = arr.astype(dtype="i")
copy_of_arr

#! Or in other way

arr = np.array([1.2,4.7,6.8])
copy_of_arr = arr.astype(int)
copy_of_arr

#! Or another example

arr = np.array([1.2,0,6.8])
copy_of_arr = arr.astype(dtype=bool)
copy_of_arr

### Array Copy vs View

#! When you use the copy method, you create new array and it means that file keeps some space on storage
# Create a copy
arr = np.array([1,2,3,4,5,6,7])

copy_of_arr = arr.copy()

arr[1] = 42

# Create a view

view_of_arr = arr.view()
arr[2] = 63

view_of_arr[-1] = 37 #! That method change both the array
arr

# Check the status of owning data

copy_of_arr.base #! Result is None and that shows copy of array doesn't own the data
view_of_arr.base #! Result is array and that shows view is same with array

### Array Shape

# Get 2-D Array Shape

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr.shape

arr = np.array([1,2,3,4], ndmin=5)  #! Here we test the delivery dimention array's shape
arr.shape

### Array Reshaping

# 1-D to 2-D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

reshaped_Arr = arr.reshape(4,3)
reshaped_Arr #! Here is the result 
"""         array([[ 1,  2,  3],
                   [ 4,  5,  6],
                   [ 7,  8,  9],
                   [10, 11, 12]])
"""

# 1-D to 3-D

arr = np.array([x for x in range(1,13)])
reshaped_arr = arr.reshape(2,3,2) #! That creates 2 item and each item has 3 item again and each 1 little item has 2 value
reshaped_arr

# Returns copy or view?

arr = np.array([i for i in range(1,16)])
arr.reshape(5,3).base #! It returns array and that show it is view and owns the array data

# Unknown Dimension
#! You don't have to give specific dimension number when you reshape any array. Numpy will calculate it for you

arr = np.array([x for x in range(1,25)])
arr.reshape(2,4,-1).shape #! The result is (2,4,3) and the last value of tuple is found by numpy

# Flattening the arrays
#! Flattening array means converting a multidimensional array into a 1D array

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
arr.ndim
new_arr = arr.reshape(-1) #! The code converts 2 dimension array to 1 dimension array
new_arr.shape
new_arr.ndim


### Array Iterating

# Iterate 1-D array
#! It is same as list
arr = np.array([1,2,3,4,5])
for i in arr:
    i

# Iterate 2-D array
arr = np.array([[1,2,3],[4,5,6]])
# for i in arr:
#     for j in i:
#         print(j) 

#! That situaiton exactly continue with same algorithm by step

# Iterate with exist function

arr = np.array([[1,2],[3,4],[5,6],[7,8]])

# for i in np.nditer(arr):
#     print(i)              #! This code print each minimum item that is in array


# Iterate array with different data types

arr = np.array([[1,2],[3,4],[5,6],[7,8]])
for i in np.nditer(arr, op_dtypes = ["S"], flags = ["buffered"]): #! We use op_dtypes argument for changing data type of array while indexing
    print(i)    #! We need to flags argument for having some space to put new data type elements. If we don't use that, we'll get this error:
    """TypeError: Iterator operand required copying or buffering, but neither copying nor buffering was enabled"""

# Iterate by skipping some element

arr =  np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(arr[:, : :2]):
    print(i)  #! It selected elements by skipped 2 step in each array item
    
                                                       

    


    
    
    



