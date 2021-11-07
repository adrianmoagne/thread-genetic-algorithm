import random
from chromosome import Chromosome
from threading import Thread
import sys
class GeneticAlgorithm(Thread):
    def __init__(self,population_amount, crossover_tax, mutation_tax , max_generations, genes_amount, adjacency_table, thread_number):
        self.thread_number = thread_number
        sys.stdout.write(f"Starting Thread ({self.thread_number})\n")
        sys.stdout.flush()
        self.population_amount = population_amount
        self.crossover_tax = crossover_tax
        self.mutation_tax = mutation_tax
        self.max_generations = max_generations
        self.adjacency_table= adjacency_table
        self.genes_amount = genes_amount
        self.population = []
        self.answer_generation = 0
        Thread.__init__(self)
        
        
    '''Inicia a população de cromossomos'''
    def initial_population(self):
        for i in range(self.population_amount):
            self.population.append(Chromosome())
            self.population[i].initial(self.adjacency_table)

    '''Escolhe um index em que cromossomos com maior taxa fitness
    tem maior probabilidade de serem sorteados'''
    def roulette_wheel(self):
        roulette = 0
        for i in range(self.population_amount):
            roulette += self.population[i].get_fitness()
        
        sorting = random.uniform(0,roulette)
        acumulado = 0
        for i in range(self.population_amount):
            acumulado += self.population[i].get_fitness()
            if(sorting < acumulado):
                return i
        return -1
    
    '''Cruza dois cromossomos pais, gerando dois filhos.
    Cada filho recebe uma quantidade aleatória de genes do pai e da mãe.
    Somente uma parte da população realiza cruzamento, definido pela taxa de crossover'''
    def crossover(self):
        children =[]
        for i in range(int(self.population_amount * self.crossover_tax)):
            father = self.population[self.roulette_wheel()]
            mother = self.population[self.roulette_wheel()]
            point = random.randint(0,self.genes_amount)
            child1 = Chromosome()
            child1.genes = father.get_genes()[:point] + mother.get_genes()[point:]
            child1.fitness(self.adjacency_table)
            child2 = Chromosome()
            child2.genes = mother.get_genes()[point:] + father.get_genes()[:point]
            child2.fitness(self.adjacency_table)
            children.append(child1)
            children.append(child2)
        return children
    
    ''' Realiza a mutação nos filhos gerados, em que cada gene tem um probabilidade
    de acordo com a taxa de mutação escolhida'''
    def mutation(self,children):
        for aux in range(len(children)):
            for i in range(self.genes_amount):
                if(random.random() < self.mutation_tax):
                    children[aux].genes[i] = random.choice(children[aux].colors)
 
            children[aux].fitness(self.adjacency_table)
  
        return children

    
    '''Ordena a população em ordem decrescente pelo fitness. Os que tiverem
    os menores fitness são cortados da população, a fim de manter a quantidade fixa
    de indivíduos'''
    def selection(self):
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        self.population = self.population[:self.population_amount]

    '''Roda o algorítmo até que um cromossomo que resolva o problema 
    seja encontrado. Caso não haja algum, o programa roda até a 
    quantidade de gerações definida. No final retorna o cromossomo com maior
    valor fitness'''
    def run(self):
        
        self.initial_population()
        for i in range(self.max_generations):
            
            self.selection()
            
            children = self.crossover()
            
            children = self.mutation(children)
            for j in range(len(children)):
                self.population.append(children[j])
            
            self.selection()
            self.answer_generation = i + 1
            if self.population[0].get_fitness()==50:
                break

        self.get_best_chromosome()

    def get_best_chromosome(self):
       
        #print(f"Thread ({self.thread_number})")
        sys.stdout.write(f"Thread ({self.thread_number}): "+"Best Chromosome: "+str(self.population[0].get_genes())+"\n")
        sys.stdout.flush()
        sys.stdout.write(f"Thread ({self.thread_number}): "+"Best fitness Chromosome: "+str(self.population[0].get_fitness())+"\n")
        sys.stdout.flush()
        sys.stdout.write(f"Thread ({self.thread_number}): "+"Answer Genaration: " +str(self.answer_generation)+"\n")
        sys.stdout.flush()
        sys.stdout.write("\n")
        sys.stdout.flush()
