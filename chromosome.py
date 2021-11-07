import random

class Chromosome:
    def __init__(self):
        self.genes = []
        self.qt_genes = 13
        self.fit = 0
        self.colors = ['red','blue','green','yellow']
 
    ''' Gera as cores inciais do cromossomo, de forma
    aleatória 
    '''
    def set_genes(self):
        for i in range(self.qt_genes):
            self.genes.append((random.choice(self.colors)))
    
    ''' Calcula a aptidão(fitness) do cromossomo
    '''
    def fitness(self, graph):
        fitness = 0
        for i in range(self.qt_genes):
            for j in graph[i]:
                if self.genes[i] != self.genes[j]:
                    fitness += 1
        self.fit= fitness

    ''' Retorna as cores do cromorssomo'''
    def get_genes(self):
        return self.genes
    
    def get_fitness(self):
        return self.fit


    def initial(self, graph):
        self.set_genes()
        self.fitness(graph)


