G = nx.MultiGraph() # or MultiDiGraph
key = G.add_edge(0, 1, key='a', weight=7)
G[0][1]['a'] # key='a'
{'weight': 7}
G.edges[0, 1, 'a'] # key='a'
{'weight': 7}
#Warning: we protect the graph data structure by making G.edges and G[1][2] read-only dict-like structures. However, you can assign values to attributes in e.g. G.edges[1, 2, 'a'] or G[1][2]['a'] using an additional bracket as shown next. You need to specify all edge info to assign to the edge data associated with an edge.
G[0][1]['a']['weight'] = 10
G.edges[0, 1, 'a']['weight'] = 10
G[0][1]['a']['weight']
10
G.edges[1, 0, 'a']['weight']
10
G = nx.MultiGraph() # or MultiDiGraph
nx.add_path(G, [0, 1, 2, 3])
G.get_edge_data(0, 1)
{0: {}}
e = (0, 1)
G.get_edge_data(*e) # tuple form
{0: {}}
G.get_edge_data('a', 'b', default=0) # edge not in graph, return 0
0
