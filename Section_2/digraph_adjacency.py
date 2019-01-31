G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
[(n, nbrdict) for n, nbrdict in G.adjacency()]
[(0, {1: {}}), (1, {0: {}, 2: {}}), (2, {1: {}, 3: {}}), (3, {2: {}})]
