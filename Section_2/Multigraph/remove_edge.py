G = nx.MultiGraph()
nx.add_path(G, [0, 1, 2, 3])
G.remove_edge(0, 1)
e = (1, 2)
G.remove_edge(*e) # unpacks e from an edge tuple
#For multiple edges
G = nx.MultiGraph() # or MultiDiGraph, etc
G.add_edges_from([(1, 2), (1, 2), (1, 2)]) # key_list returned
[0, 1, 2]
G.remove_edge(1, 2) # remove a single (arbitrary) edge
#For edges with keys
G = nx.MultiGraph() # or MultiDiGraph, etc
G.add_edge(1, 2, key='first')
'first'
G.add_edge(1, 2, key='second')
'second'
G.remove_edge(1, 2, key='second')
