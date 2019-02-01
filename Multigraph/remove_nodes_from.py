G = nx.path_graph(3) # or DiGraph, MultiGraph, MultiDiGraph, etc
e = list(G.nodes)
e
[0, 1, 2]
G.remove_nodes_from(e)
list(G.nodes)
[]
