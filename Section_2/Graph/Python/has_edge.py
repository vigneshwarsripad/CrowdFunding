G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
G.has_edge(0, 1) # using two nodes
True
e = (0, 1)
G.has_edge(*e) # e is a 2-tuple (u, v)
True
e = (0, 1, {'weight':7})
G.has_edge(*e[:2]) # e is a 3-tuple (u, v, data_dictionary)
True
#The following syntax are equivalent:
G.has_edge(0, 1)
True
1 in G[0] # though this gives KeyError if 0 not in G
True
