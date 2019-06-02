class Config:

    ###################
    #### PERSONAJE ####
    ###################

    # Las opciones pueden ser 'Defensor', 'Guerrero', 'Arquero', o 'Asesino'
    character = 'Defensor'

    character_num = 2

    min_height = 1.3
    
    max_height = 2

    ###################
    #### POBLACION ####
    ###################

    N = 150

    k = 130

    ###############
    #### CRUZA ####
    ###############

    # 1 = Cruce de un punto, 2 = Cruce de dos puntos, 3 = Cruce uniforme, 4 = Cruce anular
    crossover = 2

    p_c = 0.8

    ##################
    #### MUTACION ####
    ##################

    # 1 = Gen, 2 = MultiGen
    mutation_geneticity = 2

    # 1 = Uniforme, 2 = No Uniforme
    mutation_uniformity = 1

    initial_p_m = 0.1
    p_m = initial_p_m
    p_m_cooling_alpha = 0
    ###################
    #### SELECCION ####
    ###################
    
    #  1 = Elite, 2 = Ruleta, 3 = Universal, 4 = Boltzmann, 5 = Torneos Deterministica, 6 = Torneos Probabilistica, 7 = Ranking
    selection_method_1 = 1
    selection_method_2 = 4
    selection_method_3 = 1
    selection_method_4 = 6

    A = 0.6
    B = 0.45

    # Boltzmann: Temperaturas inicial y final
    initial_temperature = 100
    final_temperature = 23

    # 1 = Quadratic Multiplicative, 2 = Logarithmical Multiplicative, 3 = Linear Multiplicative, 4 = Linear Additive
    cooling_schedule = 1
    
    # For schedule 1: alpha > 0 , for schedule 2: alpha > 1, for schedule 3: alpha > 0 
    cooling_alpha = 0.97
    
    # Participants for tournament selection method
    tournament_participants = 3

    ###################
    #### REEMPLAZO ####
    ###################

    # 1 = Metodo 1, 2 = Metodo 2, 3 = Metodo 3
    replacement_method = 2

    ###########################
    #### CRITERIOS DE CORTE ###
    ###########################

    # Elegir True o False si se quiere que se corte por ese criterio o no
    max_generations = True
    structure = False
    content = False
    near_optimal = False
    kicking = False
    
    ###################################################
    #### CONFIGURACION PARA LOS CRITERIOS DE CORTE ####
    ###################################################

    # Maximas generaciones consecutivas sin mejorar el fitness para el criterio de corte de contenido 
    # TODO que valor deberia ir?
    max_consecutive_generations = 100

    # Maxima cantidad de generaciones
    num_generations = 100000

    # Entorno a un optimo
    optimal_fitness = 41.05775193
    delta = 1

    # Estructura
    irrelevant_percentage = 0.02
    delta_variation_fitness = 2