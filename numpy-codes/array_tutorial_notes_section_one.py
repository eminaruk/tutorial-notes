# -*- coding: utf-8 -*-
# From EMIS TECHNOLOGY

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
    i       
    # print(i)    #! We need to flags argument for having some space to put new data type elements. If we don't use that, we'll get this error:
    """TypeError: Iterator operand required copying or buffering, but neither copying nor buffering was enabled"""

# Iterate by skipping some element

arr =  np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(arr[:, : :2]):
    i
    # print(i)  #! It selected elements by skipped 2 step in each array item
    
                                                       
### Join arrays
#! We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

arr1 = np.array([[1,2,3],[4,5,6], [-4, -5, -6]])
arr2 = np.array([[7,8,9],[10,11,12],[-6, -3, -7]])

joined_array = np.concatenate((arr1, arr2), axis=1)
joined_array

#! Joining arrays with stack method

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

joined_with_stack = np.stack((arr1, arr2), axis=1)
joined_with_stack

# Stacking along rows
#! hstack() method helps to stack along rows
#! hstack() means horizontal stacking

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

joined_with_hstack = np.hstack((arr1, arr2)) #! This method doesn't have 'axis' argument
joined_with_hstack

# Stacking along columns
#! vstack() method helps to stack along columns
#! vstack() means vertical stacking

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

joined_with_vstack = np.vstack((arr1, arr2))
joined_with_vstack

# Stacking along height
#! dstack( ) method helps to stack along height
#! dstack() method means depth stacking

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

joined_with_dstack = np.dstack((arr1, arr2))
joined_with_dstack


### Split Arrays
#! Splitting is opposite of joining in array.
#! We use array_split() method for splitting

arr = np.array([x for x in range(1,16)])
splitted_arr = np.array_split(arr, 5)
splitted_arr  #! splitted_arr is a list that includes 5 different arrays.

for each_splitted_arr in splitted_arr:
    
    each_splitted_arr  #! Type of each_splitted_arr is numpy.ndarray
    # print(each_splitted_arr)

#! We have also split() method too for splitting any array. But, split() method doesn't accept missing element and if there is no enough element for splitting, it will return error.

arr = np.array([x for x in range(1,12)]) 
# EXAMPLE OF SPLIT METHOD (WHAT IF THERE IS NO ENOUGH ELEMENT) --> splitted_with_split = np.split(arr, 4) #! ValueError: array split does not result in an equal division


# Split 2-D Arrays

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14]])
splitted_twod_array = np.array_split(arr, 3)
splitted_twod_array    #! It is a list that included 3 different arrays

# Split 2-D array into three 2-D arrays along rows

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1) #! It does give same result with hsplit() method!
newarr = np.hsplit(arr, 3)

### Searching Arrays
#! We use where() method for search any certain value
arr = np.array([1,2,3,5,6,5,5,7,9,3])
certain_value = np.where(arr == 5)
certain_value #! The result is 3,5,6 and it shows indexes of value 5 in array

#! Let me show another example
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,6,8,12])
even_numbers_in_array = np.where(arr%2 == 0) #! As you can see, we put a function in where() method and this function will find the even numbers in arra
even_numbers_in_array


# Search sorted
#! The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.
arr = np.array([1,2,3,4,5,4,6,7,8,9]) 
sorted_result = np.searchsorted(arr, 5) 
sorted_result
#! If you want to search from right side youcan use 'side' argument like this:

sorted_result = np.searchsorted(arr, 7, side = "right")

# Multiple values

arr = np.array([1,3,5])
sorted_Result = np.searchsorted(arr, [2,4,6])
sorted_Result 
#! The return value is an array: [1 2 3] containing the three indexes where 2, 4, 6 would be inserted in the original array to maintain the order.


### Sorting Arrays
#! Sorting doens't mean it is just numerical sorting. It also can be alphabetical or boolen sorting!
#! We use sort() method for that
arr = np.array([4,46,67,32,4,7,7,9,3,65])
sorted_arr = np.sort(arr) #! It is copy of the array. That means it doesn't own the array data

# Sorting strings

arr= np.array(["apple","kangroo","zebra","elephant","monkey"])
sorted_arr = np.sort(arr)

# Sorting array which is containing boolean values

arr = np.array([False, True, True, False,True, True, False])
sorted_boolean_arr = np.sort(arr) #! It sorts false to true, so false comes firstly in array beacause false(0) is smaller than true(1)
sorted_boolean_arr

# Sorting 2-D Arrays

arr = np.array([[1,5,7],[4,1,3]])
sorted_two_arr = np.sort(arr) #! Here, it sorts both of them and didn't touch anything else in arrays


### Filtering Arrays
#! We use boolen index list
#! A boolean index list is a list of booleans corresponding to indexes in the array.

arr = np.array([36,23,47,12,34])
boolean_index = [False, True, True, False, False]

new_arr = arr[boolean_index] #! Here, it allows just values whichs index matches with the True boolean.
#! But this way is not common for filtering. Here is the most common way to do that:
    
# Create Filter Array

arr = np.array([3,45,57,23,14,56,78,34])

filtering_list = []

for element in arr:
    
    if element < 35:
        filtering_list.append(True)
    
    else:
        filtering_list.append(False)

#! You can use this function as whatever you want!

new_arr = arr[filtering_list] #! Here, we created a filtering list and put in this list elements which is smaller than 35. After we applied the protocol

#! This way is most common way but there is still more common way here :) Let's learn that:
    
# Filtering by use filter list that is directly got from array

arr = np.array([3,45,57,23,14,56,78,34])

filtering_list = arr%2 != 0
new_arr = arr[filtering_list]



### THE FIRST PART OF TUTORIAL NOTES IS DONE
### LET'S COVER THE FILE AND GO TO SECOND NOTE .PY FILE
### HAVE A GOOD CODING :)
### Mehmet Emin ARUK from EMIS TECHNOLOGY

