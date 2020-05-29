import numpy as np
import pandas as pd


def importa_ds():
    """
    Función que importa los datos desde sus respectivas rutas y las regresa en forma de una tupla, regresando en primer
     lugar el data frame del cuesstionario y en segundo el correspondiente a los datos de los alumnos.
    """
    cuestionario = pd.read_csv("../../data/cuestionario_2016_raw.csv", encoding='UTF-8', na_values=['>'])
    alumnos = pd.read_csv("../../data/planea_alumnos_2016.csv", encoding='UTF-8')
    return cuestionario, alumnos


def clean_column_name(df):
    """
    Función limpia el nombre de las columnas que requieren limpieza.
    """
    df.rename(columns={'ïnofolio': 'nofolio'}, inplace=True)


def une_datasets(dataset_alumnos, dataset_cuestionario):
    """
    Función que hace el proceso de limpieza sobre las columnas en ambos datasets.
    """
    return pd.merge(dataset_alumnos, dataset_cuestionario, how='inner', on=['nofolio', 'nofolio'])


def limpia_errores_en_datos(df):
    """
    Función que limpia los errores en los datos de las columnas al ser unidas. convierte en NA las respuestas inválidas.
    """
    df['p1'] = df['genero']
    df.loc[df["p1"] == "H", "p1"] = 'A'
    df.loc[df["p1"] == "M", "p1"] = 'B'
    df.loc[df["p6"] == "D", "p6"] = np.nan
    df.loc[df["p46"] == "S", "p46"] = np.nan
    df.loc[df["p55"] == "E", "p55"] = np.nan
    df.loc[df["p55"] == "G", "p55"] = np.nan
    df.loc[df["p55"] == "H", "p55"] = np.nan
    df.loc[df["p56"] == "G", "p56"] = np.nan
    df.loc[df["p58"] == "E", "p58"] = np.nan
    df.loc[df["p66"] == "G", "p66"] = np.nan
    df.loc[df["p69"] == "C", "p69"] = np.nan
    df.loc[df["p69"] == "D", "p69"] = np.nan
    df.loc[df["p69"] == "E", "p69"] = np.nan
    df.loc[df["p69"] == "F", "p69"] = np.nan
    df.loc[df["p69"] == "G", "p69"] = np.nan
    df.loc[df["p69"] == "N", "p69"] = np.nan
    df.loc[df["p69"] == "S", "p69"] = np.nan
    df.loc[df["p72"] == "G", "p72"] = np.nan
    df.loc[df["p72"] == "H", "p72"] = np.nan
    df.loc[df["p73"] == "C", "p73"] = np.nan
    df.loc[df["p73"] == "D", "p73"] = np.nan
    df.loc[df["p73"] == "E", "p73"] = np.nan
    df.loc[df["p73"] == "F", "p73"] = np.nan
    df.loc[df["p74"] == "G", "p74"] = np.nan
    df.loc[df["p75"] == "C", "p75"] = np.nan
    df.loc[df["p75"] == "D", "p75"] = np.nan
    df.loc[df["p75"] == "V", "p75"] = np.nan
    df.loc[df["p76"] == "C", "p76"] = np.nan
    df.loc[df["p76"] == "D", "p76"] = np.nan
    df.loc[df["p76"] == "E", "p76"] = np.nan
    df.loc[df["p77"] == "C", "p77"] = np.nan
    df.loc[df["p77"] == "D", "p77"] = np.nan
    df.loc[df["p77"] == "E", "p77"] = np.nan
    df.loc[df["p77"] == "F", "p77"] = np.nan
    df.loc[df["p77"] == "G", "p77"] = np.nan
    df.loc[df["p77"] == "V", "p77"] = np.nan
    df.loc[df["p79"] == "E", "p79"] = np.nan
    df.loc[df["p79"] == "F", "p79"] = np.nan
    df.loc[df["p79"] == "G", "p79"] = np.nan
    df.loc[df["p81"] == "D", "p81"] = np.nan
    df.loc[df["p81"] == "E", "p81"] = np.nan
    df.loc[df["p81"] == "F", "p81"] = np.nan
    df.loc[df["p82"] == "E", "p82"] = np.nan
    df.loc[df["p82"] == "F", "p82"] = np.nan
    df.loc[df["p83"] == "C", "p83"] = np.nan
    df.loc[df["p83"] == "D", "p83"] = np.nan
    df.loc[df["p84"] == "C", "p84"] = np.nan
    df.loc[df["p84"] == "D", "p84"] = np.nan
    df.loc[df["p84"] == "F", "p84"] = np.nan
    df.loc[df["p87"] == "E", "p87"] = np.nan
    df.loc[df["p88"] == "E", "p88"] = np.nan
    df.loc[df["p89"] == "E", "p89"] = np.nan
    df.loc[df["p109"] == "F", "p109"] = np.nan
    df.loc[df["p118"] == "C", "p118"] = np.nan
    df.loc[df["p118"] == "D", "p118"] = np.nan
    df.loc[df["p130"] == "E", "p130"] = np.nan
    df.loc[df["p131"] == "E", "p131"] = np.nan
    df.loc[df["p132"] == "C", "p132"] = np.nan
    df.loc[df["p134"] == "C", "p134"] = np.nan
    df.loc[df["p134"] == "D", "p134"] = np.nan
    df.loc[df["p137"] == "E", "p137"] = np.nan
    df.loc[df["p137"] == "F", "p137"] = np.nan
    df.loc[df["p140"] == "G", "p140"] = np.nan
    df.loc[df["p140"] == "H", "p140"] = np.nan
    df.loc[df["p145"] == "F", "p145"] = np.nan
    df.loc[df["p146"] == "D", "p146"] = np.nan
    df.loc[df["p148"] == "C", "p148"] = np.nan
    df.loc[df["p149"] == "E", "p149"] = np.nan
    df.loc[df["p150"] == "C", "p150"] = np.nan
    return df


def limpiar_ent_sost_subsist(df):
    """
    Función que limpia y agrupa algunas categorías de la columna subsist, para que al hacer el one-hot-encoding
    salgan limpios los nombres de las columnas.
    """
    for col in df[['sost', 'subsist', 'nom_ent', 'modalidad']]:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.lower()
        df[col] = df[col].str.replace(' ', '_')
        df['sost'] = df['sost'].str.replace('ï¿½', 'o')
        df['subsist'] = df['subsist'].str.replace('ï¿½', 'o')
        df['nom_ent'] = df['nom_ent'].str.replace('mï¿½xico', 'mexico')
        df['nom_ent'] = df['nom_ent'].str.replace('michoacï¿½n', 'michoacan')
        df['nom_ent'] = df['nom_ent'].str.replace('leï¿½n', 'leon')
        df['nom_ent'] = df['nom_ent'].str.replace('querï¿½taro', 'queretaro')
        df['nom_ent'] = df['nom_ent'].str.replace('potosï¿½', 'potosi')
        df['nom_ent'] = df['nom_ent'].str.replace('yucatï¿½n', 'yucatan')
    return df


def agrupa_subsistemas(df):
    """
    Función que agrupa los subsistemas por tipo, donde existen algunos subsitemas con muy pocas observaciones.
    """
    # BACH ESTATAL DGE-CGE
    df.loc[df["subsist"] == "otras_estatales", "subsist"] = "bach_estatal_dge-cge"

    # BACH AUTONOMOS
    df.loc[df["subsist"] == "bachillerato_intercultural", "subsist"] = "bachillerato_autonomo"

    # TELEBACH/EMSAD
    df.loc[df["subsist"] == "emsad", "subsist"] = "telebach/emsad"
    df.loc[df["subsist"] == "telebachilleratos_comunitarios", "subsist"] = "telebach/emsad"
    df.loc[df["subsist"] == "telebachilleratos", "subsist"] = "telebach/emsad"

    # COLBACH/Otros federales
    df.loc[df["subsist"] == "colbach", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "ipn", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "ceti", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "dgb", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "dgecytm", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "dgeta", "subsist"] = "colbach/otros_federales"
    df.loc[df["subsist"] == "otras_federales", "subsist"] = "colbach/otros_federales"

    # PARTICULARES/A.C.
    df.loc[df["subsist"] == "asociacion_civil", "subsist"] = "particulares/a.c."
    df.loc[df["subsist"] == "particulares", "subsist"] = "particulares/a.c."
    return df


def categorias_no_binarias(df):
    """
    Función que hace la codificación one-hot-encoding para las columnas que no son binarias.
    """
    categorias = ['nom_ent', 'modalidad', 'sost', 'subsist','p3', 'p4', 'p5', 'p9', 'p67', 'p70',
                  'p74', 'p138', 'p139']
    dummies = pd.get_dummies(df[categorias])
    df = df.join(dummies)
    return df




def categorias_binarias(df):
    """
    Función que hace la codificación one-hot-encoding para las columnas que son binarias.
    """
    for col in df[['p1', 'p6', 'p69', 'p73', 'p75', 'p76', 'p77', 'p83', 'p84', 'p118', 'p132', 'p133', 'p134']]:
        df.loc[df[col] == 2, col] = 0
    return df


def imputar_missings_mediana(df):
    """
    Función que realiza la imputación de los missing values en las columnas que los tienen.
    """
    cols = list(df)
    for column in cols:
        col_data = df[column]
        missing_data = sum(col_data.isna())
        if missing_data > 0:
            col_median = col_data.median()
            col_data.fillna(col_median, inplace=True)
            df[column] = col_data
    return df



# Funciones para multiprocessing
# Divide en bloques de 40 variables para tener 4 procesos

def convierte_a_numericas_proceso1():
    """
    Función que convierte las respuestas de las preguntas en una codificación del 1 al 10.
    No lleva return los cambios los hace inplane
    """
    for i in range(1, 40):
        columna = 'p' + str(i)
        dataset_unido[columna].replace('A',1,inplace=True) 
        dataset_unido[columna].replace('B',2,inplace=True) 
        dataset_unido[columna].replace('C',3,inplace=True) 
        dataset_unido[columna].replace('D',4,inplace=True) 
        dataset_unido[columna].replace('E',5,inplace=True) 
        dataset_unido[columna].replace('F',6,inplace=True) 
        dataset_unido[columna].replace('G',7,inplace=True) 
        dataset_unido[columna].replace('H',8,inplace=True) 
        dataset_unido[columna].replace('I',9,inplace=True) 
        dataset_unido[columna].replace('J',10,inplace=True) 
        #dataset_unido[columna] = df[columna].astype(float)
        
def convierte_a_numericas_proceso2():
    """
    Función que convierte las respuestas de las preguntas en una codificación del 1 al 10.
    No lleva return los cambios los hace inplane
    """
    for i in range(41, 80):
        columna = 'p' + str(i)
        dataset_unido[columna].replace('A',1,inplace=True) 
        dataset_unido[columna].replace('B',2,inplace=True) 
        dataset_unido[columna].replace('C',3,inplace=True) 
        dataset_unido[columna].replace('D',4,inplace=True) 
        dataset_unido[columna].replace('E',5,inplace=True) 
        dataset_unido[columna].replace('F',6,inplace=True) 
        dataset_unido[columna].replace('G',7,inplace=True) 
        dataset_unido[columna].replace('H',8,inplace=True) 
        dataset_unido[columna].replace('I',9,inplace=True) 
        dataset_unido[columna].replace('J',10,inplace=True) 
        #dataset_unido[columna] = df[columna].astype(float)        

def convierte_a_numericas_proceso3():
    """
    Función que convierte las respuestas de las preguntas en una codificación del 1 al 10.
    No lleva return los cambios los hace inplane
    """
    for i in range(81, 120):
        columna = 'p' + str(i)
        dataset_unido[columna].replace('A',1,inplace=True) 
        dataset_unido[columna].replace('B',2,inplace=True) 
        dataset_unido[columna].replace('C',3,inplace=True) 
        dataset_unido[columna].replace('D',4,inplace=True) 
        dataset_unido[columna].replace('E',5,inplace=True) 
        dataset_unido[columna].replace('F',6,inplace=True) 
        dataset_unido[columna].replace('G',7,inplace=True) 
        dataset_unido[columna].replace('H',8,inplace=True) 
        dataset_unido[columna].replace('I',9,inplace=True) 
        dataset_unido[columna].replace('J',10,inplace=True) 
        #dataset_unido[columna] = df[columna].astype(float)

def convierte_a_numericas_proceso4():
    """
    Función que convierte las respuestas de las preguntas en una codificación del 1 al 10.
    No lleva return los cambios los hace inplane
    """
    for i in range(121, 155):
        columna = 'p' + str(i)
        dataset_unido[columna].replace('A',1,inplace=True) 
        dataset_unido[columna].replace('B',2,inplace=True) 
        dataset_unido[columna].replace('C',3,inplace=True) 
        dataset_unido[columna].replace('D',4,inplace=True) 
        dataset_unido[columna].replace('E',5,inplace=True) 
        dataset_unido[columna].replace('F',6,inplace=True) 
        dataset_unido[columna].replace('G',7,inplace=True) 
        dataset_unido[columna].replace('H',8,inplace=True) 
        dataset_unido[columna].replace('I',9,inplace=True) 
        dataset_unido[columna].replace('J',10,inplace=True) 
        #dataset_unido[columna] = df[columna].astype(float)      
        
        


def prepara_datos():
    """
    Función que importa y prepara los datos para su uso, realizando limpieza e imputación. Por otro lado, utiliza todas
    las funciones previamente descritas para este propósito.
    """
    print("\t-> Importando los datos")
    cuestionario, alumnos = importa_ds()

    print("\t-> Limpiamos los nombres de las columnas")
    clean_column_name(alumnos)

    print("\t-> Unimos los datasets")
    dataset_unido = une_datasets(alumnos, cuestionario)

    print("\t-> Limpiamos los errores en los datos del cuestionario")
    dataset_unido = limpia_errores_en_datos(dataset_unido)

    print("\t-> Limpiamos los datos de entidad sostenimiento y subsistema ")
    dataset_unido = limpiar_ent_sost_subsist(dataset_unido)

    print("\t-> Agrupamos la variable de subsistema")
    dataset_unido = agrupa_subsistemas(dataset_unido)

    print("\t-> Creamos variables categóricas no binarias")
    dataset_unido = categorias_no_binarias(dataset_unido)

    # Sección que convierte a númericas en multiprocessing
    print("\t-> Convertimos variables categoricas a númericas de forma paralela")
    p1 = multiprocessing.Process(target = convierte_a_numericas_proceso1) 
    p2 = multiprocessing.Process(target = convierte_a_numericas_proceso2) 
    p3 = multiprocessing.Process(target = convierte_a_numericas_proceso3) 
    p4 = multiprocessing.Process(target = convierte_a_numericas_proceso4) 

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("\t-> Recodificamos variables categóricas binarias")
    dataset_unido = categorias_binarias(dataset_unido)

    print("\t-> Imputamos las columnas con missings con la mediana")
    dataset_unido = imputar_missings_mediana(dataset_unido)

    print("\t-> Exportando un csv con los datos limpios")
    dataset_unido.to_csv(r'../../data/datos_limpios.csv', index=False, header=True)

    return dataset_unido


# Funciones auxiliares
def convert_to_categorical(df):
    """
    Función que convierte todas las funciones tipo object en categóricas.
    """
    for col in df.select_dtypes('object'):
        df[col] = df[col].astype('category')
    return df


def cuenta_nulos_por_columnas(df):
    """
    Función que realiza una tabla con la cuenta de missing values por columna y obtiene la proporción que estos missing
    values representan del total.
    """
    valores_nulos = df.isnull().sum()
    porcentaje_valores_nulos = 100 * df.isnull().sum() / len(df)
    tabla_valores_nulos = pd.concat([valores_nulos, porcentaje_valores_nulos], axis=1)
    tabla_valores_nulos_ordenada = tabla_valores_nulos.rename(
        columns={0: 'Missing Values', 1: '% del Total'})
    tabla_valores_nulos_ordenada = tabla_valores_nulos_ordenada[
        tabla_valores_nulos_ordenada.iloc[:, 1] != 0].sort_values(
        '% del Total', ascending=False).round(1)
    print("El dataframe tiene " + str(df.shape[1]) + " columnas.\n"
                                                     "Hay " + str(tabla_valores_nulos_ordenada.shape[0]) +
          " columnas que tienen NA's.")
    return tabla_valores_nulos_ordenada


def cuenta_nulos_por_renglones(df):
    """
    Función que cuenta la cantidad de valores nulos por cada renglón, para valorar si es posible o no realizar
    imputaciones o se tendrían que tirar las columnas o renglones correspondientes.
    """
    df_aux = df.copy()
    valores_nulos_totales = sum(df_aux.apply(lambda x: sum(x.isnull().values), axis=1) > 0)
    print("Existen un total de: ", valores_nulos_totales, "renglones con al menos un valor nulo\n")
    numero_de_lineas = len(df_aux)
    porcentaje_de_lineas_con_nulos = valores_nulos_totales / numero_de_lineas
    texto = "Representan el {:.2%} del total de renglones.". \
        format(porcentaje_de_lineas_con_nulos)
    print(texto)
    return valores_nulos_totales

# def cuenta_nulos_por_renglones(df):
#    for i in range(len(df.index)):
#        print("Nan in row ", i, " : ", df.iloc[i].isnull().sum())
#    sum([True for idx, row in df.iterrows() if any(row.isnull())])
#    list(df.index[df.isnull().sum(axis=1) > 0])
#    tabla_valores_nulos_ordenada = 0
#    return tabla_valores_nulos_ordenada
