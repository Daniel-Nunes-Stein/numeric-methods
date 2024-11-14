from sympy import * 
import numpy as np
import re

def calc_func(func, x_min, x_max, precision):
    log = []
    if not validate_func(func):
        raise ValueError("Function contains invalid characters")
     
    x = symbols('x')
    func_expression = sympify(func)

    func_lambda = lambdify(x, func_expression, "numpy")

    values = np.arange(x_min, x_max + precision, precision) #passo/precisão
    print(values)

    i = 0
    result_list = []
    roots = []

    decimals = get_decimal(precision)

    for i in range(len(values)):
        y = func_lambda(values[i])
        print(f"f({values[i]}) = {y}")
        log.append(f"f({values[i]}) = {y}")

        if not result_list:
            result_list.append((y, values[i]))
        else:
            if (result_list[0][0] < 0 and y > 0) or (result_list[0][0] > 0 and y < 0):
                roots.append([round(result_list[0][1], decimals), round(values[i], decimals)])
                result_list.clear()
            else:
                result_list.clear()
                result_list.append((y, values[i]))
    return roots, log


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
    #ln -> log/ln
    #log -> log10
    fx = "4 * log10(2000 * sqrt(x) - 0.4) - (1/sqrt(x))"
    interval1 = float(0.01)
    interval2 = float(0.04)
    precision = float(0.01)

    try:
        roots, log = calc_func(fx, interval1, interval2, precision)
        print(roots)
        print(log)
    except ValueError as e:
        print(e)
