G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
ebunch=[(1, 2), (2, 3)]
G.remove_edges_from(ebunch)
#Removing multiple copies of edges
G = nx.MultiGraph()
keys = G.add_edges_from([(1, 2), (1, 2), (1, 2)])
G.remove_edges_from([(1, 2), (1, 2)])
list(G.edges())
[(1, 2)]
G.remove_edges_from([(1, 2), (1, 2)]) # silently ignore extra copy
list(G.edges) # now empty graph
[]
