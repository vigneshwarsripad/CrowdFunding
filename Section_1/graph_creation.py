import networkx as nx
G = nx.Graph()

##addition of nodes/edges

G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9) 

import math

##edge attributes

G.add_edge('y', 'x', function=math.cos)
G.add_node(math.cos) 


##adding more than one edge at a time
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)
elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)
