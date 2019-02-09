G = nx.Graph()

##Nodes:
##Add one node at a time:
G.add_node(1)
##Adding a node from a list, dict, set or even the lines from a file or the nodes from another graph.
G.add_nodes_from([2, 3])
G.add_nodes_from(range(100, 110))
H = nx.path_graph(10)
G.add_nodes_from(H)
##Node represented by an object
G.add_node(H)
##Edges:

##Adding one edge,
G.add_edge(1, 2)
##adding a list of edges,
G.add_edges_from([(1, 2), (1, 3)])
##adding a collection of edges,
G.add_edges_from(H.edges)
##If some edges connect nodes not yet in the graph, the nodes are added automatically. There are no errors when adding nodes or edges that already exist.
##Attributes:
##Each graph, node, and edge can hold key/value attribute pairs in an associated attribute dictionary (the keys must be hashable). By default these are empty, but can be added or changed using add_edge, add_node or direct manipulation of the attribute dictionaries named graph, node and edge respectively.

G = nx.Graph(day="Friday")
G.graph
{'day': 'Friday'}
##Adding node attributes using add_node(), add_nodes_from() or G.nodes
G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')
G.nodes[1]
{'time': '5pm'}
G.nodes[1]['room'] = 714 # node must exist already to use G.nodes
del G.nodes[1]['room'] # remove attribute
list(G.nodes(data=True))
[(1, {'time': '5pm'}), (3, {'time': '2pm'})]
#Add edge attributes using add_edge(), add_edges_from(), subscript notation, or G.edges.
G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3, 4), (4, 5)], color='red')
G.add_edges_from([(1, 2, {'color': 'blue'}), (2, 3, {'weight': 8})])
G[1][2]['weight'] = 4.7
G.edges[1, 2]['weight'] = 4
##Warning: we protect the graph data structure by making G.edges a read-only dict-like structure. However, you can assign to attributes in e.g. G.edges[1, 2]. Thus, use 2 sets of brackets to add/change data attributes:
G.edges[1, 2]['weight'] = 4 #(For multigraphs: MG.edges[u, v, key][name] = value).
##Shortcuts:
##Many common graph features allow python syntax to speed reporting.
1 in G # check if node in graph
#True
[n for n in G if n < 3] # iterate through nodes
#[1, 2]
len(G) # number of nodes in graph
#5
#Often the best way to traverse all edges of a graph is via the neighbors. The neighbors are reported as an adjacency-dict G.adj or G.adjacency()
for n, nbrsdict in G.adjacency():
for nbr, eattr in nbrsdict.items():
if 'weight' in eattr:
# Do something useful with the edges
pass
But the edges() method is often more convenient:
for u, v, weight in G.edges.data('weight'):
if weight is not None:
# Do something useful with the edges
pass
#Reporting:
#Create a low memory graph class that effectively disallows edge attributes by using a single attribute dict for all edges. This reduces the memory used, but you lose edge attributes.
class ThinGraph(nx.Graph):
#... all_edge_dict = {'weight': 1}
... def single_edge_dict(self):
... return self.all_edge_dict
... edge_attr_dict_factory = single_edge_dict
G = ThinGraph()
G.add_edge(2, 1)
G[2][1]
{'weight': 1}
G.add_edge(2, 2)
G[2][1] is G[2][2]
True