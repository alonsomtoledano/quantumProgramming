import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as mpl

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite


graph = nx.star_graph(5) # create 5 node graph

sampler = EmbeddingComposite(DWaveSampler()) # sampler definition

minimumVertexCover = dnx.min_vertex_cover(graph, sampler) # minimum vertex cover result using the created sampler


print(minimumVertexCover) # print result

nx.draw(graph, with_labels = True) # draw graph
mpl.savefig('./annealing/annealingCircuit_1_graph.png') # save graph png