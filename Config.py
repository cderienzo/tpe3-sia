class Config:

    character = 'Defensor'

    character_num = 2

    population_size = 10

    num_parents_mating = 4

    num_generations = 5

    min_height = 1.3
    
    max_height = 2

    # 1 = Cruce de un punto, 2 = Cruce de dos puntos, 3 = Cruce uniforme, 4 = Cruce anular
    crossover = 1

    # 1 = Gen, 2 = MultiGen
    mutation_geneticity = 1

    # 1 = Uniforme, 2 = No Uniforme
    mutation_uniformity = 1

    mutation_prob = 0.6

    #  1 = Elite, 2 = Ruleta, 3 = Universal, 4 = Boltzmann, 5 = Torneos1, 6 = Torneos2, 7 = Ranking
    A = 0.5
    selection_method_1 = 1
    selection_method_2 = 2

    # 1 = Metodo1, 2 = Metodo2, 3 = Metodo3
    B = 0.5
    replacement_method_1 = 1
    replacement_method_2 = 2

    # 1 = Maxima cantidad de generaciones, 2 = Estructura,  3 = Contenido, 4 = Entorno a un  optimo
    finish_criteria = 1

    files = ['testdata/armas.tsv', 'testdata/botas.tsv', 'testdata/cascos.tsv', 'testdata/guantes.tsv', 'testdata/pecheras.tsv']