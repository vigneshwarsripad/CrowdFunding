G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
len(G)
4


G = nx.DiGraph() # or MultiDiGraph
nx.add_path(G, [0, 1, 2, 3])
G.degree(0) # node 0 with degree 1
1
list(G.degree([0, 1, 2]))
[(0, 1), (1, 2), (2, 2)]
