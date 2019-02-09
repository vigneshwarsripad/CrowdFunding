G = nx.MultiGraph() # or MultiDiGraph
nx.add_path(G, [0, 1, 2])
key = G.add_edge(2, 3, weight=5)
[e for e in G.edges()]
[(0, 1), (1, 2), (2, 3)]
G.edges.data() # default data is {} (empty dict)
MultiEdgeDataView([(0, 1, {}), (1, 2, {}), (2, 3, {'weight': 5})])
G.edges.data('weight', default=1)
MultiEdgeDataView([(0, 1, 1), (1, 2, 1), (2, 3, 5)])
G.edges(keys=True) # default keys are integers


MultiEdgeView([(0, 1, 0), (1, 2, 0), (2, 3, 0)])
G.edges.data(keys=True)
MultiEdgeDataView([(0, 1, 0, {}), (1, 2, 0, {}), (2, 3, 0, {'weight': 5})])
G.edges.data('weight', default=1, keys=True)
MultiEdgeDataView([(0, 1, 0, 1), (1, 2, 0, 1), (2, 3, 0, 5)])
G.edges([0, 3])
MultiEdgeDataView([(0, 1), (3, 2)])
G.edges(0)
MultiEdgeDataView([(0, 1)])
