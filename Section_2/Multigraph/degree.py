G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
nx.add_path(G, [0, 1, 2, 3])
G.degree(0) # node 0 with degree 1
1
list(G.degree([0, 1]))
[(0, 1), (1, 2)]