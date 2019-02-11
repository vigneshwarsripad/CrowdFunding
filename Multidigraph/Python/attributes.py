G = nx.MultiDiGraph(day="Friday")
G.graph
{'day': 'Friday'}
#Add node attributes using add_node(), add_nodes_from() or G.nodes
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.nodes[1]

{'time': '5pm'}
G.nodes[1]['room'] = 714
del G.nodes[1]['room'] # remove attribute
list(G.nodes(data=True))
[(1, {'time': '5pm'}), (3, {'time': '2pm'})]
#Add edge attributes using add_edge(), add_edges_from(), subscript notation, or G.edges.
key = G.add_edge(1, 2, weight=4.7 )
keys = G.add_edges_from([(3, 4), (4, 5)], color='red')
keys = G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
G[1][2][0]['weight'] = 4.7
G.edges[1, 2, 0]['weight'] = 4
