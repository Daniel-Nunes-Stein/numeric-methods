"""
nome no vcn: ajuste polinomial

esse código foi uma adaptação de um livro colaborativo:

JUSTO, Dagoberto Adriano Rizzotto et al. "Cálculo Numérico: Um Livro Colaborativo Versão Python", UFRGS, 2020.
Disponível em: https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/livro-py.pdf. Acesso em: 04 nov. 2024.
"""

import numpy as np

def extrapolar(x, y, grau):
    """
    a função cria uma matriz V (é genérica, se ajusta até grau 4): 
    [x1, 1]
    [x2, 1]
    ...
    [xn, 1]

    depois, utiliza-se o metodo dos minimos quadrados:
    [a]
        = (V^T * V)^-1 *V^T*y
    [b] 

    onde V^T: Transposta de V

    resultando em: y = ax + b / é genérica, entao consegue se ajustar até grau 4

    foi escolhida essa abordagem matricial pois é mais geral, facil de implementar e escalar, e mais genérica, além de ter
    uma eficiencia computacional maior que uma que faz diversas somas e multiplicações com matrizes
    """
    log = []

    if not validate_crescente(x) and not validate_crescente(y):
        log.append("Função em ordem incorreta")
        raise ValueError("Função em ordem incorreta")
    
    if not validate_size(x, y):
        log.append("X e Y de tamanhos diferentes")
        raise ValueError("X e Y de tamanhos diferentes")
    
    if grau < 0:
        log.append("Grau menor que zero")
        raise ValueError("Grau menor que zero")
    
    x = np.array(x)
    y = np.array(y)

    V = np.array([x**i for i in range(grau + 1)]).transpose()

    log.append(f'Matriz V: <br> {V.tolist()}')

    cond_number = np.linalg.cond(V.T @ V)
    
    if cond_number > 1e10: 
        log.append("Matriz mal condicionada. Considere reduzir o grau ou normalizar os dados.")
        raise ValueError("Matriz mal condicionada. Considere reduzir o grau ou normalizar os dados.")
    
    a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(y)

    log.append(f'Resultado do mínimos quadrados: <br>{a}')

    terms = []
    for i in range(grau + 1):
        coef = a[i]

        if coef >= 0 and i > 0:
            sign = "+"
        else:
            sign = ""

        if i == 0:
            terms.append(f"{sign}{coef}")  
        elif i == 1:
            terms.append(f"{sign}{coef}*x") 
        else:
            terms.append(f"{sign}{coef}*x^{i}") 
    
    polinomio = " ".join(terms)
    log.append(f"Polinômio ajustado: <br> {polinomio}")

    return polinomio, log

def validate_crescente(arr):
    return np.all(np.diff(arr) >= 0)

def validate_size(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    return True


if __name__ == "__main__":
    x = [0, 1, 2, 3, 4]
    y = [27, 42, 60, 87, 127]
    grau = 4

    try:
        result, log = extrapolar(x, y, grau)
        print(result, log)

        terms = []
        for i in range(grau + 1):
            coef = result[i]

            if coef >= 0 and i > 0:
                sign = "+"
            else:
                sign = ""

            if i == 0:
                terms.append(f"{sign}{coef}")  
            elif i == 1:
                terms.append(f"{sign}{coef}*x") 
            else:
                terms.append(f"{sign}{coef}*x^{i}") 
        
        polinomio = " ".join(terms)
        print(f"Polinômio ajustado:{polinomio}")

    except ValueError as e:
        print(e)
