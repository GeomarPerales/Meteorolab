#PRACTICA 1.

#1. Librerias

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#2. Importación de datos

dir_file='D:/geomar/modulos/programacion/python/code.python/meteorolab'
excel='/data_miraflores.csv'

xls_file=dir_file+excel

obs_encoding=open(xls_file,'r') #de no conocer el "encoding"
                                #lo extraemos de esta variable

#2. IMPORTANCIA DEL ARCHIVO/DATA

#importando como csv

data=pd.read_csv(xls_file,encoding='cp1252')

#3. TRATAMIENTO DE DATOS
#3.1. ACUMULADOS MENSUALES
suma_mensual=np.zeros((len(data.DIA)))
suma=0

#reemplazo de los NAN por 0 para efectuar la suma
data=data.replace(-999,0)
data_proc=data.fillna(0)

#ciclo acumulativo diario
for j in range(0,len(data.DIA)):
    for i in range(0,len(data.ix[0][6:])):
        suma_mensual[j]=data_proc[f'{i}'][j].sum()/len(data.ix[0][6:])+suma_mensual[j]

#convirtiendo array en dataframe
diario_prom=pd.DataFrame({'mensual':suma_mensual})   

#4. ORDENAMIENTO DE DATA MENSUAL
diario=data.loc[:,['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']]


#5. VISUALIZACION DE RESULTADOS
#Temperatura de la primera hora '0', se reemplaza los 0 por NAN
#para realizar el grafico
plt.figure(1)
plt.plot(data_proc['0'].replace(0,np.nan))
plt.title('Temperatura diaria')
plt.xlabel('meses')
plt.ylabel('Temperatura (°C)')
plt.savefig(dir_file+'/T0_miraflores.png')


#Temperatura promedio mensual
plt.figure(2)
plt.title('Temperatura Promedio Diaria')
plt.xlabel('meses')
plt.ylabel('Temperatura (°C)')
plt.scatter(np.arange(len(diario_prom)),diario_prom,s=1.5)
plt.savefig(dir_file+'/Tprom_miraflores.png')



   
