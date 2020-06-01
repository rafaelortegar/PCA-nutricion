# Proyecto Final de la materia de Métodos Numéricos y Optimización de la Maestría en Ciencia de Datos

**Profesor:** Erick Palacios Moreno

**Integrantes del equipo**

| # | Alumno                            | Clave única | usuario de Github                                              |Roles|
|---|-----------------------------------|-------------|----------------------------------------------------------------|---|
| 1 | Angel Rafael Ortega Ramírez       | 123972      | [123972](https://github.com/123972)                            |Project Manager|
| 2 | Elizabeth Rodriguez               | 191430      | [erodriguezul](https://github.com/erodriguezul)                |Revisión de código|
| 3 | Karla Alfaro Pizaña               | 137314      | [alpika19186](https://github.com/alpika19186)                  |Revisión de código |
| 4 | Leonardo Marín                    | 175903      | [leonardomarintellez](https://github.com/leonardomarintellez)  |Programador|
| 5 | Mario Rodríguez                   | 164471      |[shimanteko](https://github.com/shimanteko)   |Programador|
| 6 | Elizabeth Viveros                 | 161224      |[ElyVV](https://github.com/ElyVV)   |Programadora|

# Estructura del repositorio

La estructura del repositorio está basado en [este](https://drivendata.github.io/cookiecutter-data-science/) template y
 está organizado de la siguiente forma:

- Carpeta [avances](https://github.com/123972/PCA-nutricion/tree/master/avances): contiene
 los avances de cada una de las etapas del proyecto.

- Carpeta [data](https://github.com/123972/PCA-nutricion/tree/master/data): contiene la base de datos a utilizar,
así como información sobre el procedimiento de feature engineering a seguir para unir ambas bases de datos y la limpieza
de las variables.

- Carpeta [docker](https://github.com/123972/PCA-nutricion/tree/master/docker): Contiene la información 
pertienete para poder correr los scripts y notebooks en un contenedor de docker.

- Carpeta [docs](https://github.com/123972/PCA-nutricion/tree/master/docs): Contiene el cuestionario utlilizado
durante la encuesta en la que se obtuvieron los datos utilizados en este proyecto, así como las 
[imágenes](https://github.com/123972/PCA-nutricion/tree/master/docs/images) empleadas en el README.md y las 
[referencias](https://github.com/123972/PCA-nutricion/tree/master/docs/References) utilizadas durante el 
proyecto.

- Carpeta [environment](https://github.com/123972/PCA-nutricion/tree/master/environment): Contiene el 
ambiente con las instalaciones de python empleadas en este proyecto. Dichas instalaciones también se pueden instalar vía
el archivo de requirements.txt

- Carpeta [notebooks](https://github.com/123972/PCA-nutricion/tree/master/notebooks): Contiene cinco carpetas 
con los notebooks y scripts de la sección del 
[EDA](https://github.com/123972/PCA-nutricion/tree/master/notebooks/EDA), 
[Programación](https://github.com/123972/PCA-nutricion/tree/master/notebooks/Programacion)
  y [Revisión](https://github.com/123972/PCA-nutricion/tree/master/notebooks/Revision).   

- Carpeta [results](https://github.com/123972/PCA-nutricion/tree/master/results):Esta carpeta contiene los resultados obtenidos por el proyecto, así como la presentación y el reporte final.

- Carpeta [src](https://github.com/123972/PCA-nutricion/tree/master/src): Incluye todos los scripts separados en dos secciones:[PCA](https://github.com/123972/PCA-nutricion/tree/master/src/pca) y [test algorithms](https://github.com/123972/PCA-nutricion/tree/master/src/test_algorithms) 




_____________________________________________________

# Indicaciones
Cada integrante tendrá una calificación (un número: de 0 a 10) dependiendo de su trabajo individual. Para la revisión del trabajo por cada integrante, se seleccionarán y agendarán equipos durante los sábados de los meses de abril y mayo en los que se deberá exponer lo que han realizado.

En el nivel:

`analisis-numerico-computo-cientifico/proyecto_final/proyectos/equipos`

se tendrán directorios para que cada equipo coloque los avances que ha realizado (ver ejemplo).

El archivo README.md debajo del nivel:

`analisis-numerico-computo-cientifico/proyecto_final/proyectos/`

es un archivo de control para la lista de proyectos y **únicamente lo actualiza/modifica el prof.** con comentarios para sus avances, títulos y objetivos de su proyectos y ligas hacia sus avances, trabajo escrito, presentación e implementación de su proyecto.

*Las ligas hacia el trabajo escrito y presentación son hacia otro lado (p.ej. una liga de dropbox en donde tienen pdfs o lo que utilicen para realizar esto) y no hacia directorios dentro del repositorio de la materia. Así evitamos tener archivos grandes en este repo :) y la liga hacia la implementación **sí** es al repo.

* **Ojo**: deben entregarse los 4 rubros: implementación, trabajo escrito, presentación y avances para que se considere válido el proyecto final. Si alguno de estos rubros no es entregado en tiempo y forma se tendrá 0 en el proyecto final.

* **Ojo**: Si un equipo no presenta avance alguno en las fechas de los sábados de abril y mayo que se les pide asistan, tendrán 0 en el rubro de avances y por tanto 0 en el proyecto final.


### El proyecto final se presenta en la segunda semana de finales.

# Objetivo

Que l@s estudiantes refuercen la teoría vista en el curso con la investigación e implementación de un método numérico en su forma en paralelo para resolver un problema  relacionado con la **optimización numérica** y en aplicaciones de áreas como análisis numérico y cómputo científico, inteligencia artificial, *machine learning*, estadística, bioestadística, física, economía, actuaría, ingeniería, finanzas o big data.

# Descripción

## Generalidades

Cada equipo realiza una investigación del método numérico elegido para su estudio, reporte en un trabajo escrito, presentación e implementación para resolver el problema definido por el equipo en el marco del objetivo anterior. La definición del problema se discute entre los integrantes del equipo y con el profesor. Juntos determinan el tiempo que requieren para la entrega del proyecto, para ello, semanalmente se solicitan avances del proyecto, siendo parte fundamental para el éxito del mismo. Más indicaciones respecto a esto último se encuentran en [indicaciones](indicaciones).

## Implementación

La implementación de los métodos numéricos es fundamental para el proyecto. Esta implementación utiliza código escrito en R, Python, C o algún otro lenguaje para resolver los objetivos de cada equipo. El código debe crearse dentro de un repositorio en `github`, utilizar `docker`, `AWS` y cómputo en paralelo.

Tiene un porcentaje de 40% y la calificación es por equipo. Se entrega el código de la implementación en una liga a ella, más información sobre esta liga en [indicaciones](indicaciones).

## Trabajo escrito

El trabajo escrito consiste en el reporte de la investigación realizada y los resultados obtenidos. Se dan referencias utilizadas. No se sube al repo del curso, pero se proporciona una liga al mismo, más información sobre esta liga en [indicaciones](indicaciones).

Tiene un porcentaje de 20% y la calificación es por equipo. Se entrega **una semana antes** de la fecha del examen final en un 95% completo.


## Presentación

Se realiza una presentación de máximo 20 min por cada equipo para reporte sobre el trabajo realizado y resultados. En esta presentación no se entra en detalles sobre los métodos, sólo cuestiones generales. No se sube al repo del curso, pero se proporciona una liga al mismo, más información sobre esta liga en [indicaciones](indicaciones).


Tiene dos calificaciones 10% de forma individual y 5% para el equipo. Se realiza en la fecha del examen final determinada por control escolar.

## Avances

Tienen un porcentaje de 25% y encuentran más información en [indicaciones](indicaciones).

# Calificación

La calificación se conforma de los porcentajes anteriores: 

* avances de forma individual (25%).

* trabajo escrito por equipo (20%).

* presentación individual (10%) y por equipo (5%).

* implementación del método numérico por equipo (40%).

El porcentaje del proyecto de acuerdo a la primera clase del curso tiene un porcentaje del `40%` de la **calificación final**.

**Ojo:** deben entregarse los 4 rubros: implementación, trabajo escrito, presentación y avances para que se considere válido el proyecto final. Si alguno de estos rubros no es entregado en tiempo y forma se tendrá 0 en el proyecto final.

# Lista ejemplo de métodos numéricos para proyectos:

La siguiente lista no pretende ser exhaustiva.

* Multiplicación de matrices.

* Multiplicación de tensores.

* Reglas de integración.

* Métodos para resolver sistemas de ecuaciones lineales: triangulares, sparse, densos.

* Factorización de matrices: lu, cholesky, qr, svd.

* Cálculo de eigenvalores, eigenvectores.

* Generación de números aleatorios.

* Ordenamiento de elementos en un arreglo.

* Mínimos cuadrados.

* Componentes principales.

* Sistemas de ecuaciones diferenciales.

* Algoritmos basados en árboles o grafos.

* Métodos numéricos para optimización: métodos de descenso, métodos Quasi-Newton, métodos de aproximación de rango reducido o rango bajo.

 **Los métodos numéricos deben ser utilizados en problemas de [optimización numérica](https://github.com/ITAM-DS/analisis-numerico-computo-cientifico/blob/master/temas/IV.optimizacion_convexa_y_machine_learning/4.1.Optimizacion_numerica_y_machine_learning.ipynb) y en aplicaciones detalladas al inicio.**
