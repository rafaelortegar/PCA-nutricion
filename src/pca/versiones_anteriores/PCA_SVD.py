import codecs
import numpy as np
import pandas as pd
import sys


def PCA_from_SVD(A,num_componentes):
    """
    Función para PCA a partir de la SVD 
    params: A			matriz de datos
            num_componentes 	número de componentes deseados

    return: valores_singulares	Los valores singulares de la descomposición SVD
	    componentes		Los coeficientes para calcular los componentes principales
	    Z			Los datos transformados (componentes principales)
	    varianza_explicada	La varianza explicada por cada componente principal
    """
    
    # Centrar los datos
    A = np.array(A) # convertir los datos a un numpy array por si vienen de un DataFrame
    A_centered = A - A.mean(axis=0)
    
    # Modificar esta línea de código, mandar a llamar la función creada por el equipo 
    # Calcular SVD
    U, S, Vt = np.linalg.svd(A_centered, full_matrices=False)
    
    # Los valores singulares
    valores_singulares = S
    
    # Los componentes (coeficientes)
    componentes = (np.transpose(Vt))*-1
    
    # Los datos transformados (componentes principales)
    Z = A_centered@np.transpose(Vt)
    
    # La varianza explicada
    varianza_explicada = S**2/np.sum(S**2)
    
    # regresar 4 objetos
    return valores_singulares, componentes, Z, varianza_explicada


