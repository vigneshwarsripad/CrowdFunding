G.edge_subgraph(edges).copy()
#Examples
G = nx.path_graph(5)
H = G.edge_subgraph([(0, 1), (3, 4)])
list(H.nodes)
[0, 1, 3, 4]
list(H.edges)
[(0, 1), (3, 4)]
