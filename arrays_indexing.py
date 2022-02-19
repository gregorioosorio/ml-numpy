import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("print first row [1,2,3]")
print(a[0,:])

print("print last row [7,8,9]")
print(a[-1,:])
print(a[-1,])
print(a[-1])
print(a[a.shape[0] - 1])
print(a[2])

print("print middle column [2,5,8]")
print(a[:,1])
print(a[:,1:2])

print("print first two columns [[1,4,7],[2,5,8]]")
print(a[:,0:2])
print(a[:,:2])

print("print two last rows [[4,5,6],[7,8,9]]")
print(a[-2:])

b = np.linspace(1,10,num=100)
print("print all elements exclude the last 20 elements")
print(b[:-20])
print("print last 20 elements")
print(b[-20:])