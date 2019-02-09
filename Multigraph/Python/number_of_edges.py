#For undirected multigraphs, this method counts the total number of edges in the graph:
G = nx.MultiGraph()
G.add_edges_from([(0, 1), (0, 1), (1, 2)])
[0, 1, 0]
G.number_of_edges()
3
#If you specify two nodes, this counts the total number of edges joining the two nodes:
G.number_of_edges(0, 1)
2
#For directed multigraphs, this method can count the total number of directed edges from u to v:

G = nx.MultiDiGraph()
G.add_edges_from([(0, 1), (0, 1), (1, 0)])
[0, 1, 0]
G.number_of_edges(0, 1)
2
G.number_of_edges(1, 0)
1