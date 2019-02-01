G = nx.path_graph(3) # or DiGraph, MultiGraph, MultiDiGraph, etc
G.has_node(0)
True
#It is more readable and simpler to use
0 in G
True