G = nx.path_graph(3)
list(G.nodes)
[0, 1, 2]
list(G)
[0, 1, 2]
#To get the node data along with the nodes:
G.add_node(1, time='5pm')
G.nodes[0]['foo'] = 'bar'
list(G.nodes(data=True))
[(0, {'foo': 'bar'}), (1, {'time': '5pm'}), (2, {})]
list(G.nodes.data())
[(0, {'foo': 'bar'}), (1, {'time': '5pm'}), (2, {})]
list(G.nodes(data='foo'))
[(0, 'bar'), (1, None), (2, None)]
list(G.nodes.data('foo'))
[(0, 'bar'), (1, None), (2, None)]
list(G.nodes(data='time'))
[(0, None), (1, '5pm'), (2, None)]
list(G.nodes.data('time'))
[(0, None), (1, '5pm'), (2, None)]
list(G.nodes(data='time', default='Not Available'))
[(0, 'Not Available'), (1, '5pm'), (2, 'Not Available')]
list(G.nodes.data('time', default='Not Available'))
[(0, 'Not Available'), (1, '5pm'), (2, 'Not Available')]
#If some of your nodes have an attribute and the rest are assumed to have a default attribute value you can create a dictionary from node/attribute pairs using the default keyword argument to guarantee the value is never
#None:
G = nx.Graph()
G.add_node(0)
G.add_node(1, weight=2)


G.add_node(2, weight=3)
dict(G.nodes(data='weight', default=1))
{0: 1, 1: 2, 2: 3}