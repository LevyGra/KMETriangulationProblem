from Classes.graph import Graph
from pickle import load

graph:Graph = load(open("GraphTheoryApproach/Generated_Graphs/002_002.pkl", "rb"))

graph.print_graph()

