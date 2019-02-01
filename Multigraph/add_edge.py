G = nx.MultiGraph()
e = (1, 2)
ekey = G.add_edge(1, 2) # explicit two-node form
G.add_edge(*e) # single edge as tuple of two nodes
1
G.add_edges_from( [(1, 2)] ) # add edges from iterable container
[2]
#Associate data to edges using keywords:
ekey = G.add_edge(1, 2, weight=3)
ekey = G.add_edge(1, 2, key=0, weight=4) # update data for key=0
ekey = G.add_edge(1, 3, weight=7, capacity=15, length=342.7)

#For non-string attribute keys, use subscript notation.
ekey = G.add_edge(1, 2)
G[1][2][0].update({0: 5})
G.edges[1, 2, 0].update({0: 5})
