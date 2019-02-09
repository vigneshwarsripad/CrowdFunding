G = nx.path_graph(2) # or MultiGraph, etc
H = G.to_directed()
list(H.edges)
[(0, 1), (1, 0)]
G2 = H.to_undirected()
list(G2.edges)
[(0, 1)]
