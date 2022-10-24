"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    dataset=pd.read_fwf("clusters_report.txt", widths = [9, 16, 16, 80], skiprows = [0,1,2,3],
    names = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'], 
    na_filter = False)


    for indice, contenido in enumerate(dataset['cluster']):
        if contenido =='':
            dataset['cluster'].iloc[indice] = dataset['cluster'].iloc[indice-1]

    for indice, contenido in enumerate(dataset['cantidad_de_palabras_clave']):
        if contenido =='':
            dataset['cantidad_de_palabras_clave'].iloc[indice] = dataset['cantidad_de_palabras_clave'].iloc[indice-1]

    for indice, contenido in enumerate(dataset['porcentaje_de_palabras_clave']):
        if contenido =='':
            dataset['porcentaje_de_palabras_clave'].iloc[indice] = dataset['porcentaje_de_palabras_clave'].iloc[indice-1]

    dataset['porcentaje_de_palabras_clave'].replace({"%": ''}, regex=True, inplace=(True))
    dataset['porcentaje_de_palabras_clave'].replace({",": '.'}, regex=True, inplace=(True))

    dataset['cluster'] = dataset['cluster'].astype(int)
    dataset['cantidad_de_palabras_clave'] = dataset['cantidad_de_palabras_clave'].astype(int)
    dataset['porcentaje_de_palabras_clave'] = dataset['porcentaje_de_palabras_clave'].astype(float)

    dataset = dataset.groupby(['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave'])['principales_palabras_clave'].apply(' '.join).reset_index()

    dataset['principales_palabras_clave'].replace({", ": ","}, regex=True, inplace=(True))
    dataset['principales_palabras_clave'].replace({",": ", "}, regex=True, inplace=(True))
    dataset['principales_palabras_clave'] = dataset['principales_palabras_clave'].str.strip()
    dataset["principales_palabras_clave"] = dataset["principales_palabras_clave"].str.rstrip('.')
    dataset['principales_palabras_clave'].replace({"  ": " "}, regex=True, inplace=(True))
    dataset['principales_palabras_clave'].replace({"   ": " "}, regex=True, inplace=(True))
    dataset['principales_palabras_clave'].replace({"    ": " "}, regex=True, inplace=(True))
    dataset['principales_palabras_clave'].replace({"     ": " "}, regex=True, inplace=(True))

    return dataset
