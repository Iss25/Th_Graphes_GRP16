import os
from pathfinder_hw import * 
import time

"""
Loads the graph contained in file.
"""
def load_graph(file_name):
    graph = []
    with open(file_name,'r') as file:
        txt = file.read().split("\n")
        for line in txt[1:-1]:
            adj = []
            for node in line.split(","):
                adj.append(int(node))
            graph.append(adj)
        while(len(graph) != int(txt[0])):
            graph.append([])
    return graph

"""
Translate a graph from adjacency list to file representation.
"""
def from_adj_to_str(graph):
    output = str(len(graph))
    for line in graph:
        output += "\n"
        for adj in line:
            output += str(adj) + ","
        output = output[:-1]
    output += "\n"
    return output

"""
Writes a graph into file_name.
"""
def save_graph(file_name,graph):
    with open(file_name,'w') as file:
        file.write(from_adj_to_str(graph))

if __name__ == "__main__":
    doc = os.listdir("Devoir 3/test_bench_students")
    i = 0
    for file in sorted(doc):
        i += 1 
        strt = time.time()
        graph = load_graph("Devoir 3/test_bench_students/" + file)
        eulerian_path1 = eulerian_path_finder(graph)

        if eulerian_path1 is None:
            print(time.time() - strt)
            print("No eulerian path found for " + file)
        else:
            print(time.time() - strt)
            print("Eulerian path found for " + file)
            #print(eulerian_path1)
