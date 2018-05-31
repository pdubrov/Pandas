import numpy as np

my_matrix = [[1,2,3], [4,5,6], [7,8,9]]

np_array = np.array(my_matrix)
print(np_array)

np_matrix = np.matrix(my_matrix)
print(np_matrix)

#returns numbers from 10 10 with step 2
print(np.arange(1, 10, 2))

print(np.zeros((3,6)))

print(np.ones((2,4)))


# returns 39 evenly-spaced numbers from 0 to 10
print(np.linspace(0,10,39))

#identity matrix
print(np.eye(4))

#populates array of given dimencions with numbers from uniform distribution on (0,1)
print(np.random.rand(3,4))
np.random.seed(101)# to ensure same random numbers are geenrated

#numbers from standard normal distribution N(0,1)
print(np.random.randn(3,4))

#random integer
print(np.random.randint(1, 90, (3,3)))

print(np_matrix.reshape( 1, 9))

print(np_matrix.shape)
print(np_matrix.dtype)

print(np_matrix)
print(np_matrix.max())
print(np_matrix.argmax()) # index of max elem

np_matrix.std()