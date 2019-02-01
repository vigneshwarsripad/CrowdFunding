G = nx.path_graph(4)
G.number_of_edges()
3
#If you specify two nodes, this counts the total number of edges joining the two nodes:
G.number_of_edges(0, 1)
1
#For directed graphs, this method can count the total number of directed edges from u to v:
G = nx.DiGraph()
G.add_edge(0, 1)
G.add_edge(1, 0)
G.number_of_edges(0, 1)
1
