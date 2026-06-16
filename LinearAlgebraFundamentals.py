import numpy as np
A=np.array([[1,2,3,4],[10,20,30,40]])
B=np.array([[10,20,30,40],[1,2,3,4]])

print("A+B \n",A+B)
print("A-B \n",A-B)

C=2*A
print("Scalar Multiplication :\n",C)
AA=np.array([[1,2],[3,4]])
BB=np.array([[10,20],[30,40]])
res=np.dot(AA,BB)
print("Matrix Multiplication :\n",res)

i=np.eye(5)
print("Identity Matrix \n", i)


Z = np.zeros((2, 3))
print("Zero Matrix \n", Z)

D = np.diag([1, 2, 3])
print("Diagonal Matrix\n", D)

E = np.ones((3, 3))
print("Ones Matrix \n", E)