import sympy as sp


# x=sp.Symbol('x')
# print("X : ",x)
# f=x**2
# print("f(x) : ",f)
# derivative=sp.diff(f,x)
# print("Derivative: ", derivative)

# x, y = sp.symbols('x y')
# f = x**2 + y**2
# grad_x = sp.diff(f, x)
# grad_y = sp.diff(f, y)

# print("Partial Derivatives:", grad_x, grad_y)

def singlederivative():
    x = sp.Symbol('x')
    print("X : ", x)
    f = x**2
    print("f(x) : ", f)
    derivative = sp.diff(f, x)
    print("Derivative: ", derivative)
    return derivative

def partialderivative():
    x, y = sp.symbols('x y')
    print("X : ", x)
    print("Y : ", y)
    f = x**2 + y**2
    print("f(x) : ", f)
    grad_x = sp.diff(f, x)
    grad_y = sp.diff(f, y)
    print("Partial Derivatives:", grad_x, grad_y)
    return grad_x,grad_y
if __name__ == "__main__":
    singlederivative()
    partialderivative()