import numpy as np

# vector
a = np.array([1,2,3,4,5])
print("create an vector: [1,2,3,4,5]")
print(a)

# matrix
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("create a matrix: [[1,2,3], [4,5,6], [7,8,9]]")
print(A)

# with arange
B = np.arange(10)
print("arange from 0 to 10 (excluding the 10)")
print(B)

# with arange
C = np.arange(1,10)
print("arange from 1 to 10 (excluding the 10)")
print(C)

# with arange
D = np.arange(1,10,2)
print("arange from 1 to 10 (excluding the 10) with step 2")
print(D)

# with linspace
E = np.linspace(1,10,num=20)
print("linspace from 1 to 10 (including the 10) with exactly 20 points")
print(E)

# n-dimensional array with linspace
F = np.linspace((1,2,3), (10,20,30), 10)
print("linspace from row = [1,2,3] to [10,20,30] with 10 rows")
print(F)
