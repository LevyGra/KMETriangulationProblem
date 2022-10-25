from Classes.graph import Graph
from pickle import load

graph:Graph = load(open("GeneratedGraphs/graph_4_1.pkl", "rb"))

graph.print_graph()

