"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""

import math
import heapq
    
def prim_mst(N, roads):
    """ 
    INPUT : 
        - N, the number of crossroads
        - roads, list of tuple (u, v, s) giving a road between u and v with satisfaction s
    OUTPUT :
        - return the maximal satisfaction that can be achieved
        
        See homework statement for more details
    """
    tot_graph = 0
    tot_satis = 0

    graph = {}
    for i in range(N):
        graph[i] = []

    while roads:
        u,v,s = roads.pop()
        graph[u].append([v,s])
        graph[v].append([u,s])
        tot_graph += s

    visited = {}
    not_visited = [(0,0)]

    while not_visited:
        satis,node = heapq.heappop(not_visited)

        if node not in visited.keys():
            tot_satis += satis
            visited[node] = satis

            for node_adj,satis in graph[node]:
                if node_adj not in visited:
                    heapq.heappush(not_visited, (satis, node_adj))

    return tot_graph-tot_satis

    
if __name__ == "__main__":

    # Read Input for the first exercice
    
    with open('in1.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        roads = []
        for road in range(m):
        
            l = fd.readline().rstrip().split()
            roads.append(tuple([int(x) for x in l]))
            
    # Compute answer for the first exercice
     
    ans1 = prim_mst(n, roads)
     
    # Check results for the first exercice

    with open('out1.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans1:
            print("Exercice 1 : Correct")
        else:
            print("Exercice 1 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans1, expected_output)) 
        

