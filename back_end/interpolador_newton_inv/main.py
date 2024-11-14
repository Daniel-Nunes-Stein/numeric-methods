import numpy as np


def inter_newton_inv(y, x, pontos, y_intersection):
    log = []

    if not validate_crescente(x) and not validate_decrescente(y):
        raise ValueError("Função em ordem incorreta")
    
    if not validate_size(x, y):
        raise ValueError("X e Y de tamanhos diferentes")
    
    table = []
    table.append(x)

    repetitions = 1
    
    for n in range(pontos - 1):
        order = []
        for m in range(len(table[n]) - 1):
            result = (table[n][m + 1] - table[n][m]) / (y[m + repetitions] - y[m]) #calculating g[y0, y1]; g[y0, y1, y2] ...
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
            log.append(f'({y_intersection} - {x[j]}) * ')
            factor *= (y_intersection - y[j]) #(y - y0) * g[y0, y1]; (y - y1) * g[y0, y1, y2] ...
        grau += 1
        aproximacao += factor
    
    log.append(f'Fator = {aproximacao}')
    log.append(f'Tabela de ordens: {table}')
    
    return y_intersection, aproximacao, log


def validate_crescente(arr):
    return np.all(np.diff(arr) >= 0)


def validate_decrescente(arr):
    return np.all(np.diff(arr) <= 0)


def validate_size(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return True

if __name__ == "__main__":
    qtd_pontos = 5
    x = [0.10, 0.20, 0.30, 0.40, 0.50]
    y = [0.125, 0.064, 0.027, 0.008, 0.001]
    y_intersection = 0.03
    
    try:
        fx ,result, table = inter_newton_inv(y, x, qtd_pontos, y_intersection)
        print(f'Valor de x para f({y_intersection}): {result}')
        print(f'Tabela de ordens: {table}')
    except ValueError as e:
        print(e)
