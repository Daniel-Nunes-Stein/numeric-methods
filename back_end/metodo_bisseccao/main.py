from sympy import * 
import numpy as np
import re

def bissection(func, intervalo, tol, parada_opts):
    log = []

    if not validate_func(func):
        log.append("Função possui caracteres inválidos")
        return "", "", "", log
        raise ValueError("Function contains invalid characters")
    
    x = symbols('x')
    func_expression = sympify(func)
    func_lambda = lambdify(x, func_expression, "numpy")


    a = intervalo[0]
    b = intervalo[1]
    m = None
    k = 0

    if func_lambda(a) * func_lambda(b) >= 0:
        log.append('Não há raiz no intervalo dado')
        return "", "", "", log
        raise ValueError('Não há raiz no intervalo dado')

    while True:
        m = (a + b) / 2
        print(f'a{k} = {a}')
        print(f'm{k} = {m}')
        print(f'b{k} = {b}')
        log.append(f"a{k} = {a} // m{k} = {m} // b{k} = {b}")
        
        if (func_lambda(a) > 0 and func_lambda(m) < 0) or (func_lambda(a) < 0 and func_lambda(m) > 0):
            a = a
            b = m
        else:
            a = b
            b = m
        
        erro_absoluto = abs(m - a)
        log.append(f"erro {k}: {erro_absoluto}")
        print(f'erro {k}: {erro_absoluto}')
        if parada_opts == 0:
            if erro_absoluto < tol:
                return m, erro_absoluto, k, log
        elif parada_opts == 1:
            if abs(func_lambda(m)) < tol:  
                print('Encontrada a raiz através do metodo f(x) = 0 ou f(x) < tol')
                return m, abs(func_lambda(m)) , k, log
        k+=1
    


def validate_func(f):
    pattern = r'^[0-9x\+\-\*/\^\(\) ]*|log\(\w*\)|ln\(\w*\)|pi|e|sin\(\w*\)|cos\(\w*\)|tan\(\w*\)|arcsin\(\w*\)|arccos\(\w*\)|arctan\(\w*\)$'
    if re.match(pattern, f):
        return True
    else:
        return False
    





if __name__ == '__main__':
    fx = "(2200 * ln((1.6*10^5) / (1.6*10^5 - 2680 * x)) - 9.8 * x) - 1000"
    tol = 0.01 #pode ser m - b < tol // a - m < tol // f(x) < tol
    intervalo = (25, 26)
    #k = "(log(b - a) - log(criterio_de_parada)) / log(2)"
    parada_opts = 0 #0: a - m < tol / 1: f(x) < tol

    try:
        root, erro, log = bissection(fx, intervalo, tol, parada_opts)
        if root is not None:
            print(f'Raiz: {root} +/- {erro}')
            print(log)
    except ValueError as e:
        print(e)
    
    