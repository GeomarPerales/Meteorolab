#PRACTICA 3.
#Comportamiento temporal de variables hidrológicas comúnes

#Estación      :  Ñaña

#Departamento  :  Lima
#Provi         :  Lima
#Distrito      :  Lurigancho


#1.LIBRERIAS

import pandas as pd
import ast
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import pyplot
import numpy as np

#2. IMPORTACIÓN DEL ARCHIVO

dir_file='D:/geomar/modulos/programacion/python/code.python/meteorolab'
txt='/qc00000543.txt'

txt_file=dir_file+txt

obs_encoding=open(txt_file,'r') #de no conocer el "encoding"
                                #lo extraemos de esta variable

#asignacion de variables

var=('year','mes','dia','Prec','Tmax','Tmin')

#importando como txt

data=pd.read_csv(txt_file,encoding='cp1252',delim_whitespace=True,names=var)

#importando como tabla

data_tabla=pd.read_table(txt_file,delim_whitespace=True,names=var)


#3.ANALISIS ESTADISTICO SIMPLE DE LA MUESTRA

#analisis estadistico de la tabla por cada variable asignada

data.describe()


#4. VISUALIZACIÓN DE DATOS

# de la columna de datos de la variable años

year=data['year']   #year : nombre de columna asignado
year_forma2=data.year

#almacenando datos  por columnas

Tmax=data.loc[:,['year','mes','dia','Tmax']] #Year, mes, día y Tmax
                                             # : almacena todas las variables
#matrices cruzadas
#año y meses                                             
Prec=pd.crosstab(data.year,data.mes) #Prec                                             


#5. APLICACIÓN DE FILTROS

#para casos mas especificos usando
#ver datos menores a 1980

data_m1980=data[data['year']<1980]

#ver datos menores a 1980 y prec. menores a 0

data_filtro1=data[(data['year']<1980) & (data['Prec']<0)]


#ver datos mayores a 1980 y prec. menores a 0 y Tmax menores a 0

data_filtro2=data[(data['year']>1980) & (data['Prec']<0) & (data['Tmax']<0)]


#para un caso mas practico
#ajuste de variables menores a 0

data_filtro3=data[(data['Prec']<0) & (data['Tmax']<0) & (data['Tmin']<0)]

#Generando series de tiempo de días, meses y años

start=dt.datetime(data.year[1],data.mes[1],data.dia[1])
nrow=len(data)-1
end=dt.datetime(data.year[nrow],data.mes[nrow],data.dia[nrow])

days_serie=pd.date_range(start,end)


#6. GRAFICO DE DATOS
Tmax_data=np.column_stack((data.year,data.Tmax))

#grafico de lineas
Lw=0.4
Ms=4

plt.figure(1)

plt.title('Tiempo vs Temperatura máxima')
plt.xlabel('Tiempo (En años) ')
plt.ylabel('Temperatura (en C°)')
plt.plot(data.year,data.Tmax,'r',linewidth=Lw,markersize=Ms)
plt.savefig(dir_file+'/Tmax.png')

plt.figure(2)

plt.title('Tiempo vs Temperatura minima')
plt.xlabel('Tiempo (En años) ')
plt.ylabel('Temperatura (en C°)')
plt.plot(data.year,data.Tmin,'b',linewidth=Lw,markersize=Ms)
plt.savefig(dir_file+'/Tmin.png')

plt.figure(3)

plt.title('Precipitación')
plt.xlabel('Tiempo (En años) ')
plt.ylabel('Precipitación (en mm)')
plt.plot(data.year,data.Prec,'g',linewidth=Lw,markersize=Ms)
plt.savefig(dir_file+'/Precipitacion.png')


