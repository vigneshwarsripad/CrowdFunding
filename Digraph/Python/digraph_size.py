G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
G.size()
3
G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_edge('a', 'b', weight=2)
G.add_edge('b', 'c', weight=4)
G.size()
2
G.size(weight='weight')
6.0
