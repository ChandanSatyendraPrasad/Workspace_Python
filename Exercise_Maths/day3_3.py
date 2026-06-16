import numpy as np


# Sample Data
x = np.array([[1, 1], [1, 2], [1, 3]])
print("X\n",x)
y = np.array([2, 2.5, 3.5])
print("Y\n",y)
theta = np.array([0.1, 0.1])
print("theta\n",theta)
learning_rate = 0.1
iterations = 1000


def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    for _ in range(iterations):
        predictions = X.dot(theta)
        print("predictions",predictions)
        errors = predictions - y
        print("errors",errors)
        gradient = (1 / m) * X.T.dot(errors)
        print("gradient",gradient)
        theta -= learning_rate * gradient
        print("theta",theta)
    return theta

# Perform gradient descent
optimized_theta = gradient_descent(x, y, theta, learning_rate, iterations)
print("Optimized theta\n", optimized_theta)

