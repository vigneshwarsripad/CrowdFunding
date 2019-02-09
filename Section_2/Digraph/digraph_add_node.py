G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G.add_node(1)
G.add_node('Hello')
K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G.add_node(K3)
G.number_of_nodes()
3
#Use keywords set/change node attributes:
G.add_node(1, size=10)
G.add_node(3, weight=0.4, UTM=('13S', 382871, 3972649))
