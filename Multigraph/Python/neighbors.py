G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
[n for n in G.neighbors(0)]
[1]
#Notes
#It is usually more convenient (and faster) to access the adjacency dictionary as G[n]:
G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_edge('a', 'b', weight=7)
G['a']
AtlasView({'b': {'weight': 7}})
G = nx.path_graph(4)
[n for n in G[0]]
[1]
