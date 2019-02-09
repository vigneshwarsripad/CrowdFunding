G = nx.path_graph(5)
G.update(nx.complete_graph(range(4,10)))
from itertools import combinations
edges = ((u, v, {'power': u * v})
... for u, v in combinations(range(10, 20), 2)
... if u * v < 225)
nodes = [1000] # for singleton, use a container
G.update(edges, nodes)
# dict-of-set/list/tuple
adj = {1: {2, 3}, 2: {1, 3}, 3: {1, 2}}
e = [(u, v) for u, nbrs in adj.items() for v in nbrs]
G.update(edges=e, nodes=adj)
DG = nx.DiGraph()
# dict-of-dict-of-attribute
adj = {1: {2: 1.3, 3: 0.7}, 2: {1: 1.4}, 3: {1: 0.7}}
e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
... for v, d in nbrs.items()]
DG.update(edges=e, nodes=adj)
# dict-of-dict-of-dict
adj = {1: {2: {'weight': 1.3}, 3: {'color': 0.7, 'weight':1.2}}}
e = [(u, v, {'weight': d}) for u, nbrs in adj.items()
... for v, d in nbrs.items()]
DG.update(edges=e, nodes=adj)
# predecessor adjacency (dict-of-set)
pred = {1: {2, 3}, 2: {3}, 3: {3}}
e = [(v, u) for u, nbrs in pred.items() for v in nbrs]
# MultiGraph dict-of-dict-of-dict-of-attribute
MDG = nx.MultiDiGraph()
adj = {1: {2: {0: {'weight': 1.3}, 1: {'weight': 1.2}}},
... 3: {2: {0: {'weight': 0.7}}}}
e = [(u, v, ekey, d) for u, nbrs in adj.items()
... for v, keydict in nbrs.items()
... for ekey, d in keydict.items()]
MDG.update(edges=e)
