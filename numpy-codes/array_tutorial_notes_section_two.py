# -*- coding: utf-8 -*-
# From EMIS TECHNOLOGY

######## NUMPY  ###########

import numpy as np
from numpy import random

### Random Numbers in Numpy

#Generate basic random number

random_number = random.randint(0,100)

#Generate random float

random_float = random.randn()

#Generate random array

random_array = random.randint(100, size=(5)) #! Random number doesn't mean different number. It can be same number in a random list or array

#Generate 2-D array

random_twod_array = random.randint(100, size=(3,5)) #! Result is an array that include 3 rows and 5 columns

# Generate random array by floats

random_float_array = random.randn(5)
random_twod_float_array = random.randn(3,5) #! Here, you can do same thing with the randint() method

# Generate random element from any array
#! Here, we use random.choice() method for getting random element from any array

arr = np.array([1,2,3,4,5,6])
random_choice_from_array = random.choice(arr)

#! Let's do more exciting staff with choice
#! Firstly create a new array

arr = np.array([x for x in range(100)])
random_choice_array_from_another_array = random.choice(arr, size=(4,5)) #! Here you are :) We got a new array that is made by another array

### Data Distribution

# Random distribution
#! A random distribution is a set of random numbers that follow a certain probability density function.
#! Probability Density Function is a function that describes a continuous probability. i.e. probability of all values in an array.
#! Let me show that with an example

arr = random.choice([3,5,6,1], p=[0.2,0.3,0.0,0.5], size = (50)) #! That code creates an array that includes 49 item by floowing probablities of these numbers
#! These probabities of numbers sum always has to be 1
arr = random.choice([3,5,6,1], p=[0.2,0.3,0.0,0.5], size = (5,6)) #! Also we can make it by define the size of array
arr

### Random Permutations

# Shuffling Arrays
#! Shuffle means changing arragment of elements in array

arr = np.array([1,2,3,4,5,6,7,8,9])
random.shuffle(arr) #! It is not copy of array, it is view. Hence, it owns data and when we change the arragment, that process occurs on original array too.

# Generating permutation od array

arr = np.array([1,2,3,4,5,6,7,8,9])
generated_permutation_arr = random.permutation(arr) #! Here you can see the process is same with the shuffle but the main differense is, permutation returns a new array.


### Seaborn

# Displots
#!Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array. 

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([1,2,3,4,5,6,7,8,9])
# plt.show()

#! We can also disable the histogram

sns.displot([1,2,3,4,5,6,7,8,9], kind="kde")

# Normal (Gaussian) Distribution
#! We use random.normal() method
"""
It has three parameters:

loc - (Mean) where the peak of the bell exists.

scale - (Standard Deviation) how flat the graph distribution should be.

size - The shape of the returned array.
"""
 
normal_dist = random.normal(size=(3,5))

# Generate an advanced normal distribution

advanced_normal_dist = random.normal(loc=1, scale=5, size=(4,6)) #! Mean of distribution is 1, standart deviation is 5

# Visualition of distribution (normal)

basic_normal_dist = random.normal(size=1000, loc= 1, scale= 6)
sns.displot(basic_normal_dist, kind= 'kde')

### Binomial Distribution
#! We use binomial() method here

"""
It has three parameters:

n - number of trials.

p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

size - The shape of the returned array.
"""

binomial_dist = random.binomial(n = 10, p = 0.4, size=15)




 







