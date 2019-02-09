G = nx.path_graph(5)
H = G.copy()
H = G.copy(as_view=False)
H = nx.Graph(G)
H = G.__class__(G)
#Fresh Data – For fresh data, the graph structure is copied while new empty data attribute dicts are created. The resulting graph is independent of the original and it has no edge, node or graph attributes. Fresh copies are not enabled. Instead use:
H = G.__class__()
H.add_nodes_from(G)
H.add_edges_from(G.edges)
#View – Inspired by dict-views, graph-views act like read-only versions of the original graph, providing a copy of the original structure without requiring any memory for copying the information. See the Python copy module for more information on shallow and deep copies, https://docs.python.org/2/library/copy.html.
#Parameters as_view (bool, optional (default=False)) – If True, the returned graph-view provides a read-only view of the original graph without actually copying any data.
#Returns G – A copy of the graph.
#Return type Graph

G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
H = G.copy()
