# Create a subgraph SG based on a (possibly multigraph) G
SG = G.__class__()
SG.add_nodes_from((n, G.nodes[n]) for n in largest_wcc)
if SG.is_multigraph:
SG.add_edges_from((n, nbr, key, d)
for n, nbrs in G.adj.items() if n in largest_wcc
for nbr, keydict in nbrs.items() if nbr in largest_wcc
for key, d in keydict.items())
else:
SG.add_edges_from((n, nbr, d)
for n, nbrs in G.adj.items() if n in largest_wcc
for nbr, d in nbrs.items() if nbr in largest_wcc)
SG.graph.update(G.graph)
#Examples
G = nx.path_graph(4) # or DiGraph, MultiGraph, MultiDiGraph, etc
H = G.subgraph([0, 1, 2])
list(H.edges)
[(0, 1), (1, 2)]
