import numpy as np

def lagrange(x, y, x_intersection):
    log = []
    i = 0
    j = 0
    l = []
    result = 1
    final_result = 0

    if not validate_crescente(x) and not validate_crescente(y):
        raise ValueError("Função em ordem incorreta")
    
    if not validate_size(x, y):
        raise ValueError("X e Y de tamanhos diferentes")
    
    for i in range(len(x)):
        log.append(f'L{i}: ')
        for j in range(len(x)):
            if j != i:
                log.append(f' ({x_intersection} - {x[j]}) / ({x[i]} - {x[j]}) *')
                result *= (x_intersection - x[j]) / (x[i] - x[j])
        l.append(result)
        log.append(f' = {result}')
        result = 1
    
    log.append('- // -')
    log.append(f'f({x_intersection}) = ')

    for i in range(len(y)):
        log.append(f'({l[i]} * {y[i]}) + ')
        final_result += l[i] * y[i]
    
    log.append(f' = {final_result}')

    return final_result, x_intersection, log


def validate_crescente(arr):
    return np.all(np.diff(arr) >= 0)


def validate_size(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return True


if __name__ == "__main__":
    x_intersection = 2.5
    x = [8.1, 8.3, 8.6, 8.7]
    y = [16.944, 17.566, 18.505, 18.821]

    try:
        result = lagrange(x, y, x_intersection)
        print(f"Resultado da interpolação em {x_intersection}: {result}")
    except ValueError as e:
        print(e)
