import numpy as np

def new_array():
    return np.array([[1,2,3],[4,5,6]])

print("sum 1 to all array cells: [[2,3,4],[5,6,7]]")
ary = new_array()
print([[cell + 1 for cell in row] for row in ary])
print(ary + 1)

ary = new_array()
print("power of 2 to all array cells: [[1,4,9],[16,25,36]]")
print(ary ** 2)

ary = new_array()
print("square root to all array cells: [[sqrt(1),sqrt(2),sqrt(3)],[sqrt(4),sqrt(5),sqrt(6)]]")
print(np.sqrt(ary))