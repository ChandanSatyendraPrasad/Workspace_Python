import numpy as np

#A = np.array([[2, 3, 4], [4, 5, 6], [7, 8, 9]])
A = np.array([[4, -2],[1, 1]])
determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)
print("Determinant: ", determinant)
print("Inverse: ", inverse)