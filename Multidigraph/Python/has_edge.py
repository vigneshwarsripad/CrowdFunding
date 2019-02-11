#Can be called either using two nodes u, v, an edge tuple (u, v), or an edge tuple (u, v, key).
G = nx.MultiGraph() # or MultiDiGraph
nx.add_path(G, [0, 1, 2, 3])
G.has_edge(0, 1) # using two nodes
True
e = (0, 1)
G.has_edge(*e) # e is a 2-tuple (u, v)
True
G.add_edge(0, 1, key='a')


'a'
G.has_edge(0, 1, key='a') # specify key
True
e=(0, 1, 'a')
G.has_edge(*e) # e is a 3-tuple (u, v, 'a')
True
#The following syntax are equivalent:
G.has_edge(0, 1)
True
1 in G[0] # though this gives :exc:`KeyError` if 0 not in G
True
