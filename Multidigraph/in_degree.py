G = nx.MultiDiGraph()
nx.add_path(G, [0, 1, 2, 3])
G.in_degree(0) # node 0 with degree 0
0
list(G.in_degree([0, 1, 2]))
[(0, 0), (1, 1), (2, 1)]
