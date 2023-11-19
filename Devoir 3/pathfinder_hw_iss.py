import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    graph_d = {}
    nbr_lien = 0
    
    for k ,v in enumerate(graph):
        graph_d[k] = v
        nbr_lien += len(v)
    
    odd_node = 0
    odd_node_key = {}
    
    for key in graph_d:
        if len(graph_d[key]) % 2 != 0:
            odd_node += 1
            odd_node_key[key] = len(graph_d[key])

    if odd_node != 0 and odd_node != 2:
        return None        
    
    start = 0
    if(odd_node_key != {}):
        start = next(iter(odd_node_key))
    
    stack = [start]
    eulerian_path = []
    
    while stack:
        actual = stack[-1]
        if(len(graph_d[actual]) > 0):
            nxt = graph_d[actual].pop()
            graph_d[nxt].remove(actual)
            stack.append(nxt)
        else:
            eulerian_path.append(stack.pop())

    if len(eulerian_path) != nbr_lien/2 +1:
        return None

    return eulerian_path[::-1]


if __name__ == "__main__":
    test0 = [[1],[0, 2],[1, 3],[2, 4, 6],[3, 5, 7, 6],[4, 9],[3, 4],[4, 8],[7, 9],[5, 8]]
    
    print(eulerian_path_finder(test0))