import sympy as sp
# x = sp.Symbol('x')
# f = x**2
# definite_integral = sp.integrate(f, (x, 0, 2))
# indefinite_integral = sp.integrate(f, x)
# print("Definite Integral:", definite_integral)
# print("Indefinite Integral:", indefinite_integral)


x = sp.Symbol('x')

def compute_integrals(expression, lower_limit, upper_limit):
    f = sp.sympify(expression)
    definite_integral = sp.integrate(f, (x, lower_limit, upper_limit))
    indefinite_integral = sp.integrate(f, x)
    return definite_integral, indefinite_integral

if __name__ == '__main__':
    expr = input('Enter the function in x (for example x**2): ')
    a = float(input('Enter the lower limit: '))
    b = float(input('Enter the upper limit: '))
    definite, indefinite = compute_integrals(expr, a, b)
    print('Definite Integral:', definite)
    print('Indefinite Integral:', indefinite)