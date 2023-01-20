from Classes.graph import Graph
from pickle import load
import csv
import os

K = 7

# Get Graph File Names
# Change wd to Graphs folder
owd = os.getcwd()
os.chdir(f"GraphTheoryApproach/Generated_Graphs/K{K}_Graphs")
# Get pkl files for full graphs, sorted in numeric order.
#graphs = sorted(os.listdir(), key=lambda x: (x[:3], x[4:6:3]))
#print(graphs)
graphs_fullpath = [os.path.join(os.getcwd(), file) for file in sorted(os.listdir(), key= lambda x:x[:3])]
#print(graphs_fullpath)
# Move back to original wd
os.chdir(owd)

# Create CSV file
with open(f"GraphTheoryApproach/sequences_0{K}_20230119.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    
    # Loop through .pkl files
    for graph in graphs_fullpath:
        graph:Graph = load(open(graph, "rb"))
        print(f"Generating sequence for ({graph.n}, {graph.k})")
        sequence = graph.generate_sequence_down()
        writer.writerow([graph.n, graph.k, len(sequence), sequence])
        
    
    