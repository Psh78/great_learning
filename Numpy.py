#NUMPY stands for numerical python
#NUMPY is the core library for numeric and scientific computing
#It consists of multi-dimensional array objects and a collection of routines for processing those arrays

import numpy as np

"""
n1=np.array([[1,2,3,4],[5,6,7,8]])
n2=np.array([[1,2,3,4],[8,7,6,5]])
n3=n1*n2
print(n3)
"""
#numpy zeroes aray
"""
n1=np.zeros([5,5]) 
print(n1)
"""
#initialising a numpy array full of speciffic number
"""
n1=np.full([4,4],10)
print(n1)
"""
#initializing a numpy array within a range of numbers
"""
n1=np.arange(10,15)
print(n1)
"""
#initialising a numpy array within a range and of specific sequence
"""
n1=np.arange(10,20,3)
print(n1)
"""

#inistialising numpy aray with random numbers
"""
n1=np.random.randint(10,20,6)
print(n1)
"""

#checking the shape of the numpy array
"""
n1=np.array([[2,3,5,6],[7,8,9,0]])
print(n1)
print('before changing shape:')
print(n1.shape)
n1.shape = (8,1)
print('After changing shape:')
print(n1.shape)
print(n1)
#the shape can only be resized with the same numeber of total integers. Not more and not less.
"""
#joining numpy arrays
#There are three types of joining methods, this is called stacking. They are vstack()-'vertical stack',hstack()-'horizontal stack',column_stack()-'column stack'
"""
n1=np.array([1,2,3,4])
n2=np.array([5,6,7,8])
print('the vertical stack is:')
print(np.vstack((n1,n2)))
print('the horizontal stack is:')
print(np.hstack((n1,n2)))
print('the column stack is:')
print(np.column_stack((n1,n2)))
print('the row stack is:')
print(np.row_stack((n1,n2)))
"""
#numpy intersection and difference
"""
n1=np.array([1,2,3,5])
n2=np.array([5,2,7,8])
print('the intersection is:')
print(np.intersect1d(n1,n2))
print('the difference in n1 is:')
print(np.setdiff1d(n1,n2))
print('the difference in n2 is:')
print(np.setdiff1d(n2,n1))
"""
#addition of numpy array

"""
n1=np.array([1,2,3,4])
n2=np.array([4,3,2,1])
print('The total sum of the two arrays is:')
print(np.sum([n1,n2]))
#We can only get the sum of column numbers using the axis=0
print('the sum of column is:')
print(np.sum([n1,n2],axis=0))
#We can only get the sum of row numbers using axis=1
print('the sum of row numbers is:')
print(np.sum([n1,n2],axis=1))
"""
#Basic arithmetic operations
"""
n1=np.array([1,2,3,4])
n2=np.array([4,3,2,1])
print('The sum is:',n1+n2)
print('The multiplication is:',n1*n2)
print("The division is:",n1/n2)
print("The subtracion is:",n1-n2)
print('adding 1 to the whole array:',n1+1)
print('dividing the resultant sum of arrays:',(n1+n2)/2)
"""
#numpy Math functions
"""
n1=np.array([1,2,3,4])
n2=np.array([4,3,2,1])
print('The mean of the array n1 is:',np.mean(n1))#average of all numbers
print('The median of array n2 is:',np.median(n2))#the middle number in a sorted, ascending or descending
print("The standard deviation of array n1 is:",np.std(n1))# measures the spread of the data about the mean value.
"""
#saving and loading numpy arrays
#to save we use np.save('<file name>',<array name>)
#to load the saved numpy we use np.load('<filename.npy')
"""
n1=np.array([1,2,3,4])
np.save('my_numpy',n1)
print(np.load('my_numpy.npy'))
print('printing the n2 array by loading it with n1 array')
n2=np.load('my_numpy.npy')
print(n2)
"""