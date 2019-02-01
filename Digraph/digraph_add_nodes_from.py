G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_nodes_from('Hello')
K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G.add_nodes_from(K3)
sorted(G.nodes(), key=str)
[0, 1, 2, 'H', 'e', 'l', 'o']
#Use keywords to update specific node attributes for every node.
G.add_nodes_from([1, 2], size=10)
G.add_nodes_from([3, 4], weight=0.4)
#Use (node, attrdict) tuples to update attributes for specific nodes.
G.add_nodes_from([(1, dict(size=11)), (2, {'color':'blue'})])
G.nodes[1]['size']
11
H = nx.Graph()
H.add_nodes_from(G.nodes(data=True))
H.nodes[1]['size']
11
