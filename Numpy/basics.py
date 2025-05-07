#  NUMPY (dealing with matrices ,arrays)

# numpy is fast and easy to work  with arrays/matrices and takes less memory as compared to list
# there are 2 types of arrays (1: 1D ) (2: 2D / multidemensional)
# arrays are static in nature (they don't use extra spaces when they execute)

# to use the numpy features, firstly we import/access the numpy module/ library

import numpy as np
                                    #  CREATION OF ARRAYS
# 3by3 array
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)
# 4by2 array
h = np.array([[22,23],[56,77],[33,49],[12,8]])
# print(h)


# 1D ARRAY CREATION

a = np.array([11 , 12 , 13])
# we know that array holds same type of data so we put same type of data in arrays
print(a) 

# to find out the DIMENSIONS of data  (rows) of data  and 1D ARRAYS HAS 1 DIMENSION(1 ROW)
print("Dimension is :"  + str(a.ndim)) 


# to check the DATA TYPE of array elements which kind of data they hold 
print(a.dtype)

# to check the SIZE of data how many elements are present there
print(a.size)

# the SHAPE of array tells us how many elements are there by coloumns and rows 
print(a.shape)

#  2D ARRAY CREATION
 
b = np.array([[22 , 33 ,44] , [12 ,11 ,25]]) 
             # this is written like 
             # [[22 33 44]
             #  [12 11 25]]
# blue brackets for 1d array and pink brackets shows that how many 1d arrays are there in itself
print(b)
print("Dimension is :" +str(b.ndim))
print("Size  is :" + str(b.size))
print("Shape is :" + str(b.shape))

# to access the value 11 we use indices of array a[row][column]
print(b[1][1])

# 3D ARRAY CREATION

c = np.array([[[11,12,13] , [22,23,24]] , [[33,34,35] , [43,44,45]]])
# [
#   [ 
#    [11 12 13]
#    [22 23 24]
#   ]
#   [
#    [33 34 35]
#    [43 44 45]
#   ]
# ]
print(c)
print("Dimension is :" +str(c.ndim))
print("Size  is :" + str(c.size))
print("Shape is :" + str(c.shape))

# 4D ARRAY CREATION

d = np.array([[[[10,11,12] , [20,21,22]],[[30,31,32] , [40,41,42]]],[[[50,51 ,52] , [60,61,62]],[[70,71,72] , [80,81,82]]]])
# [ 
#   [ 
#     [
#      [10 11 12]
#      [20 21 22]
#     ]
#     [
#      [30 31 32]
#      [40 41 42]
#     ]
#   ]
#   [    
#     [
#      [50 51 52]
#      [60 61 62]
#     ]
#     [ 
#      [70 71 72]
#      [80 81 82]
#     ]
#   ]
# ]
print(d)
print("Dimension is :" +str(d.ndim))
print("Size  is :" + str(d.size))
print("Shape is :" + str(d.shape) )







