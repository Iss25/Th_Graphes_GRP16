import os
from pathfinder_hw_iss import eulerian_path_finder


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
    
    for file in sorted(doc):
        graph = load_graph("Devoir 3/test_bench_students/" + file)
        eulerian_path = eulerian_path_finder(graph)
        if eulerian_path is None:
            print("No eulerian path found for " + file)
        else:
            print("Eulerian path found for " + file)
            print(eulerian_path)