# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:42:16 2020

@author: Elizabeth
"""

import sklearn as sk
import pandas as pd
import numpy as np 
import math

from sklearn import preprocessing
from sklearn.decomposition import PCA


def componentes_principales(X, n_components):
    """
    componentes_principales(X): Función que devuelve las componentes principales.
    
    Parámetros
    ----------
    n_components: número de componentes. 
    
    svd_solver: str {‘auto’, ‘full’, ‘arpack’, ‘randomized’}
        Se elige 'full', lo que significa que se ejecuta completamente SVD llamando al 
        solucionador estándar LAPACK a través de scipy.linalg.svd y se seleccionan los componentes mediante postprocessing.
        
    Atributos
    ---------
    
    var_exp: porcentaje de varianza explicada por cada componente.
                
    val_sing: valores singulares correspondientes a cada componente.
        
    pca.components_: representan las direcciones de máxima varianza en los datos.
    
    Método
    ---------
    
    fit_transform: ajusta el modelo a los datos y aplica la reducción de dimensionalidad en los datos.
    
    """
    pca = PCA(n_components, svd_solver='full')
        
    componentesprincipales = pca.fit_transform(X)
    
    pca.components_
    
    var_exp = pca.explained_variance_ratio_
    
    eigenvalues = pca.explained_variance_
    
    val_sing = pca.singular_values_
    
    return pca, var_exp, componentesprincipales, val_sing, pca.components_, eigenvalues







