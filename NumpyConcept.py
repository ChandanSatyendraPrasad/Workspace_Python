import numpy as np
# Create a 1D array
arr1d = np.array([1, 2, 3, 4,5])
print("1D Array:") 
print(arr1d)
# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2d)
# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr3d)
# Create an array of zeros with shape (3, 4)
zeros_array = np.zeros((3, 4))
print("\nZeros Array:") 
print(zeros_array)

# Create an array of ones with shape (4, 4)
ones_array = np.ones((4, 4))
print("\nOnes Array:") 
print(ones_array)

# Create an array of random numbers with shape (3, 3)
random_array = np.random.rand(3, 3)
print("\nRandom Array:") 
print(random_array)

# Create an array of evenly spaced numbers with 10 elements between 0 and 100
evenly_spaced_array = np.linspace(0, 100, 10)
print("\nEvenly Spaced Array:") 
print(evenly_spaced_array)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False
evenly_spaced_array_no_endpoint = np.linspace(0, 1, 10, endpoint=False)
print("\nEvenly Spaced Array (No Endpoint):") 
print(evenly_spaced_array_no_endpoint)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False and dtype=int
evenly_spaced_array_no_endpoint_int = np.linspace(0, 1, 10, endpoint=False, dtype=int)
print("\nEvenly Spaced Array (No Endpoint, int):") 
print(evenly_spaced_array_no_endpoint_int)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False and dtype=float
evenly_spaced_array_no_endpoint_float = np.linspace(0, 1, 10, endpoint=False, dtype=float)
print("\nEvenly Spaced Array (No Endpoint, float):") 
print(evenly_spaced_array_no_endpoint_float)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False and dtype=complex
evenly_spaced_array_no_endpoint_complex = np.linspace(0, 1, 10, endpoint=False, dtype=complex)
print("\nEvenly Spaced Array (No Endpoint, complex):") 
print(evenly_spaced_array_no_endpoint_complex)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False and dtype=str
evenly_spaced_array_no_endpoint_str = np.linspace(0, 1, 10, endpoint=False, dtype=str)
print("\nEvenly Spaced Array (No Endpoint, str):") 
print(evenly_spaced_array_no_endpoint_str)

# Create an array of evenly spaced numbers with 10 elements between 0 and 1, with endpoint=False and dtype=bool
evenly_spaced_array_no_endpoint_bool = np.linspace(0, 1, 10, endpoint=False, dtype=bool)
print("\nEvenly Spaced Array (No Endpoint, bool):") 
print(evenly_spaced_array_no_endpoint_bool)

# Create an array of integers from 0 to 10 with a step of 2
range_array = np.arange(0, 10, 2)
print("\nRange Array:") 
print(range_array)

# Create an array of integers from 1 to 100 with a step of 3
range_array = np.arange(1, 100, 3)
print("\nRange Array:") 
print(range_array)

arr = np.array([1, 2, 3, 4, 5])
print("\nOriginal Array:")
print(arr)
added_arr = arr + 10
print("\nAdded Array:")
print(added_arr)
# Reshape the array to a 2D array with 5 rows and 1 column
reshaped_arr = arr.reshape(5, 1)
print("\nReshaped Array:")
print(reshaped_arr) 

expamded_arr = added_arr[:, np.newaxis]
print("\nExpanded Array:")
print(expamded_arr)

#Addition of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 + arr2  
print("Result of addition:", result)

#Multiplication of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 * arr2  
print("Result of multiplication:", result)

#Division of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 / arr2  
print("Result of division:", result)

#Subtraction of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 - arr2  
print("Result of subtraction:", result)

#Square of array
arr = np.array([11, 22, 33])
print("\nOriginal Array:")
print(arr)
squared_arr = arr ** 2
print("\nSquared Array:")   
print(squared_arr)

#Power of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 ** arr2  
print("Result of power:", result)

#Modulo of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 % arr2  
print("Result of modulo:", result)

#Floor division of two arrays
arr1 = np.array([1, 2, 3])  
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])  
print("\nSecond Array:")
print(arr2)
result = arr1 // arr2  
print("Result of floor division:", result)

#Square Root of array
arr = np.array([1, 4, 9, 16, 25])
print("\nOriginal Array:")
print(arr)  
sqrt_arr = np.sqrt(arr)
print("\nSquare Root Array:")
print(sqrt_arr)
sum_arr = np.sum(arr)
print("\nSum of Array:")    
print(sum_arr)
mean_arr = np.mean(arr)
print("\nMean of Array:")
print(mean_arr)
median_arr = np.median(arr)
print("\nMedian of Array:")
print(median_arr)
std_arr = np.std(arr)
print("\nStandard Deviation of Array:")
print(std_arr)
max_arr = np.max(arr)
print("\nMaximum of Array:")
print(max_arr)
min_arr = np.min(arr)
print("\nMinimum of Array:")
print(min_arr)

#Indexing of array
arr = np.array([10, 20, 30, 40, 50])
print("\nOriginal Array:")
print(arr)
first_element = arr[0]
print("\nFirst Element:")
print(first_element)
last_element = arr[-1]
print("\nLast Element:")
print(last_element)
slast_element = arr[-2]
print("\nSecond Last Element:")
print(slast_element)
#Slicing of array
arr = np.array([10, 20, 30, 40, 50])
print("\nOriginal Array:")
print(arr)
sliced_arr = arr[1:4]
print("\nSliced Array:")
print(sliced_arr)

#Reverse of array
arr = np.array([10, 20, 30, 40, 50])
print("\nOriginal Array:")
print(arr)
reversed_arr = arr[::-1]
print("\nReversed Array:")
print(reversed_arr)

#Concatenation of two arrays
arr1 = np.array([1, 2, 3])
print("\nFirst Array:")
print(arr1)
arr2 = np.array([4, 5, 6])
print("\nSecond Array:")
print(arr2)
concatenated_arr = np.concatenate((arr1, arr2))
print("\nConcatenated Array:")
print(concatenated_arr)