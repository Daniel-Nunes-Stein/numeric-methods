import numpy as np # Importamos nossa biblioteca preferida
from scipy.integrate import trapezoid, quad
from sympy import * 

# def f(x): # Transcrevemos a função dada
#     return np.cos(x) + x/np.pi

# x = np.linspace(0, 4*np.pi, num=21)

# y = f(x) # Nossa função já foi definida no bloco anterior

# print(trapezoid(y, x))

def newton_colis(func, x, y, interval, points, choice):

    log = []

    if choice == 0:
        a, b = interval
        a, b = float(a), float(b)

        log.append(f"Intervalo: [{a}, {b}]")

        x_integrator = np.linspace(a, b, num = points)
        log.append(f"Pontos de x (x_integrator): {x_integrator}")

        var = symbols('x')
        func_expression = sympify(func)
        func_lambda = lambdify(var, func_expression, "numpy")
        print(func_lambda)

        y_integrator = func_lambda(x_integrator)
        log.append(f"Valores de y (y_integrator) para x_integrator: {y_integrator}")

        integral = trapezoid(y_integrator, x_integrator)
        log.append(f"A = {integral}")
        print(integral)
        return integral, log
    if choice == 1:
        x = np.array(x)
        y = np.array(y)

        log.append(f"Valores de x: {x.tolist()}")
        log.append(f"Valores de y: {y.tolist()}")

        integral = trapezoid(y, x)
        log.append(f"A = {integral}")
        print(integral)
        return integral, log
    
       
    

if __name__ == "__main__":
    func = "exp(x)"
    x = [0, 1, 2, 3]
    y = [4, 5, 6, 7]
    interval = (0, 4)
    points = 100

    choice = 1 #0 para fazer com func, 1 para fazer com tabela

    result = newton_colis(func, x, y, interval, points, choice)