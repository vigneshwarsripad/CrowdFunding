G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
ebunch = [(1, 2), (2, 3)]
G.remove_edges_from(ebunch)
