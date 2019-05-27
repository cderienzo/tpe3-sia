class Config:

    character = 'Defensor'

    character_num = 2

    population_size = 100

    num_parents_mating = 70

    num_generations = 20

    min_height = 1.3
    
    max_height = 2

    # 1 = Cruce de un punto, 2 = Cruce de dos puntos, 3 = Cruce uniforme, 4 = Cruce anular
    crossover = 2

    uniform_crossover_p = 0.5

    # 1 = Gen, 2 = MultiGen
    mutation_geneticity = 2

    # 1 = Uniforme, 2 = No Uniforme
    mutation_uniformity = 2

    mutation_prob = 0.6

    #  1 = Elite, 2 = Ruleta, 3 = Universal, 4 = Boltzmann, 5 = Torneos1, 6 = Torneos2, 7 = Ranking
    A = 0.5
    B = 0.5
    selection_method_1 = 1
    selection_method_2 = 2
    selection_method_3 = 3
    selection_method_4 = 5

    # Rounds for tournament selection method
    tournament_rounds = 3

    # 1 = Metodo1, 2 = Metodo2, 3 = Metodo3
    replacement_method = 1

    # 1 = Maxima cantidad de generaciones, 2 = Estructura,  3 = Contenido, 4 = Entorno a un optimo
    finish_criteria = 4

    # Maximas generaciones consecutivas sin mejorar el fitness para el criterio de corte de contenido. 
    # TODO que valor deberia ir?
    max_consecutive_generations = 20

    # Para la condicion de corte de entorno a un optimo donde se llega a un fitness inferior a un delta.
    # TODO que valores deberian ir?
    optimal_fitness = 4
    delta = 0.001