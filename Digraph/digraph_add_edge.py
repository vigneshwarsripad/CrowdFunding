G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
e = (1, 2)
G.add_edge(1, 2) # explicit two-node form
G.add_edge(*e) # single edge as tuple of two nodes
G.add_edges_from( [(1, 2)] ) # add edges from iterable container
#Associate data to edges using keywords:
G.add_edge(1, 2, weight=3)
G.add_edge(1, 3, weight=7, capacity=15, length=342.7)
#For non-string attribute keys, use subscript notation.
G.add_edge(1, 2)
G[1][2].update({0: 5})
G.edges[1, 2].update({0: 5})