# W3_Project_Pablo


![tibus](https://c.tenor.com/1KlsutPHdpMAAAAC/bruce-nemo.gif)




El objetivo de este proyecto era limpiar la base de datos de la página de Kagle: Global Shark Attacks, para analizar los ataques de tiburón.

## HIPÓTESIS: 

¿Son los tiburones blancos los mas agresivos y mortíferos de todos los tiburones?

## DOCUMENTOS:

Deathstype, whity y sharky son los .csv que he exportado tras la limpieza de las variables que he considerado necesarias para comprobar mi hipótesis. 

Sharknado_limpiezaDF es el jupyter notebook en donde he desarrollado la limpieza del data frame inicial.

Visualization es el jupyter en donde he analizado los .csv finales para comprobar la hipótesis y donde he incorporado los graficos. 

## LIBRERÍAS IMPORTADAS (technology stack):

- [seaborn](https://seaborn.pydata.org/) as sns
- [matplotlib.pyplot](https://matplotlib.org/) as plt
- [pandas](https://pandas.pydata.org/) as pd
- [numpy](https://numpy.org/) as np
- [re](https://github.com/python/cpython/blob/3.10/Lib/re.py) (regex)
- [plotly.express](https://plotly.com/python/) as px

## LIMPIEZA DE LA BASE DE DATOS:

He empezado cambiando el nombre y analizando las variables de las que disponía, para seleccionar cuales limpiar para poder comprobar mi hipótesis (Sharky). 

Decidí limpiar las variables que identificaban que tipo de tiburón les había mordido; la variable que analizaba el tipo de percance que había ocurrido; el género de las víctimas y por último si había resultado en la muerte del afectado o no. 


## ANÁLISIS:

Tras importar las librerías y los .csv, analizamos la resolución de los ataques de tiburón en general. Después hacemos lo mismo para los del tiburón blanco, con lo que descubrimos que tiene el segundo mayor ratio de muerte por ataque y el mayor ratio de que tras el ataque no haya herido. 

## CONCLUSIÓN

El tiburón blanco es el más agresivo porque tiene muchos mas ataque que el resto de los tiburones, es el segundo mas mortífero despues del tiburón tigre y es el tiburon con mayor porcentaje de ataque sin heridos.