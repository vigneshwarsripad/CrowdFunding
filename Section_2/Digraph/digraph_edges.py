G = nx.DiGraph() # or MultiDiGraph, etc
nx.add_path(G, [0, 1, 2])
G.add_edge(2, 3, weight=5)
[e for e in G.edges]
[(0, 1), (1, 2), (2, 3)]
G.edges.data() # default data is {} (empty dict)
OutEdgeDataView([(0, 1, {}), (1, 2, {}), (2, 3, {'weight': 5})])
G.edges.data('weight', default=1)
OutEdgeDataView([(0, 1, 1), (1, 2, 1), (2, 3, 5)])
G.edges([0, 2]) # only edges incident to these nodes

OutEdgeDataView([(0, 1), (2, 3)])
G.edges(0) # only edges incident to a single node (use G.adj[0]?)
OutEdgeDataView([(0, 1)])
