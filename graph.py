import networkx as nx
import matplotlib.pyplot as plt

class GraphColoring():
    def __init__(self,number,) -> None:

        self.grafico = nx.Graph()
        self.number = number
       
    def set_nodes(self,graph):
        self.grafico.add_nodes_from(graph.keys())

    def set_edges(self,graph):
        for i,j in graph.items():
            self.grafico.add_edges_from(([(i,t) for t in j]))

    def draw(self,chromosome):
        nx.draw(self.grafico,node_color=chromosome,with_labels=True)
        plt.savefig(f"{self.number}.png")
        plt.clf()
      
    


