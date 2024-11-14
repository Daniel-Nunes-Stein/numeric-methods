from sympy import * 
import numpy as np
import re

def newton_raphson(func, func_derivative, x_inicial, tol):
    log = []
    if not validate_func(func) or not validate_func(func_derivative):
        raise ValueError("Function contains invalid characters")
    
    x = symbols('x')
    func_expression = sympify(func)
    func_derivative_expression = sympify(func_derivative)
    func_lambda = lambdify(x, func_expression, "numpy")
    func_derivative_lambda = lambdify(x, func_derivative_expression, "numpy")

    x0 = x_inicial
    x = None
    erro_absoluto = 99999
    k = 0
    decimals = get_decimal(tol)

    while abs(erro_absoluto) >= tol:
        f_derivative = func_derivative_lambda(x0)

        if f_derivative == 0:
            print("A derivada é zero. Método falhou.")
            return None
    
        x = x0 - (func_lambda(x0) / func_derivative_lambda(x0))

        if k != 0:
            erro_absoluto = abs(x - x0)

        x0 = x

        log.append(f'Iteração {k}: x0 = {x0}\nErro absoluto (criterio de parada): {erro_absoluto}')

        k+=1

    rounded_x = round(x, decimals)
    e_a = abs(x - rounded_x)
    print(f'Erro absoluto: {e_a}')
    erro_relativo = abs(e_a) / abs(rounded_x)
    print(f'Erro relativo: {erro_relativo}')
    erro_percentual = erro_relativo * 10**2
    
    return rounded_x, erro_percentual, k, log

        
def validate_func(f):
    pattern = r'^[0-9x\+\-\*/\^\(\) ]*|log\(\w*\)|ln\(\w*\)|pi|e|sin\(\w*\)|cos\(\w*\)|tan\(\w*\)|arcsin\(\w*\)|arccos\(\w*\)|arctan\(\w*\)$'
    if re.match(pattern, f):
        return True
    else:
        return False


def get_decimal(precision):
    precision_str = str(precision)
    if 'e' in precision_str:
        decimals = int(precision_str.split('-')[1])
    else:
        decimals_str = precision_str.split('.')[1]
        decimals = len(decimals_str)
    print(decimals)
    print(precision_str)
    return decimals


if __name__ == '__main__':
    #e^x = exp(x)
    fx = "exp(x) - 4 * x^2"
    fx_derivative = "exp(x)- 8*x"
    tol = 0.001 
    x_inicial = 1

    try:
        root, erro, log = newton_raphson(fx, fx_derivative, x_inicial, tol)
        if root is not None:
            print(f'Raiz: {root} +/- {erro}%')
    except ValueError as e:
        print(e)
    
    