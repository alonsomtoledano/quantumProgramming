import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


#Create 6 nodes graph
graph = nx.Graph()
graph.add_nodes_from(["1","2","3","4","5","6"])
graph.add_edge("1","2")
graph.add_edge("1","3")
graph.add_edge("2","3")
graph.add_edge("2","4")
graph.add_edge("3","4")
graph.add_edge("3","5")
graph.add_edge("4","5")
graph.add_edge("2","6")
graph.add_edge("4","6")

nx.draw(graph, with_labels = True) # draw graph
plt.savefig('./annealing/annealingCircuit_2_graph.png') # save graph png

sampler = EmbeddingComposite(DWaveSampler()) # sampler definition
print(dnx.min_vertex_cover(graph, sampler)) # minimum vertex cover result using the created sampler