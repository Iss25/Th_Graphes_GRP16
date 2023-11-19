import copy

"""
Calcule un chemin eulérien dans graph et le retourne comme une liste de noeuds visités.
Si aucun chemin eulérien n'existe, la fonction retourne None.
L'argument graph ne doit pas être modifié lors de l'exécution de la fonction.
"""
def eulerian_path_finder(graph):
    odd_node = 0
    odd_node_key = []
    eulerian_path = []

    graph_d = {k: v for k, v in enumerate(graph)}
    #print(graph_d)
    
    for key in graph_d:
        if len(graph_d[key]) % 2 != 0:
            odd_node += 1
            odd_node_key.append(key)
    
    if odd_node != 0 and odd_node != 2:
        return None        
    
    return eulerian_path

if __name__ == "__main__":
    test0 = [[1],[0, 2],[1, 3],[2, 4, 6],[3, 5, 7, 6],[4, 9],[3, 4],[4, 8],[7, 9],[5, 8]]
    
    eulerian_path_finder(test0)