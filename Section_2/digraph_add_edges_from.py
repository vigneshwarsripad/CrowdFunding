G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_edges_from([(0, 1), (1, 2)]) # using a list of edge tuples
e = zip(range(0, 3), range(1, 4))
G.add_edges_from(e) # Add the path graph 0-1-2-3
#Associate data to edges
G.add_edges_from([(1, 2), (2, 3)], weight=3)
G.add_edges_from([(3, 4), (1, 4)], label='WN2898')
