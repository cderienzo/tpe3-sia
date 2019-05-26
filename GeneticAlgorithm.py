import numpy
import random
from Config import Config
from Loader import Loader
from items import *

class GeneticAlgorithm():

    # Create an initial seed population
    def seed(self):
        population = list()
        for individual in range(Config.population_size):
            population.append({'height': random.uniform(Config.min_height, Config.max_height), 'items': numpy.random.randint(0, item_count(), items_count())})
        return population

    def replacement(self, population):
        population_1 = Loader.replacement(1)(self, population)
        population_2 = Loader.replacement(2)(self, population)

        sample_1 = random.sample(population_1, Config.B)
        sample_2 = random.sample(population_2, 1 - Config.B)

        return numpy.append(sample_1, sample_2)

    def fitness(self, population):
    # Calculating the fitness value of each solution in the current population.   
        fitness_vector = list()
        for individual in population:
            arms = item_value(individual['items'][0], 0)
            boots = item_value(individual['items'][1], 1)
            helmets = item_value(individual['items'][2], 2)
            gloves = item_value(individual['items'][3], 3)
            vests = item_value(individual['items'][4], 4)
            strength = arms['strength'] + boots['strength'] + helmets['strength'] + gloves['strength'] + vests['strength']
            agility = arms['agility'] + boots['agility'] + helmets['agility'] + gloves['agility'] + vests['agility']
            skill = arms['skill'] + boots['skill'] + helmets['skill'] + gloves['skill'] + vests['skill']
            resistence = arms['resistence'] + boots['resistence'] + helmets['resistence'] + gloves['resistence'] + vests['resistence']
            life = arms['life'] + boots['life']+ helmets['life'] + gloves['life'] + vests['life']
            
            strength = 100 * numpy.tanh(0.01 * Loader.strength_multiplier * strength)
            agility = numpy.tanh(0.01 * Loader.agility_multiplier * agility)
            skill = 0.6 * numpy.tanh(0.01 * Loader.skill_multiplier * skill)
            resistence = numpy.tanh(0.01 * Loader.resistence_multiplier * resistence)
            life = 100 * numpy.tanh(0.01 * life)

            atm = 0.5 - pow((3 * individual['height'] - 5), 4) + pow((3 * individual['height'] - 5), 2) + individual['height']/2
            dem = 2 + pow((3 * individual['height'] - 5), 4)- pow((3 * individual['height'] - 5), 2) - individual['height']/2

            attack = (agility * skill) * strength * atm
            defense = (resistence * skill) * life * dem
            fitness = Loader.attack_multiplier * attack + Loader.defense_multiplier * defense
            fitness_vector.append(fitness)
        return fitness_vector

    def select_mating_pool(self, population, fitness):
        population_1 = Loader.select(1)(population, fitness)
        population_2 = Loader.select(2)(population, fitness)

        sample_1 = random.sample(population_1, Config.A)
        sample_2 = random.sample(population_2, 1 - Config.A)

        return numpy.append(sample_1, sample_2)

    def crossover(self, parents):
        return Loader.crossover()(parents)

    def mutation(self, offspring):
        # TODO revisar que cambia random
        if (Config.mutation_uniformity == 2):
            Config.mutation_prob = random.uniform(0, 1)
        return Loader.mutation()(offspring)

