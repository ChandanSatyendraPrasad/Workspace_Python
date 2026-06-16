#Broadcasting in NumPy allows you to perform operations on arrays of different shapes. 
#When performing operations on arrays, NumPy automatically expands the smaller array to match the shape of the larger array, allowing for element-wise operations without the need for explicit replication of data.
import numpy as np
#Array Scalar Operations
#You can perform operations between an array and a scalar value. The scalar is broadcasted to match the shape of the array, allowing for element-wise operations.
#Example:
a = np.array([1, 2, 3])
print(a)
b = 2
c = a * b
print(c)
aa=a+10
print(aa)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
#Adding a scalar to a matrix
print(matrix)
matrix_plus_10 = matrix + 10
print(matrix_plus_10)

vector = np.array([1, 2, 3])
#Adding a vector to a matrix
print("Vector:")
print(vector)
print("Matrix:")
print(matrix)
matrix_plus_vector = matrix + vector
print("Matrix + Vector:")
print(matrix_plus_vector)

#Aggregation Functions
#NumPy provides various aggregation functions that allow you to compute summary statistics on arrays. 
#These functions can be applied to the entire array or along specific axes.
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:",a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Standard Deviation:", np.std(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Sum along axis 0:", np.sum(a, axis=0))
print("Sum along axis 1:", np.sum(a, axis=1))   

#Reshaping and Transposing
#NumPy provides functions to reshape and transpose arrays, allowing you to change the dimensions and orientation of your data.
a = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:")
print(a)
#Reshaping the array to a different shape
reshaped_a = a.reshape(3, 2)
print("Reshaped Array (3, 2):") 
print(reshaped_a)
#Transposing the array
transposed_a = a.T
print("Transposed Array:")
print(transposed_a)

#Random Number Generation
#NumPy provides a powerful random number generation module that allows you to create arrays of random numbers with various distributions.
#Generating random numbers from a normal distribution
normal_random_numbers = np.random.normal(loc=0, scale=1, size=(3, 3))
print("Random numbers from a normal distribution:")
print(normal_random_numbers)
#Generating random integers between 0 and 10
random_integers = np.random.randint(0, 10, size=(3, 3))
print("Random integers between 0 and 10:")
print(random_integers)
