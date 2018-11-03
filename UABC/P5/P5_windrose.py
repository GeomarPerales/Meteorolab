#PRACTICA 5.
#Uso de la Rosa de Viento

#1. LIBRERIAS

import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np

import portolan
import metpy.calc as mpcalc
from metpy.units import units

from windrose import WindroseAxes

dir_file='D:/geomar/modulos/programacion/python/code.python/meteorolab'
excel='/000527.xlsx'

xls_file=dir_file+excel

obs_encoding=open(xls_file,'r') #de no conocer el "encoding"
                                #lo extraemos de esta variable

#2. IMPORTANCIA DEL ARCHIVO/DATA
#asignacion de variables

#importando como excel
data=pd.read_excel(xls_file,sheet_name='Hoja1')


#3. ANALISIS ESTADISTICO DE LA MUESTRA
data.describe()

#4. PREPARACION DE DATOS
#para observar las cabezas de columnas
data.columns

#asignando variables a nuestros datos de interes
wind=data.Velocidad[2:].to_frame(name='velocidad')
direction=data.Direccion[2:].to_frame(name='direccion')

#cambiando la direccion cardinal a angular
angle=np.zeros((len(direction)-1)) #añado el dos para igualar size de ambas columnas

#corregir
#cambiar la denominacion: NS por NW

for i in range(2,len(angle)):
    angle[i]=portolan.middle(direction.direccion[i])

ws = wind.values
ws = np.delete(ws, [1,])
ws = np.array(ws, dtype = 'float')

#5. construcción de la rosa de viento
#5.1. Rosa de Vientos de histograma apilado normado
#(representado en porcentaje)
ax = WindroseAxes.from_ax()
ax.bar( angle, ws, normed = True, opening = 0.8, edgecolor = 'white')
ax.set_legend()

plt.savefig(dir_file+'/windrose_normado.png')

#5.2. Rosa de Vientos de histograma apilado no normado con rangos
ax = WindroseAxes.from_ax()
ax.box( angle, ws, bins = np.arange(0,10,1))
ax.set_legend()

plt.savefig(dir_file+'/windrose_rangos.png')

#5.3. Rosa de Vientos con relleno y mapa de color definido
ax = WindroseAxes.from_ax()
ax.contourf( angle, ws, bins = np.arange(0,10,1), cmap = cm.hot)
ax.set_legend()

plt.savefig(dir_file+'/windrose_relleno.png')

#5.4. Rosa de Vientos con relleno y lineas de contorno
ax = WindroseAxes.from_ax()
ax.contourf( angle, ws, bins = np.arange(0,10,1), cmap = cm.hot)
ax.contour( angle, ws, bins = np.arange(0,10,1), colors = 'black')
ax.set_legend()

plt.savefig(dir_file+'/windrose_relleno_contorno.png')

#5.5. Rosa de Vientos con lineas de contorno
ax = WindroseAxes.from_ax()
ax.contour( angle, ws, bins = np.arange(0,10,1), cmap = cm.hot, lw = 3)
ax.set_legend()

plt.savefig(dir_file+'/windrose_lineas_contorno.png')

