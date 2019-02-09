1 in G # check if node in graph
True
[n for n in G if n < 3] # iterate through nodes
[1, 2]
len(G) # number of nodes in graph
5
#Often the best way to traverse all edges of a graph is via the neighbors. The neighbors are reported as an adjacency-dict G.adj or G.adjacency()
for n, nbrsdict in G.adjacency():
    for nbr, eattr in nbrsdict.items():
... if 'weight' in eattr:
... # Do something useful with the edges
... pass
#But the edges reporting object is often more convenient:
for u, v, weight in G.edges(data='weight'):
... if weight is not None:
... # Do something useful with the edges
... pass
