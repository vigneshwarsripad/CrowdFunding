# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:07:26 2019

@author: vigne
"""
##networkx must be imported
import networkx as nx


##Undirected graph which ignores edges between nodes
G = nx.Graph()

##Directed Graph, with directed edges
G = nx.DiGraph()

##Graph with undirected edges between pairs of nodes
G = nx.MultiGraph()

##Directed version of Multigraph
G = nx.MultiDiGraph()