from sympy import * 
import numpy as np
import re

def secante(func, tol, intervalo):
    log = []
    if not validate_func(func):
        raise ValueError("Function contains invalid characters")
    
    x = symbols('x')
    func_expression = sympify(func)
    func_lambda = lambdify(x, func_expression, "numpy")

    x0 = intervalo[0]
    x1 = intervalo[1]
    k = 2
    x = 0
    decimals = get_decimal(tol)
    log.append(f"x0 = {x0} // f(x0) = {func_lambda(x0)}")
    log.append(f"x1 = {x1} // f(x1) = {func_lambda(x1)}")

    while abs((x1) - x0) >= tol or abs(func_lambda(x)) >= tol:
        fx0 = func_lambda(x0)
        fx1 = func_lambda(x1)
        x = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        log.append(f'x{k} = {x} // f(x{k}) = {func_lambda(x)}')
        x0 = x1
        x1 = x
        k+=1
    
    return round(x, decimals), log
   
    
    

        
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
    fx = "x^3 - 9*x + 3"
    tol = 0.0001 
    intervalo = (0, 1)

    try:
        root, log = secante(fx, tol, intervalo)
        if root is not None:
            print(f'Raiz: {root}')
    except ValueError as e:
        print(e)
    
    