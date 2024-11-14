import numpy as np

# Matriz de coeficientes
A = np.array([[10, 2, 1], 
              [1, 5, 1], 
              [2, 3, 10]])

# Vetor de termos independentes
b = np.array([7, -8, 6])

def seidel(A, b, p, x0, nMax):
    n, _ = np.shape(A)
    
    # Usando a matriz diagonal inversa
    D_inv = np.diag(1 / np.diag(A))
    
    # Calculando B e d
    B = -D_inv @ (A - np.diag(np.diag(A)))
    d = D_inv @ b
    
    # Inicializando os vetores de solução
    xOld = np.copy(x0).flatten()  # Convertendo para 1D
    x = np.copy(x0).flatten()      # Convertendo para 1D
    
    it = 0
    er = 1
    
    while er >= 10**(-p) and it < nMax:
        for i in range(n):
            x[i] = B[i] @ x + d[i]  # Agora x é um vetor 1D
            
        er = np.max(np.abs(x - xOld)) / np.max(np.abs(x))
        xOld = np.copy(x)  # Atualiza xOld
        it += 1  # Incrementa o contador de iterações
    
    return x, it

# Inicializando x0 como um vetor de zeros
n, _ = np.shape(A)
x0 = np.zeros(n)

# Chamando a função
x, it = seidel(A, b, 30, x0, 30)
print(f'O valor da solução após {it} iterações é: \n{x}')
