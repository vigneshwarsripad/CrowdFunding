1 in G # check if node in graph
True
[n for n in G if n<3] # iterate through nodes
[1, 2]
len(G) # number of nodes in graph
5
G[1] # adjacency dict-like view keyed by neighbor to edge attributes
AdjacencyView({2: {0: {'weight': 4}, 1: {'color': 'blue'}}})
#Often the best way to traverse all edges of a graph is via the neighbors. The neighbors are available as an adjacency-view G.adj object or via the method G.adjacency().
for n, nbrsdict in G.adjacency():
... for nbr, keydict in nbrsdict.items():
... for key, eattr in keydict.items():
... if 'weight' in eattr:
... # Do something useful with the edges
... pass
But the edges() method is often more convenient:
for u, v, keys, weight in G.edges(data='weight', keys=True):
... if weight is not None:
... # Do something useful with the edges
... pass