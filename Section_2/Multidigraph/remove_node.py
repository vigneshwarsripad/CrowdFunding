G = nx.path_graph(3) # or DiGraph, MultiGraph, MultiDiGraph, etc
list(G.edges)
[(0, 1), (1, 2)]
G.remove_node(1)
list(G.edges)
[]
