from genetic import GeneticAlgorithm
from graph import GraphColoring

def main():
    adjacency_table =  {
                        0: [5, 12,7,11,10,9,1,4,2,3],
                        1 : [0,9],
                        2 : [0,3],
                        3 : [0,2,4],
                        4 : [0,3,5],
                        5 : [0,4,12],
                        6 : [12,7],
                        7 : [12,6,0,11,8],
                        8 : [7,11,9],
                        9 : [8,11,10,1,0],
                        10 : [9,11,0],
                        11 : [10,7,8,9,0],
                        12 : [5,6,7,0],
                    }
    lista =[]

    '''Gera 5 soluções para o problema de coloração de grafos(colorir cada vértice vizinho 
    com cores diferentes), retorna o fitness daquele cromossomo, 
    os genes(cores) contidos nele e a geração a qual ele pertence.
    Cada solução é iniciada em uma thread.
    '''                
    for i in range(5):
        lista.append(GeneticAlgorithm(450,0.6,0.02,100,13,adjacency_table,i))                    
        lista[i].start()

    '''Para cada solução gerada em uma das threads, é desenhado o grafo'''

    #Caso NÃo queira  gerar as imagens em um arquivo png, comente o código abaixo

    for thread in lista:
        graf = GraphColoring(thread.thread_number)
        graf.set_nodes(thread.adjacency_table)
        graf.set_edges(thread.adjacency_table)
        graf.draw(thread.population[0].get_genes())
     
if __name__ == '__main__':
	main()
