key = G.add_edge(1, 2)
#a list of edges,
keys = G.add_edges_from([(1, 2), (1, 3)])
#or a collection of edges,
keys = G.add_edges_from(H.edges)
#If some edges connect nodes not yet in the graph, the nodes are added automatically. If an edge already exists, an additional edge is created and stored using a key to identify the edge. By default the key is the lowest unused integer.
keys = G.add_edges_from([(4,5,{'route':28}), (4,5,{'route':37})])
G[4]
AdjacencyView({3: {0: {}}, 5: {0: {}, 1: {'route': 28}, 2: {'route': 37}}})
