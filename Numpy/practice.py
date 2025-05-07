# PRACTICE QUESTIONS
import numpy as np
# QUES 1
     # part1
    #  create array
a= np.array([10,11,12,13,14,15,16,17,18,19,20])
# print(a)
     # part 2
     # extract first 3 numbers
# print(a[0:3])
    #  part 3
    # modify last element to be 100
a[-1]= 100
# print(a)

# Ques 2 
    # part 1
    # give array  1 to 10 numb and slice 11 numbers 
b= np.array([1,2,3,4,5,6,7,8,9,10])
c = b[:11]
# print(c)
    # part 2
    # slice part will change value and check original will change or not 
# c[2] = 20
# print(b)

#QUES 3
    # part 1
    # create 3 by 3 and filled 1 to 9
d = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(d)
    # part 2
    # retrieve 2 row and 3 col
# print(d[1][2])
    # part 3
# print(d[0:3,1])


# QUES 4
    #  part 1
    # 4 by 2 matrix from 0 to 50 num
h = np.array([[22,23],[56,77],[33,49],[12,8]])
# print(h)
    #  part 2 
    # shape , size , dimension
# print("SHAPE IS :" + str(h.shape))
# print("SIZE IS :"+ str(h.size))
# print("DIMENSION IS :" + str(h.ndim))

# QUES 5
    #  part 1 
    # 1D array of 5 zeroes and then convert it to int
# arr_zeros = np.zeros(5)
# arr_zeros_int = arr_zeros.astype(int)
# print(arr_zeros_int)
    #  part 2
    #  identity matrix
# i =np.array([[1,0,0],[0,1,0],[0,0,1]])
# print(i)

# identity_matrix = np.eye(3)
# print(identity_matrix)
    # part 3 
    # 10 num of even number from 0 to 100
evenly_spaced = np.linspace(0, 100, 10)
print(evenly_spaced)

# Ques 6
    #  part 1
    # sort the given array to ascending 
l =np.array([8,2,5,1,7])
n =l.sort()
# print(l)
    # part 2 
    # concatenate matrix
# o = np.array([1,2,3])
# n = np.array([4,5,6])
# print(np.concatenate((o,n)))

# QUES 7
    # part 1 
    # 1D array of size 6 and reshape to (2,3)
# w = np.array([1,2,3,4,5,6])
# print(w.reshape(2,3))
#     # part 2 
c = np.array([1, 2, 3, 4, 5, 6])
q = c[:, np.newaxis]  # column vector
print(q)
      #part 3
    #   Use np.expand_dims to convert a 1D array into a 2D row vector:
arr = np.array([1, 2, 3, 4])
row_vector = np.expand_dims(arr, axis=0)
print(row_vector)




  
