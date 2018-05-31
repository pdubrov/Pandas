import numpy as np

arr = np.arange(0, 10)
print(arr)

print(arr[3:])

#broadcasting
slice = arr[:5] # pointer to array, view of original area, not a copy
print(slice)

slice[:] = 99 # changes original array as well
print(slice)
print(arr)

#copy
arr_copy = arr.copy()
arr_copy[:4] = 55
print(arr_copy)
print(arr)

#matrix
mat = np.array( [[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(mat)
print(mat[:, 0])
print(mat[1,2])
print(mat[1])
print(mat[0:2,1:3]) # when slicing "up to, not including index"  0<=row<2, 1<=col<3
#same as
print(mat[ :2,1: ])

#Conditional selection
arr = np.arange(1, 10)
bool_arr = arr > 4
print(bool_arr )
cond_arr = arr[bool_arr]
print(cond_arr)
cond_arr = arr[arr > 5]
print(cond_arr)