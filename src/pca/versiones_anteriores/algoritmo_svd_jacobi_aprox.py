#!/usr/bin/env python
# coding: utf-8

import codecs
import sys
import numpy as np
import pandas as pd


# Función que verifica si dos vectores son ortogonales de acuerdo a cierto nivel de tolerancia
def verificar_ortogonalidad(u,v,tol = 10**-8):
    if np.linalg.norm(u) <= tol or np.linalg.norm(v) <= tol:
        resultado = 1
    elif ((np.dot(u,v))/(np.linalg.norm(u)*np.linalg.norm(v))) <= tol:
        resultado = 1
    else:
        resultado = 0
    return resultado

# Función signo
def signo(x):
    if x<0:
        sig = -1
    else:
        sig = 1
    return sig



def svd_jacobi_aprox(A,TOL,maxsweep):
    # Calcula la descomposición de una matriz A en sus componentes U, S V, 
    # utilizando el método de Jacobi para calcular la factorización SVD.De esta forma 
    # la matriz A queda descompuesta de la siguiente forma: A = U*S*t(V).
    # Args: 
    #    A (matriz): Matriz de entrada (nxm) de números reales a la que se le calculará la descomposición SVD.
    #    TOL (numeric): controla la convergencia del método, siendo un valor real de 10^-8 (sugerido en la nota 3.3.d.SVD)
    #    Nota: Se sugiere una TOL mayor a 10^-32.
    #    maxsweep (numeric): número máximo de sweeps,donde cada sweep consiste de un número máximo(nmax)
    #    de rotaciones; y en cada sweep se ortogonalizan 2 columnas.
    # Returns: 
    #   Lista con 3 elementos, donde el primer elemento representa a la matriz U(nxm),el segundo a la matriz S(mxm) matriz diagonal
    #   y el tercero y último a la matriz V (mxm).En conjunto estas tres matrices componen la factorización SVD de la matriz de entrada A.
    # Nota: Esta función estima la SVD thin,la cual calcula unicamente las m columnas de U correspondientes a los m renglones de V. De esta
    # manera las columnas restantes de U no son calculadas, provocando una mejora significativa en velocidad de ejecución comparada con la 
    # la Full SVD. Referencia: https://en.wikipedia.org/wiki/Singular_value_decomposition#Thin_SVD.
    
    #dimensiones de A
    n = A.shape[1] #numero de columnas
    m = A.shape[0] #numero de filas
    nmax =n*(n-1)/2
    
    #inicializa valores del ciclo
    ak = A
    vk = np.identity(n, dtype = float) 
    sig = ''
    uk = ak
    num_col_ortogonal = 0
    k = 0
    stop = False
        
    
    while(k<=maxsweep & num_col_ortogonal<nmax):
        num_col_ortogonal =0
        for i in range(n-1):
            for j in range(i+1,n):
                col_j = ak[:,j]
                col_i = ak[:,i]

                #comprueba ortogonalidad  
                if(verificar_ortogonalidad(col_i,col_j,TOL)==1):
                    num_col_ortogonal =num_col_ortogonal+1
                else:
                    #calcula coeficientes de la matriz
                    a = np.dot(col_i,col_i)
                    b = np.dot(col_j,col_j)
                    c = np.dot(col_i,col_j)

                    #si c es cercano a cero no actualiza
                    if(c<TOL):
                        stop =True
                        break

                    #calcula la rotacion givens que diagonaliza
                    epsilon = (b-a)/(2*c)
                    t = signo(epsilon)/(abs(epsilon)+np.sqrt(1+epsilon**2))
                    cs = 1/np.sqrt(1+t**2)
                    sn = cs*t

                    #actualiza las columnas de la matriz ak
                    temp1 = ak[:,i].copy()
                    ak[:,i] = cs*temp1-sn*ak[:,j]
                    ak[:,j] = sn*temp1+cs*ak[:,j]


                    #actualiza las columnas de la matriz vk
                    temp2 = vk[:,i].copy() 
                    vk[:,i] = cs*temp2-sn*vk[:,j]
                    vk[:,j] = sn*temp2+cs*vk[:,j]             
                #cierra else
            #cierra for j
            if(stop):
                stop = False
                break
            
        #cierra for i
        k = k+1
     #cierra while
    
      
    #Obtener sigma (normas euclidianas de columnas de ak)
    sig = np.linalg.norm(ak, axis=0)

    #Obtener U (columnas normalizadas de ak)
    for i in range(n):
        if (sig[i]<TOL):
            uk[:,i] = 0  
        else:
            uk[:,i] = ak[:,i]/sig[i]
        

    # Indices de sigma ordenada en forma decreciente para ordenar V,S,U
    #index <- order(sig,decreasing = TRUE)
    index = np.argsort(sig) # Obtenemos los indices de sig ordenado
    index = index[::-1] # Invertimos, para obtener los índices del orden decreciente
    #Reordenamos
    V = vk[:,index]
    s = sig[index]
    U = uk[:,index]
    
    return U, s, V  


