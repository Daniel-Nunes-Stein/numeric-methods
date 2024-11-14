import numpy as np


def gauss_jacobi(a_matrix, b_matrix, x_matrix, precision, nMax):
    a_matrix = np.array(a_matrix)
    b_matrix = np.array(b_matrix)
    x_matrix = np.array(x_matrix)
    b_matrix = b_matrix.reshape(-1, 1)
    x_matrix = x_matrix.reshape(-1, 1)  

    n,_ = np.shape(a_matrix)
    log = []
    
    inv = np.linalg.inv(a_matrix*np.eye(n))
    c_matrix = np.eye(n) - inv@a_matrix #B
    d_matrix = inv@b_matrix
    x_old = np.copy(x_matrix)
    i = 0
    er = 1

    while(er >= 10**(-precision) and i <= nMax):
        x = c_matrix@x_old + d_matrix
        er = np.max(np.abs(x-x_old))/np.max(np.abs(x))
        log.append((f'Iteração: {i}<br>X: {x.tolist()}<br>Erro: {er}\n---------------------'))
        x_old = np.copy(x)
        i = i + 1
    log.append((f'Iteração: {i}<br>X: {x.tolist()}<br>Erro: {er}\n---------------------'))
    return x.tolist(), i, log


if __name__ == "__main__":
    variable_matrix = np.array([[10, 2, 1], [1, 5, 1], [2, 3, 10]])
    constant_matrix = np.array([7, -8, 6])
    x0 = np.array([0.7, -1.6, 0.6])
    precision = 10 #numero de casas dps da virgula
    max_iterations = 30

    x, i, log = gauss_jacobi(variable_matrix, constant_matrix, x0, precision, max_iterations)

    print(f"Valor da solução: {x}\nNº de iterações: {i}")