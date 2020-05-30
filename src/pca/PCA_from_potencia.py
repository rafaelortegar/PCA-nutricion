import numpy as np
import pandas as pd

def power_iteration(A, num_simulations: int):
    # Ideally choose a random vector
    # To decrease the chance that our vector
    # Is orthogonal to the eigenvector
    b_k = np.random.rand(A.shape[1])

    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)

        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)

        # re normalize the vector
        b_k = b_k1 / b_k1_norm
    
    #Obtenemos el eigenvalor correspondiente a b_k con el cociente de Rayleigh
    m_k = (b_k.T@A@b_k)/(b_k.T@b_k)
    
    #Devolvemos el mayor eigenvalor y su correspondiente eigenvector
    return m_k,b_k
	
def power_deflation(A,iter):
    #numero de columnas
    n = A.shape[1]
    # Inicializamos arrays de ceros
    eigenvalues = np.zeros(n)
    eigenvectors = np.zeros((n,n))
    #Hago una copia de la matriz original
    A_def = A.copy()
    #Iteramos tantas veces como columnas de la matriz
    for i in range(n):
        #Aplicamos el método de la potencia
        m_def,b_def = power_iteration(A_def,iter)
        #Actualizamos los arrays de eigen valores y vectores
        eigenvalues[i] = m_def
        eigenvectors[:,i]= b_def
        # Matriz actualizada
        A_def = A_def - np.outer(b_def,b_def)@A_def@np.outer(b_def,b_def)
    return eigenvalues, eigenvectors
	
def PCA_from_potencia(X):
    prop = 0 #Proporción de varianza explicada
    comp = 1 
    cur_var = 0
    comp_vecs = np.zeros([X.shape[1], X.shape[1]])
    
    # convertir a array
    A = np.array(X)
    
    # Centrar los datos
    mean_vec = np.mean(A, axis=0)
    datos_centrados = (A - mean_vec)
    
    #Calculamos la matriz de covarianzas
    cov = np.dot(X.T, X)/X.shape[0]
    
    #Aplicamos el método de la potencia
    evalues_pow, evectors_pow = power_deflation(cov,50)
    
    # La varianza explicada
    varianza_explicada = evalues_pow/np.sum(evalues_pow)
    
    # Los datos transformados (componentes principales)
    Z = datos_centrados@evectors_pow
    
    
    # Calcula número de componentes de manera automatica de acuerdo a la variana explicada
    # Threshold de 80%
    n = X.shape[1] #numero de columnas
    varianza_acumulada = varianza_explicada.cumsum()
    conteo = (varianza_acumulada)  <  0.8
    num_componentes = conteo.sum() + 1
    
    return evalues_pow[:num_componentes], evectors_pow[:num_componentes], Z[:,:num_componentes], varianza_explicada[:num_componentes] 
    