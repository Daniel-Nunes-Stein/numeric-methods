import numpy as np

def gauss_elimination(a_matrix, b_matrix):
    log = []
    result = []

    print(a_matrix, b_matrix)

    a_matrix = np.array(a_matrix)
    b_matrix = np.array(b_matrix)
    b_matrix = b_matrix.reshape(-1, 1)
    print(a_matrix, b_matrix)
    log.append(a_matrix.tolist())
    log.append(b_matrix.tolist())
    

    if a_matrix.shape[0] != a_matrix.shape[1]:
        log.append("ERRO: Matriz quadrada nao inserida")
        return "", log
    
    if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
        log.append("ERRO: Vetor constante de tamanho incorreto")
        return "", log
    
    n = len(b_matrix)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)

    #criar matriz
    augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1, dtype=float)
    
    while i < n:
        if augmented_matrix[i][i] == 0.0:
            log.append("Divisao por zero")
            return "", log

        for j in range(i + 1, n):
            scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i] #pegando o m
            augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i]) #criando linha nova
            log.append(augmented_matrix.tolist())

        i = i+1
    
    x[m] = augmented_matrix[m][n] / augmented_matrix[m][m]

    for k in range(n-2, -1, -1):
        x[k] = augmented_matrix[k][n]
        
        for j in range(k+1, n):
            x[k] = x[k] - augmented_matrix[k][j] * x[j]
        x[k] = x[k] / augmented_matrix[k][k]

    print("A matriz de vetor x a seguir resolve a matriz aumentada:")
    for answer in range(n):
        result.append(f"x{answer} = {x[answer]}")
    
    return result, log

if __name__ == "__main__":
    variable_matrix = np.array([[2, -1.5, 3], [-1, 0, 2], [4, 4.5, 5]])
    constant_matrix = np.array([[1], [3], [1]])

    gauss_elimination(variable_matrix, constant_matrix)