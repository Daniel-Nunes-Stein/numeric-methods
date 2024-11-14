import numpy as np

def gauss_seidel(a_matrix, b_matrix, x_matrix, precision, nMax):
    log = []

    a_matrix = np.array(a_matrix)
    b_matrix = np.array(b_matrix)
    x_matrix = np.array(x_matrix)
    b_matrix = b_matrix.reshape(-1, 1)
    x_matrix = x_matrix.reshape(-1, 1)

    n, _ = np.shape(a_matrix)

    D_inv = np.diag(1 / np.diag(a_matrix))
    c_matrix = np.eye(n) - D_inv @ a_matrix
    d_matrix = D_inv @ b_matrix
    x_old = np.copy(x_matrix).flatten()
    x = np.copy(x_matrix).flatten()
    i = 0
    er = 1

    while er >= 10**(-precision) and i < nMax:
        log.append(f'Iteração {i}')
        for j in range(n):
            x[j] = c_matrix[j] @ x + d_matrix[j]
            log.append(f'x[{j}] = {x[j]}')
        log.append(f'x = {x.tolist()}')
        er = np.max(np.abs(x - x_old)) / np.max(np.abs(x))
        x_old = np.copy(x)
        log.append(f'Erro: {er}<br>---------------')
        i += 1
    
    return x.tolist(), i, log

if __name__ == "__main__":
    variable_matrix = np.array([[10, 2, 1], 
                                 [1, 5, 1], 
                                 [2, 3, 10]])
    constant_matrix = np.array([7, -8, 6])
    x0 = np.array([0.7, -1.6, 0.6])
    precision = 10
    max_iterations = 30

    x, i = gauss_seidel(variable_matrix, constant_matrix, x0, precision, max_iterations)

    print(f"Valor da solução: {x}\nNº de iterações: {i}")
