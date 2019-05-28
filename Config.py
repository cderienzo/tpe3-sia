class Config:

    # Las opciones pueden ser 'Defensor', 'Guerrero', 'Arquero', o 'Asesino'
    character = 'Defensor'

    character_num = 2

    population_size = 100

    num_parents_mating = 70

    num_generations = 20

    min_height = 1.3
    
    max_height = 2

    # 1 = Cruce de un punto, 2 = Cruce de dos puntos, 3 = Cruce uniforme, 4 = Cruce anular
    crossover = 2

    uniform_crossover_p = 0.8

    # 1 = Gen, 2 = MultiGen
    mutation_geneticity = 2

    # 1 = Uniforme, 2 = No Uniforme
    mutation_uniformity = 2
    delta_mutation_prob = 0.0001
    mutation_prob = 0.01

    #  1 = Elite, 2 = Ruleta, 3 = Universal, 4 = Boltzmann, 5 = Torneos1, 6 = Torneos2, 7 = Ranking
    A = 1
    B = 1
    selection_method_1 = 4
    selection_method_2 = 2
    selection_method_3 = 4
    selection_method_4 = 2

    # Initial and final temperatures for boltzmann
    initial_temperature = 373
    final_temperature = 273

    # 1 = Exponential Multiplicative, 2 = Logarithmical Multiplicative, 3 = Linear Multiplicative, 4 = Linear Additive
    cooling_schedule = 4
    
    # For schedule 1: alpha between 0.8 and 0.9, for schedule 2: alpha > 1, for schedule 3: alpha > 0 
    cooling_alpha = 1.5
    
    # Rounds for tournament selection method
    tournament_rounds = 3

    # 1 = Metodo1, 2 = Metodo2, 3 = Metodo3
    replacement_method = 2

    # 1 = Maxima cantidad de generaciones, 2 = Estructura,  3 = Contenido, 4 = Entorno a un optimo
    finish_criteria = 4

    # Maximas generaciones consecutivas sin mejorar el fitness para el criterio de corte de contenido. 
    # TODO que valor deberia ir?
    max_consecutive_generations = 20

    # Para la condicion de corte de entorno a un optimo donde se llega a un fitness inferior a un delta.
    # TODO que valores deberian ir?
    optimal_fitness = 4
    delta = 0.001