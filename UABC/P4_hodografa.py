#PRACTICA 4.
#Uso de la Hodografa

#La hodógrafa comunica la misma información que un perfil vertical del viento,
#pero como su principal propósito es revelar la cortante vertical de viento se
#basa en los vectores de viento. los vectores indican la velocidad con su longitud.

#Los vectores del viento se plotean en un sistema de coordenadas polares
#(los ejes representan los cuatro puntos cardinales).  Todos los vectores del
#viento se extienden desde el centro del sistema de coordenadas (origen) en la
#dirección de su movimiento.  Es decir que un viento del sudoeste se dibujará
#como una flecha que comienza en el centro del diagrama dirigiéndose hacia
#el noreste.  Su longitud estará dada por la velocidad del viento.  Para ello
#el diagrama tiene una serie de círculos concéntricos alrededor del punto de
#origen que representan velocidades constantes.

#Se van dibujando todos los vectores del viento en diferentes niveles de altura,
#en orden.  Luego se traza la línea que une los extremos de dichos vectores.
#Típicamente los vectores no se dibujan, sólo se traza la línea que une los extremos.

#1. LIBRERIAS

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import portolan
import metpy.calc as mpcalc
from metpy.units import units
from metpy.plots import Hodograph
#from metpy.plots import SkewT

#OBS: hay un error cuando se trabaja con add_metpy_logo y SkewT

url='https://www.senamhi.gob.pe/mapas/mapa-estaciones/_dat_esta_tipo.php?estaciones=000527'

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
angle=np.zeros(len(direction)+2) #añado el dos para igualar size de ambas columnas

#corregir
#cambiar la denominacion: NS por NW

for i in range(2,len(direction)+2):
    angle[i]=portolan.middle(direction.direccion[i])


#5. GENERACIÓN DE LA HODOGRAFA
angle=pd.DataFrame(angle[2:],columns=['angulo'])    

wind_speed=wind.values*units.knots
wind_dir=angle.values*units.degrees

u,v=mpcalc.wind_components(wind_speed,wind_dir)

#visualizando la hodografa
fig=plt.figure(figsize=(6,6))
fig.suptitle('Hodografa - Estacion 000527')

ax=fig.add_subplot(1,1,1)
h=Hodograph(ax,component_range=10.)
h.plot(u,v,linewidth=5)
h.add_grid(increment=5)
plt.savefig(dir_file+'/hodografa.png')

#resultado: dado que la hodografa es casi constante en todo la figura
#concluimos que la velocidad del viento es casi constante en modulo y direccion

