import pandas as import pd 
import numpy as np 

import featuretools as ft 
import featuretools.variable_types as vtypes 

import sys 
import psutil 
import os 

from timeit import default_timer as timer 

# Algoritmo basado en la liga:
# https://github.com/Featuretools/Automated-Manual-Comparison/blob/master/Loan%20Repayment/notebooks/Featuretools%20on%20Dask.ipynb
# recomiendan utilizar data type category en lugar de object,
# pues reduce tiempos en memoria.

def convert_types(df):
    """Convert pandas data types for memory reduction."""
    
    # Iterate through each column
    for c in df:
        
        # Convert ids and booleans to integers
        if ('SK_ID' in c):
            df[c] = df[c].fillna(0).astype(np.int32)
            
        # Convert objects to category
        elif (df[c].dtype == 'object') and (df[c].nunique() < df.shape[0]):
            df[c] = df[c].astype('category')
        
        # Booleans mapped to integers
        elif set(df[c].unique()) == {0, 1}:
            df[c] = df[c].astype(bool)
        
        # Float64 to float32
        elif df[c].dtype == float:
            df[c] = df[c].astype(np.float32)
            
        # Int64 to int32
        elif df[c].dtype == int:
            df[c] = df[c].astype(np.int32)
        
    return df


def create_partition(user_list, partition):
    """Creates and saves a dataset with only the users in `user_list`."""
    
    # Make the directory
    directory = '../input/partitions/p%d' % (partition + 1)
    if os.path.exists(directory):
        return
    
    else:
        os.makedirs(directory)
        
        # Subset based on user list
        app_subset = app[app.index.isin(user_list)].copy().reset_index()
        bureau_subset = bureau[bureau.index.isin(user_list)].copy().reset_index()

        # Drop SK_ID_CURR from bureau_balance, cash, credit, and installments
        bureau_balance_subset = bureau_balance[bureau_balance.index.isin(user_list)].copy().reset_index(drop = True)
        cash_subset = cash[cash.index.isin(user_list)].copy().reset_index(drop = True)
        credit_subset = credit[credit.index.isin(user_list)].copy().reset_index(drop = True)
        previous_subset = previous[previous.index.isin(user_list)].copy().reset_index()
        installments_subset = installments[installments.index.isin(user_list)].copy().reset_index(drop = True)
        

        # Save data to the directory
        app_subset.to_csv('%s/app.csv' % directory, index = False)
        bureau_subset.to_csv('%s/bureau.csv' % directory, index = False)
        bureau_balance_subset.to_csv('%s/bureau_balance.csv' % directory, index = False)
        cash_subset.to_csv('%s/cash.csv' % directory, index = False)
        credit_subset.to_csv('%s/credit.csv' % directory, index = False)
        previous_subset.to_csv('%s/previous.csv' % directory, index = False)
        installments_subset.to_csv('%s/installments.csv' % directory, index = False)

        if partition % 10 == 0:
            print('Saved all files in partition {} to {}.'.format(partition + 1, directory))
            

# Break into 104 chunks
chunk_size = app.shape[0] // 103

# Construct an id list
id_list = [list(app.iloc[i:i+chunk_size].index) for i in range(0, app.shape[0], chunk_size)]


from itertools import chain

# Sanity check that we have not missed any ids
print('Number of ids in id_list:         {}.'.format(len(list(chain(*id_list)))))
print('Total length of application data: {}.'.format(len(app)))

start = timer()
for i, ids in enumerate(id_list):
    # Create a partition based on the ids
    create_partition(ids, i)
    
end = timer()
print(f'Partitioning took {round(end - start)} seconds.')


def convierte_a_numericas_parallel():
    """
    Función que hace la conversión a numéricas de todas las columnas en paralelo. 
    Args: 
    nombre de columna: columna sobre la que está trabajando el algoritmo
    
    """
    return None




