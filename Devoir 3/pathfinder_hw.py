import copy

def eulerian_path_finder(graph):
    """
    Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
    Si aucun chemin eulérien n'existe, la fonction retourne None.
    L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
    """
    
    nbr_lien = 0
    start = 0
    odd = set()
    graph_d = []
    
    for i in range(len(graph)):
        nbr_lien += len(graph[i])
        if len(graph[i])%2 != 0:
            odd.add(i)
        if len(graph[i]) != 0:
            graph_d.append(set(graph[i]))
    
    if len(odd) > 2:
        return None
    if len(odd) != 0:
        start = odd.pop()
        
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
        
    if len(eulerian_path) != nbr_lien/2 + 1:
        return None
    
    return eulerian_path[::-1]