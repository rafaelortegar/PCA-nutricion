# Tercer avance del proyecto de Métodos Numéricos y Optimización

**Profesor:** Erick Palacios Moreno

**Lenguaje a utilizar:** Python

# Equipo y Roles designados:
| # | Alumno                            | Clave única | Roles Iniciales     |
|---|-----------------------------------|-------------|---------------------|
| 1 | Rafael Ortega                     | 123972      | Project Manager     |
| 2 | Elizabeth Rodriguez               | 191430      | Revisión de Código  |
| 3 | Karla Alfaro Pizaña               | 137314      | Revisión de Código  |
| 4 | Elizabeth Viveros                 | CU      | Programadora |
| 5 | Mario Rodríguez                   | CU      |Programador    |
| 6 | Leonardo Marín                    | 175903      |Programador          |

# Asignación de tareas por persona y por rol

**Project Manager:**    
* Creación e implementación de Docker en el proyecto, responsable: Rafael Ortega.
 
    Se realizó el Dockerfile para poder utilizar Docker en el proyecto.

    Se organiza una reunión para verificar dónde estamos en este momento, y a dónde vamos
    en los siguientes pasos del proyecto.
    
    Implementación de una instancia en EC2 para realizar la paralelización del
    algoritmo.

**Equipo de Programación:**
 * Implementación de pruebas unitarias sobre SVD y PCA, responsabe: Elizabeth viveros
 Prueba unitaria sobre el algoritmo de SVD y PCA para verificar si está correcto. 
 
 * Notebook de muestra del algoritmo de PCA sobre los datos --> Elizabeth Viveros
 
 * Paralelización del algoritmo de PCA from SVD. --> Leonardo Marín.
 
 * Funciones para calcular PCA utilizando SVD en segunda versión directo con jacobi --> Leonardo Marín.
 
* Obtener eigenvalores de la matriz --> Elizabeth Viveros

* Perfilamiento de las funciones que ya tenemos y buscar forma de optimizarlas: --> Mario Rodríguez. --> subir notebook

* Obtener los componentes --> Elizabeth Viveros

* Hacer dinámica la obtención del número de componentes --> Elizabeth Viveros y Leonardo Marín

* Meter las componentes a la regresión --> Rafael Ortega

* Incorporar en el reporte la explicación del algoritmo de PCA implementado por la paquetería sklearn --> Elizabeth Viveros


* Perfilamiento --> Mario Rodríguez.

* Se modificó el EDA para que refleje variables representativas con el modelo --> Mario Rodríguez.

* Modificación de las funciones de limpieza para mejorarlas --> Mario Rodríguez.



**Equipo de Revisión:**
* Revisión del algoritmo de SVD y PCA --> Elizabeth Rodríguez

* calcular PCA utilizando SVD en segunda versión directo con jacobi --> Elizabeth Rodríguez

* Tabla con resumen de los 3 algoritmos para el reporte --> Elizabeth Rodríguez

* Validación de errores entre los 3 algoritmos, comparara diferencias. Eli rod y karla

* Reporte Final --> Karla Alfaro.
 - Introducción
 - Datos y contexto
 - EDA en el reporte --> Mario Rodríguez y Karla Alfaro
 - Problemas de multicolinealidad y dimensión alta
 - Teoría del análisis de componentes principales

* Revisión de los resultados obtenidos con el PCA de Eli Viveros: Mario Rodríguez

* Documentación de los algoritmos ingresados : Rafa



# Fechas

| # | Milestone/avance                                           | Fecha       | Entregable                          |
|---|------------------------------------------------------------|-------------|-------------------------------------|
| 1 | Avance 1:Selección de BD, lenguaje, tema, roles            | 25/Abril    | README.md en Avance_1               |
| 2 | Avance 2: EDA & Feature Engineering y código simple        | 16/Mayo     | Notebooks de EDA & FE               |
| 3 | Avance 3: Revisión y Perfilamiento y paralelización        | 21/Mayo     | Notebooks del funcionamiento        |
| 4 | Avance 4: Reporte final                                    | 22/Mayo     | PDF Reporte final & Notebooks       |
| 5 | Presentación del proyecto                                  | Examen Final| Notebook Reporte Final y explicación|



# Por realizar:
- [ ] Paralelización del algoritmo. (en proceso)
- [ ] Montarlo en una instancia de Amazon Web Services para intentar paralelizarlo.(en proceso)
- [x] Subir el documento de docker para su uso en las instancias y por el equipo.
- [x] Finalizar el reporte final para entregar.
- [ ] Realizar perfilamiento del algoritmo. (en proceso)
- [x] Revisar y hacer más pruebas a los algoritmos realizados.
- [x] Mejorar documentación.
