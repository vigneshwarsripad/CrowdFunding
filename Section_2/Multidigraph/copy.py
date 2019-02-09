G = nx.path_graph(5)
H = G.copy()
H = G.copy(as_view=False)
H = nx.Graph(G)
H = G.__class__(G)
#Fresh Data – For fresh data, the graph structure is copied while new empty data attribute dicts are created. The
#resulting graph is independent of the original and it has no edge, node or graph attributes. Fresh copies are not
#enabled. Instead use:
H = G.__class__()
H.add_nodes_from(G)
H.add_edges_from(G.edges)

G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
H = G.copy()
