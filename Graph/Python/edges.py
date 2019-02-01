G = nx.path_graph(3) # or MultiGraph, etc
G.add_edge(2, 3, weight=5)
[e for e in G.edges]
[(0, 1), (1, 2), (2, 3)]
G.edges.data() # default data is {} (empty dict)
EdgeDataView([(0, 1, {}), (1, 2, {}), (2, 3, {'weight': 5})])
G.edges.data('weight', default=1)
EdgeDataView([(0, 1, 1), (1, 2, 1), (2, 3, 5)])
G.edges([0, 3]) # only edges incident to these nodes
EdgeDataView([(0, 1), (3, 2)])
G.edges(0) # only edges incident to a single node (use G.adj[0]?)
EdgeDataView([(0, 1)])