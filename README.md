# Trabajo Práctico Especial 3 - Algoritmos Genéticos - Grupo 9 #

#### IMPORTANTE ####

    1. En el caso de no tener python instalado, pueden seguir esta guía para descargar python 3.5:

    # Descargar e instalar python y pip installer
        > sudo apt-get install python2.7-dev python3.5-dev
        > cd ~
        > wget https://bootstrap.pypa.io/get-pip.py
        > sudo python get-pip.py

    Luego, para ejecutar archivos .py deberán hacerlo con el comando python3 para indicar la versión de python a utilizar como se muestra abajo

    2. En el caso de que el trabajo falle por el siguiente error:
    
    ImportError: No module named "nombre_del_modulo"

    # Instalar el modulo correspondiente antes de importarlo
        > pip3 install nombre_del_modulo

    Luego, la ejecución del programa funcionará

#### EJECUCIÓN ####

    Los archivos de fulldata no están subidos al repositorio debido a su peso.
    Sin embargo, para el correcto funcionamiento del trabajo, es necesario poner la carpeta fulldata en la carpeta del repositorio de manera que quede:

    sia-2019-1c-09
        TP1
        TP2
        TP3
            fulldata
            WITH GUI
            WITHOUT GUI
            README.md

    Existen dos posibilidades para ejecutar el proyecto. 
    - Si se desea que se muestre la interfaz gráfica y los gráficos que se mostraron en la presentación,
      se debe ingresar a la carpeta WITH GUI desde la terminal y ejecutar:
      >  python3 find_best_solution.py
    - Depende del sistema operativo, las librerías que se utilizaron para la interfaz o los gráficos pueden no andar.
      En ese caso, se debe ingresar a la carpeta WITHOUT GUI desde la terminal y ejecutar:
      > python3 find_best_solution.py

