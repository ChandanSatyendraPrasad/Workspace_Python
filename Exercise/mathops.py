def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    result = 1
    for i in range(int(b)):
        result *= a
    return result

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    if a == 0:
        return 0
    x = a
    for _ in range(100):
        x = (x + a / x) / 2
    return x

def factorial(n):
    if n < 0:
        return "Error: Factorial of negative number"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, int(n) + 1):
        result *= i
    return result

def sine(angle_degrees):
    angle_rad = angle_degrees * 3.14159265359 / 180
    result = 0
    term = angle_rad
    for i in range(1, 20):
        result += term
        term *= -angle_rad * angle_rad / ((2*i) * (2*i + 1))
    return result

def cosine(angle_degrees):
    angle_rad = angle_degrees * 3.14159265359 / 180
    result = 1
    term = 1
    for i in range(1, 20):
        term *= -angle_rad * angle_rad / ((2*i - 1) * (2*i))
        result += term
    return result

def tangent(angle_degrees):
    sin_val = sine(angle_degrees)
    cos_val = cosine(angle_degrees)
    if cos_val == 0:
        return "Error: Tangent undefined"
    return sin_val / cos_val

def logarithm(x, base=10):
    if x <= 0:
        return "Error: Logarithm of non-positive number"
    result = 0
    count = 0
    while x >= base:
        x /= base
        count += 1
    remainder = x - 1
    power_term = remainder
    for i in range(1, 50):
        result += power_term / i
        power_term *= remainder
    return count + result