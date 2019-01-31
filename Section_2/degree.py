G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
G.degree[0] # node 0 has degree 1
1
list(G.degree([0, 1, 2]))
[(0, 1), (1, 2), (2, 2)]
