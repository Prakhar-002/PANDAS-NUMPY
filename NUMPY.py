
#? WHY USE NUMPY?

# NumPy provides efficient storage

# It also provides better ways of handling data for processing

# It is fast

# It is easy to learn

# NumPy uses relatively less memory to store data

#!----------------------------------------- 

#? JUPYTER NOTEBOOK

"""
• The Jupyter Notebook is an open-source web application that allows you to create
and share documents that contain live code, equations, visualizations and narrative
text.

• The Notebook has support for over 40 programming languages, including Python, R,
Julia. and Scala.

• Notebooks can be shared with others using email, Dropbox, GitHub and the Jupyger
Notebook Viewer.

• Your code can produce rich, interactive output: HTML, images, videos, LaTeX, and
custom MIME types.
"""

import numpy as np 

myArr = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]], np.int8)

print(myArr[1, 2]) #* 30


#? Array creation: Conversion from other Python structures

listArray = np.array([[1, 2, 3], [2, 4, 5]])

print(listArray)

"""
[ [1 2 3]
 [2 4 5]]
"""

print(listArray.dtype)

#* int64

print(listArray.shape) #* (2, 3)

print(listArray.size)  #* 6

objectArray = np.array({1, 24, 52})

print(objectArray) #* {24, 1, 52} 

print(objectArray.dtype) #*  object

#!-------------------------------------------------------------

#? intrinsic numpy array creation objects

zeroes = np.zeros((2, 5))

print(zeroes)

# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

print(zeroes.dtype) #* float64

print(zeroes.shape) #* (2, 5)

rng = np.arange(10)

print(rng) #* [0 1 2 3 4 5 6 7 8 9]

l_space = np.linspace(1, 10, 3) # (firstElm, lastElem, btwNo.OfElem)

print(l_space) #* [ 1.   5.5 10. ]


emp = np.empty((2, 2))

print(emp) #* Give an empty array

""" 
[[1.01454668e-311 1.44033956e+214]
 [3.23771047e+160 6.01334541e-154]]
"""

emp_like = np.empty_like(l_space) # Give same array shape with empty value

print (emp_like)

#* [7.65701345e-303 7.49674305e-300 7.50986707e-300]


ide = np.identity(3)

print(ide)

"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

arr = np.arange(33)

reshape_arr = arr.reshape(3, 11)

print(reshape_arr) #* reshape in multi-D array

"""
[[ 0  1  2  3  4  5  6  7  8  9 10]
 [11 12 13 14 15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28 29 30 31 32]]
"""

print(arr.ravel()) #* Again make 1D array

"""
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32]
"""


#!-------------------------------------------------------------

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

ar = np.array(x)

print(ar.sum(axis=0)) #* [12 15 18] Row

print(ar.sum(axis=1)) #* [ 6 15 24]   Column

print(ar.T) #* Transpose Of array

"""
[[1 4 7]
 [2 5 8]
 [3 6 9]
"""

#* give 1-D array 
for item in ar.flat:
      print(item)

""" 
1
2
3
4
5
6
7
8
9
"""

print(ar.ndim) #* 2 No. of dimension

print(ar.size) #* 9 no. of elem

print(ar.nbytes) #* 72 No. of byte use



#!-------------------------------------------------------------

one = np.array([1, 3, 2, 45, 20])

print(one.argmax())  #* 3 Index of max num in array

print(one.argmin())  #* 0 Index of min num in array

print(one.argsort()) #* [0 2 1 4 3] give sorted num index

mat = np.array([[1, 3, 8], [8, 5, 3], [8, 9, 20]])

print(mat.argmax())  #* 8

print(mat.argmin())  #* 0

print(mat.argmax(axis=0)) #* [1 2 2]

print(mat.argmax(axis=1)) #* [2 0 2]

print(mat.argsort(axis=1))

"""
[[0 1 2]
 [2 1 0]
 [0 1 2]]
"""


#!-------------------------------------------------------------


arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[1, 2], [3, 5]])

print(arr1 + arr2) #* We can DMAS (/ * + -) rule in matrix

"""
[[2 4]
 [6 9]]
"""

print(np.sqrt(arr1)) #* Take square root of all values

"""
[[1.         1.41421356]
 [1.73205081 2.        ]]
"""


print(arr1.sum())  #* 10
print(arr1.max())  #* 4
print(arr1.min())  #* 1



nums = np.array([[0, 2, 13], [4, 12, 6], [7, 8, 9]])

print(np.where(nums>9)) #* give index of value greater than 9

"""
(array([0, 1]), array([2, 1]))
"""

print(np.count_nonzero(nums)) #* 8 NO. of nonZero