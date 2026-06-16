import numpy as np

A = np.array([[2, 3], [10,40]])
print("Matrix A:\n",A)
#determinant
determinant = np.linalg.det(A)
print("Determinant: ", determinant)


#inverse
inverse = np.linalg.inv(A)
print("Inverse of A: \n", inverse)

aa=determinant*inverse
print("TEST : \n",aa)

# eigenValues, eigneVectors 

eigenValues, eigneVectors = np.linalg.eig(A)
print("EigenVal\n", eigenValues)
print("EigenVectors\n", eigneVectors)

B = np.array([[4, 2], [1, 1]])
eigval, eigvec = np.linalg.eig(B)
print("EigVal: ",eigval)
print("EigVect: \n",eigvec)

#Decomposition of Matrix
U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular Values: \n", S)
print("V Transpose: \n", Vt)

