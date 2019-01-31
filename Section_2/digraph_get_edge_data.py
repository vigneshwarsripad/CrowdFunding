G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
G[0][1]
{}
#Warning: Assigning to G[u][v] is not permitted. But it is safe to assign attributes G[u][v]['foo']
G[0][1]['weight'] = 7
G[0][1]['weight']
7
G[1][0]['weight']
7
G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
G.get_edge_data(0, 1) # default edge data is {}
{}
e = (0, 1)
G.get_edge_data(*e) # tuple form
{}
G.get_edge_data('a', 'b', default=0) # edge not in graph, return 0
0
