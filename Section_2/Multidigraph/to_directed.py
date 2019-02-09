G = nx.Graph() # or MultiGraph, etc
G.add_edge(0, 1)
H = G.to_directed()
list(H.edges)
[(0, 1), (1, 0)]
#If already directed, return a (deep) copy
G = nx.DiGraph() # or MultiDiGraph, etc
G.add_edge(0, 1)
H = G.to_directed()
list(H.edges)
[(0, 1)]
