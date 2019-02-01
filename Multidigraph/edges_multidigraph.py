G = nx.MultiDiGraph()
nx.add_path(G, [0, 1, 2])
key = G.add_edge(2, 3, weight=5)
[e for e in G.edges()]
[(0, 1), (1, 2), (2, 3)]
list(G.edges(data=True)) # default data is {} (empty dict)
[(0, 1, {}), (1, 2, {}), (2, 3, {'weight': 5})]
list(G.edges(data='weight', default=1))
[(0, 1, 1), (1, 2, 1), (2, 3, 5)]
list(G.edges(keys=True)) # default keys are integers
[(0, 1, 0), (1, 2, 0), (2, 3, 0)]
list(G.edges(data=True, keys=True))
[(0, 1, 0, {}), (1, 2, 0, {}), (2, 3, 0, {'weight': 5})]
list(G.edges(data='weight', default=1, keys=True))
[(0, 1, 0, 1), (1, 2, 0, 1), (2, 3, 0, 5)]
list(G.edges([0, 2]))
[(0, 1), (2, 3)]
list(G.edges(0))
[(0, 1)]
