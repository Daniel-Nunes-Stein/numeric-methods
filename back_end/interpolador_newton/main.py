import numpy as np


def inter_newton(x, y, pontos, x_intersection):
    log = []

    if not validate_crescente(x) and not validate_crescente(y):
        log.append("Função em ordem incorreta")
        raise ValueError("Função em ordem incorreta")
    
    if not validate_size(x, y):
        log.append("X e Y de tamanhos diferentes")
        raise ValueError("X e Y de tamanhos diferentes")
    
    table = []
    table.append(y)

    repetitions = 1

    for n in range(pontos - 1):
        order = []
        for m in range(len(table[n]) - 1):
            result = (table[n][m + 1] - table[n][m]) / (x[m + repetitions] - x[m]) #calculating f[x0, x1]; f[x0, x1, x2] ...
            log.append(f'Ordem: ({table[n][m + 1]} - {table[n][m]}) / ({x[m + repetitions]} - {x[m]}) = {result}')
            order.append(result)
        table.append(order)
        repetitions += 1

    aproximacao = 0
    grau = 0
    log.append('Fator:')
    for i in range(len(table)):
        factor = table[i][0] #first element of the order 0, 1 ... n
        for j in range(grau):
            log.append(f'({x_intersection} - {x[j]}) * ')
            factor *= (x_intersection - x[j]) #(x - x0) * f[x0, x1]; (x - x1) * f[x0, x1, x2] ...
        grau += 1
        aproximacao += factor
    log.append(f'Fator = {aproximacao}')
    log.append(f'Tabela de ordens: {table}')
    
    return x_intersection, aproximacao, log


def validate_crescente(arr):
    return np.all(np.diff(arr) >= 0)


def validate_size(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return True

if __name__ == "__main__":
    qtd_pontos = 3
    x = [2, 3.5, 4]
    y = [3.1, 4.9, 5.6]
    x_intersection = 3
    
    try:
        fx ,result, table = inter_newton(x, y, qtd_pontos, x_intersection)
        print(f'Valor de f({fx}): {result}')
        print(f'Tabela de ordens: {table}')
    except ValueError as e:
        print(e)
