G = nx.MultiDiGraph()
nx.add_path(G, [0, 1, 2, 3])
G.out_degree(0) # node 0 with degree 1
1
list(G.out_degree([0, 1, 2]))
[(0, 1), (1, 1), (2, 1)]
