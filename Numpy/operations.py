# CONCATENATION/MERGE/ADDITION/JOIN
# CONCATENATION WITH AXIS
# SLICING OF ARRAYS
# RESHAPE ARRAYS
# SORT ARRAYS


import numpy as np
                              # CONCATENATION/MERGE/ADDITION/JOIN
# for adding two arrays it is must that they have same order (rows , columns and size)

e = np.array([[11 , 12 ,13 ,14] , [21 , 22 ,23 ,24]])
f = np.array([[31,32,33,34,],[41,42,43,44]])
g =np.array([[61,62,63,64],[71,72,73,74]])

# concatenate will add the index to arrays while addition would b add the values on that index
# print(np.concatenate((e,f))) 
# [[11 12 13 14]
#  [21 22 23 24]
#  [31 32 33 34]
#  [41 42 43 44]]

# print(e+f)
# [[42 44 46 48]
#  [62 64 66 68]]

a = np.concatenate((e,f,g)) 
# print(a)
# if the order will not same and they have no equality then inhomogenous shape will occur and opeartion is not.... The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part (LIKE THIS)

                            # CONCATENATION WITH AXIS

# if the order is not same we gives the axis around which they are arranged and manage
b = np.array([[1, 2], [6,7]])
c = np.array([[3,4]])

z= np.concatenate((b, c), axis=0)
# print(z)
# ([[1, 2],
#   [6,7],
#  [3,4]])
y =np.concatenate((b, c.T), axis=1)
# print(y)
# ([[1, 2, 3],
#  [6, 7, 4]])
x = np.concatenate((b,c), axis=None)
# print(x)
# ([1, 2, 6,7, 3,4])
                                    # SLICING OF ARRAYS

# Slicing means extract out some values from specific position

m = np.array([22,33,44,55,66,77,88,99,222])
# to print all the elements around (0 reprsent strating index)
# print(m[0:])
# to print specific elements (Remember : ending idx is not included)
# print(m[2:6])

# if we slice some part of array and then change value to it original array will affect also
n = m[3:7]
# print(n)
n[2] = 100
# print(m)

# to slice the array and get specific row and coloumn 
p = np.array([[1,2,3],[4,5,6],[7,8,9]])
# this will give specific coloumn like 2 coloumn
print(p[0:3,2])

                                    # RESHAPE ARRAYS
                                
u = np.array([[100,200,300,400],[900,800,700,600]])
# print(u.shape)

# reshape of arrays means change the rows and col positions according to the size of arrays(like we have (2,4) it would change to(4,2)(1,8)(8,1)) we will see the multiples of that size 
# also The new shape should be compatible with the original shape. 

# print(u.reshape(8,1))
v = np.array([[[7,6,8],[5,0,1]],[[4,2,3],[11,33,44]]])
# print(v.shape)

r = (v.reshape(3,2,2))
# print(r)
# [[[ 7  6]
#   [ 8  5]]
#  [[ 0  1]
#   [ 4  2]]
#  [[ 3 11]
#   [33 44]]]

# it is difficult to reshape odd no. of arrays like 3by3 by many conventions but no impossible 
# to change HD data to LD data we can use (reshape+concatenate) opeartions

                                #   SORT/ARRANGE ARRAYS
l =np.array([8,2,5,1,7])
# first method
# firstly convert the original array to another varibale and then sort the variable ..sorting is on the original array 
# why we transorm the original array to variable (only because Sort the list in ascending order and return None)
n =l.sort()
print(l)
# second method
# access the numpy method of sort
print(np.sort(l)
