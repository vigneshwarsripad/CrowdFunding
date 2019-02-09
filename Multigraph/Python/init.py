G = nx.Graph() # or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.Graph(name='my graph')
e = [(1, 2), (2, 3), (3, 4)] # list of edges
G = nx.Graph(e)
#Arbitrary graph attribute pairs (key=value) may be assigned
G = nx.Graph(e, day="Friday")
G.graph
{'day': 'Friday'}
