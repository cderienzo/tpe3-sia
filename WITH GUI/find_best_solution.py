import numpy
import sys
from statistics import mean
from GeneticAlgorithm import GeneticAlgorithm
from Config import Config
from State import State
from gui.mainwindow import Ui_GeneticAlgorithm
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QImage, QPixmap
import matplotlib.pyplot as plt 

class MainWindow(QMainWindow, Ui_GeneticAlgorithm):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.pushButton.setEnabled(False)

        GA = GeneticAlgorithm()

        population = GA.seed()

        # use ggplot style for more sophisticated visuals 
        plt.style.use('ggplot') 
        
        changed_line = []
        changed_line_2 = [] 
        changed_line_3 = [] 
        changed_line_4 = [] 
        fit_line = [] 
        changed_x_vec = [] 
        changed_y_vec = []
        changed_x_vec_2 = [] 
        changed_y_vec_2 = [] 
        changed_x_vec_3 = [] 
        changed_y_vec_3 = [] 
        changed_x_vec_4 = [] 
        changed_y_vec_4 = [] 
        fit_line_x_vec = [] 
        fit_line_y_vec = [] 

        fitness = None
        index = None

        a = QPixmap('gui/1.png')
        b = QPixmap('gui/2.png')
        c = QPixmap('gui/3.png')
        d = QPixmap('gui/4.png')
        e = QPixmap('gui/5.png')
        f = QPixmap('gui/6.png')
        g = QPixmap('gui/7.png')
        h = QPixmap('gui/8.png')
        i = QPixmap('gui/9.png')
        j = QPixmap('gui/10.png')
        previmage = None
        image = a

        while(not finished(GA, population, fitness, index)):
            fitness = GA.fitness(population)
            best_match_idx = numpy.where(fitness == numpy.max(fitness))
            index = best_match_idx[0][0]

            if (Config.mutation_uniformity == 2):
                changed_y_vec_4 = numpy.append(changed_y_vec_4, Config.p_m) 
                changed_x_vec_4 = numpy.append(changed_x_vec_4,State.generation) 
                changed_line_4 = live_plotter(changed_x_vec_4,changed_y_vec_4,changed_line_4,"Generations","Mutation Probability","Mutation Probability per generation", resize=True) 
            
            if(Config.graph_fit==1): 
                fit_line_x_vec=numpy.append(fit_line_x_vec, State.generation) 
                fit_line_y_vec=numpy.append(fit_line_y_vec, fitness[index]) 
                fit_line = live_plotter(fit_line_x_vec,fit_line_y_vec,fit_line,"Generations","Max Fitness","Max Fitness per generation", resize=False) 
  
            if(Config.graph_std==1):
                changed_y_vec = numpy.append(changed_y_vec, min(fitness)) 
                changed_x_vec = numpy.append(changed_x_vec,State.generation) 
                changed_line = live_plotter(changed_x_vec,changed_y_vec,changed_line,"Generations","Min Fitness","Min Fitness per generation", resize=False) 

            changed_y_vec_2 = numpy.append(changed_y_vec_2, mean(fitness)) 
            changed_x_vec_2 = numpy.append(changed_x_vec_2,State.generation) 
            changed_line_2 = live_plotter(changed_x_vec_2,changed_y_vec_2,changed_line_2,"Generations","Avg Fitness","Avg Fitness per generation", resize=False) 

            if (Config.selection_method_1 == 4 or Config.selection_method_2 == 4 or Config.selection_method_3 == 4 or Config.selection_method_4 == 4):
                schedule_id = Config.cooling_schedule
                if schedule_id == 1:
                    temp_i = 1 + Config.initial_temperature / (1 + Config.cooling_alpha * pow(State.generation,2))
                elif schedule_id == 2:
                    temp_i = 1 + Config.initial_temperature / (1 + (Config.cooling_alpha*numpy.log(State.generation+1)))
                elif schedule_id == 3:
                    temp_i = 1 + Config.initial_temperature / ( 1 + Config.cooling_alpha*State.generation)
                elif schedule_id == 4:
                    temp_i = 1 + Config.final_temperature + (Config.initial_temperature - Config.final_temperature)*((Config.num_generations - State.generation)/Config.num_generations)
                else:
                    temp_i = Config.initial_temperature - State.generation * (Config.initial_temperature - Config.final_temperature)/Config.num_generations

                changed_y_vec_3 = numpy.append(changed_y_vec_3, temp_i) 
                changed_x_vec_3 = numpy.append(changed_x_vec_3,State.generation) 
                changed_line_3 = live_plotter(changed_x_vec_3,changed_y_vec_3,changed_line_3,"Generations","Boltzmann Temperature","Boltzmann Temperature per generation", resize=False) 

            plt.draw() 
            
            self.generation.setText(str(State.generation))
            self.generation.repaint()
            self.fitness.setText(str(fitness[index]))
            self.fitness.repaint()
            self.height.setText(str(population[index]['height']))
            self.height.repaint()
            self.items.setText(str(population[index]['items']))
            self.items.repaint()
            self.pm.setText(str(Config.p_m))
            self.pm.repaint()
            
            if (fitness[index] > Config.a and fitness[index] < Config.b):
                image = b
            elif (fitness[index] > Config.b and fitness[index] < Config.c):    
                image = c
            elif (fitness[index] > Config.c and fitness[index] < Config.d):
                image = d
            elif (fitness[index] > Config.d and fitness[index] < Config.e):
                image = e
            elif (fitness[index] > Config.e and fitness[index] < Config.f):
                image = f
            elif (fitness[index] > Config.f and fitness[index] < Config.g):
                image = g
            elif (fitness[index] > Config.g and fitness[index] < Config.h):
                image = h
            elif (fitness[index] > Config.h and fitness[index] < Config.i):
                image = i
            elif (fitness[index] > Config.i):
                image = j  
            if (image != previmage):
                previmage = image
                self.character.setPixmap(image)

            population = GA.replacement(population, fitness)
            State.generation += 1


        fitness = GA.fitness(population)
        best_match_idx = numpy.where(fitness == numpy.max(fitness))
        index = best_match_idx[0][0]
        self.generation.setText(str(State.generation))
        self.generation.repaint()
        self.fitness.setText(str(fitness[index]))
        self.fitness.repaint()
        self.end.setText("Finished!")
        self.end.repaint()


def finished(GA, population, fitness, index):
    finish = False
    if (Config.kicking):
        return kicking_finished(population, fitness, index)
    if (Config.max_generations):
        finish = finish or max_generations_finished()
    if not finish and (Config.structure):
        finish = finish or structure_finished(GA, population, fitness, index)
    if not finish and (Config.content):
        finish = finish or content_finished(fitness, index)
    if not finish and (Config.near_optimal):
        finish = finish or near_optimal_finished(fitness, index)
    return finish        

def max_generations_finished():
    return State.generation >= Config.num_generations

def structure_finished(GA, population, fitness, index):
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

def content_finished(fitness, index):
    if State.generation == 0:
        return False
    if (fitness[index] > State.best_fitness_current):
        State.best_fitness_current = fitness[index]
        State.consecutive_generations = 0
        return False
    else:
        State.consecutive_generations += 1
        return State.consecutive_generations >= Config.max_consecutive_generations     

def near_optimal_finished(fitness, index):
    if State.generation == 0:
        return False
    return (Config.optimal_fitness - fitness[index]) < Config.delta 

def kicking_finished(population, fitness, index):
    if State.last_population is None:
        State.last_population = population
        return False
    
    changed = [individual for individual in population if individual not in State.last_population]
    State.last_population = population
    if (len(changed) > Config.irrelevant_percentage * len(population)):
        if Config.kicking_flag == 1: 
            Config.kicking_flag = 0 
        return False
    
    distance = Config.optimal_fitness - fitness[index]
    if  distance > Config.delta:        
        if Config.kicking_flag == 0: 
            Config.kicking_flag = 1 
        else: 
            Config.kicking_flag = 0 
        return False

    return True

def live_plotter(x_vec,y1_data,line1,xlabel,ylabel,title,pause_time=0.1, resize=False): 
    if line1==[]: 
        # this is the call to matplotlib that allows dynamic plotting 
        plt.ion() 
        fig = plt.figure(frameon=False) 
        ax = fig.add_subplot(111) 
        # create a variable for the line so we can later update it 
        line1, = ax.plot(x_vec, y1_data, '-o', alpha=0.8)         
        #update plot label/title 
        plt.xlabel(xlabel) 
        plt.ylabel(ylabel) 
        plt.title(title) 
        plt.show() 
    line1.set_data(x_vec,y1_data) 

    if resize:
        plt.ylim([0, 1])
    else:
        plt.ylim([0, 55]) 

    # adjust limits if new data goes beyond bounds 
    if(numpy.max(x_vec) >= line1.axes.get_xlim()[1]): 
        plt.xlim([numpy.min(x_vec)-numpy.std(x_vec),numpy.max(x_vec)+numpy.std(x_vec)]) 
    
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above 
    plt.pause(pause_time) 
     
    # return line so we can update it again in the next iteration 
    return line1 


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()    