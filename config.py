config = {
    # 1 = Cruce de un punto, 2 = Cruce de dos puntos, 3 = Cruce uniforme, 4 = Cruce anular
    'breeding': 1,

    # 1 = Gen, 2 = MultiGen
    'mutation_geneticity': 1,

    # 1 = Uniforme, 2 = No Uniforme
    'mutation_uniformity': 1,

    #  1 = Elite, 2 = Ruleta, 3 = Universal, 4 = Boltzmann, 5 = Torneos1, 6 = Torneos2, 7 = Ranking
    'selection': 1,

    # 1 = Metodo1, 2 = Metodo2, 3 = Metodo3
    'replacement_method': 1,

    # 1 = Maxima cantidad de generaciones, 2 = Estructura,  3 = Contenido, 4 = Entorno a un  optimo
    'finish_criteria': 1
}

def configuration():
    return config