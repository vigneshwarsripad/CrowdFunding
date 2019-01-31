class ThinGraph(nx.Graph):
... all_edge_dict = {'weight': 1}
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
