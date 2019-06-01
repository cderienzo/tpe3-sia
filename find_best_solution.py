import numpy
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config
from State import State
import matplotlib.pyplot as plt

def finished():
    finish = False
    if (Config.kicking):
        return kicking_finished()
    if (Config.max_generations):
        finish = finish or max_generations_finished()
    if not finish and (Config.structure):
        finish = finish or structure_finished()
    if not finish and (Config.content):
        finish = finish or content_finished()
    if not finish and (Config.near_optimal):
        finish = finish or near_optimal_finished()
    return finish        

def max_generations_finished():
    return State.generation >= Config.num_generations

def structure_finished():
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    if(len(changed) == 0):
        return True
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    fitness_changed = GA.fitness(changed)
    best_match_idx_changed = numpy.where(fitness_changed == numpy.max(fitness_changed))
    index_changed = best_match_idx_changed[0][0]
    if ((fitness_changed[index_changed] - fitness[index]) < Config.delta_variation_fitness):
        return False    

    return True

def content_finished():
    if State.generation == 0:
        return False
    if (fitness[index] > State.best_fitness_current):
        State.best_fitness_current = fitness[index]
        State.consecutive_generations = 0
        return False
    else:
        State.consecutive_generations += 1
        return State.consecutive_generations >= Config.max_consecutive_generations     

def near_optimal_finished():
    if State.generation == 0:
        return False
    return (Config.optimal_fitness - fitness[index]) < Config.delta 

def kicking_finished():
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        return False
    
    distance = Config.optimal_fitness - fitness[index]
    if  distance > Config.delta:         
        Config.p_m += Config.p_m*0.8*numpy.tanh(distance)
        return False

    return True
def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Standard Deviation')
        plt.title('Standard Deviation Evolution')
        plt.show()
    line1.set_data(x_vec,y1_data)
    # adjust limits if new data goes beyond bounds
    if numpy.min(y1_data)<=line1.axes.get_ylim()[0] or numpy.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([numpy.min(y1_data)-numpy.std(y1_data),numpy.max(y1_data)+numpy.std(y1_data)])
    if numpy.max(x_vec) >= line1.axes.get_xlim()[1]:
        plt.xlim([numpy.min(x_vec)-numpy.std(x_vec),numpy.max(x_vec)+numpy.std(x_vec)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1

GA = GeneticAlgorithm()

population = GA.seed()

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')
std_line = []
y = 0
x = 0
std_x_vec = []
std_y_vec = []


while(not finished()):
    fitness = GA.fitness(population)
    best_match_idx = numpy.where(fitness == numpy.max(fitness))
    index = best_match_idx[0][0]
    std = numpy.std(fitness)
    print("gen: ", State.generation,"  fitness: ", fitness[index]," std: ",std,"  height: ", population[index]['height'],"  items: ", population[index]['items'])
    
    # For no plotting comment lines below
    std_y_vec = numpy.append(std_y_vec,std)
    std_x_vec = numpy.append(std_x_vec,x)
    x+=1
    std_line = live_plotter(std_x_vec,std_y_vec,std_line)

    population = GA.replacement(population, fitness)
    State.generation += 1

print("-------------------------------------------------------------------------")
print("Generation : ", State.generation)
print("-------------------------------------------------------------------------")
fitness = GA.fitness(population)
best_match_idx = numpy.where(fitness == numpy.max(fitness))
index = best_match_idx[0][0]
print("best solution : ", population[index])
print("best solution fitness : ", fitness[index])
print("-------------------------------------------------------------------------") 



