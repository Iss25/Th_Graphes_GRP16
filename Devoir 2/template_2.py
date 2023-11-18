"""
    Student template for the third homework of LINMA1691 "Théorie des graphes".

    Authors : Devillez Henri
"""


import math
import random

class Union_Find():
    """
    Disjoint sets data structure for Kruskal's or Karger's algorithm.
  
    It is useful to keep track of connected components (find(a) == find(b) iff they are connected).  
  
    """
    
    def __init__(this, N):
        """
        Corresponds to MakeSet for all the nodes
        INPUT :
            - N : the initial number of disjoints sets
        """
        this.N = N
        this.p = list(range(N))
        this.size = [1]*N
        
    def union(this, a, b):
        """
        INPUT :
            - a and b : two elements such that 0 <= a, b <= N-1
        OUTPUT:
            - return nothing
            
        After the operation, the two given sets are merged
        """
        a = this.find(a)
        b = this.find(b)
       
        if a == b:
            return
       
        # Swap variables if necessary
        if this.size[a] > this.size[b]:
            a,b = b,a
        
        this.size[b] += this.size[a]
        this.p[a] = b
        
    def find(this, a):
        """
        INPUT :
            - a : one element such that 0 <= a <= N-1
        OUTPUT:
            - return the root of the element a
        """
        if a != this.p[a]: this.p[a] = this.find(this.p[a])
        return this.p[a]
    

def min_cut(N, edges):
    """ 
    INPUT : 
        - N the number of nodes
        - edges, list of tuples (u, v) giving an edge between u and v

    OUTPUT :
        - return an estimation of the min cut of the graph
        
    This method has to return the correct answer with probability bigger than 0.999
    See project homework for more details
    """
    def karger(nodes, edges):
        """ 
        INPUT : 
            - N the number of nodes
            - edges, list of tuples (u, v) giving an edge between u and v

        OUTPUT :
            - return an estimation of the min cut of the graph
              
        See project homework for more details
        """
        
        this_min_cut = -1
        
        # TO COMPLETE

        t = Union_Find(nodes)
        verify=[False]*len(edges)

        while t.N > 2:
            random_int = random.randint(0, len(edges)-1)
            if verify[random_int] == False:
                verify[random_int] = True
                random_edge = edges[random_int]
    
                if t.find(random_edge[0])!=t.find(random_edge[1]):
                    t.union(random_edge[0],random_edge[1])
                    t.N-=1
        
        this_min_cut = 0
        i=0
        for a, b in edges:
            if t.find(a)!=t.find(b):
                this_min_cut+=1
                i+=1


        return this_min_cut 
   
    
    best_min_cut = -1
    
    # TO COMPLETE (apply karger several times)
    # Probability to return the true min cut should be at least 0.9999
    binomial = math.factorial(N)/(2*math.factorial(N-2))
    p=1/binomial
    k = math.ceil(math.log(0.0001,1-p))
    l=[0]*len(edges)
    for i in range(k):
        l[karger(N, edges)]+=1/k

    """
    best_min_cut = len(edges)
    for i in range(len(l)):
        if i<best_min_cut and l[i]>=p:
            best_min_cut = i
    return best_min_cut
    """
    for i in range(len(l)):
        #prend la coupe min de proba >= p
        if l[i] >= p:
            return i
        
    return -1 #pas de coupe minimale (devrait pas arriver)
   
if __name__ == "__main__":

    # Read Input for the second exercice
    
    with open('in2.txt', 'r') as fd:
        l = fd.readline()
        l = l.rstrip().split(' ')
        
        n, m = int(l[0]), int(l[1])
        
        edges = []
        for edge in range(m):
        
            l = fd.readline().rstrip().split()
            edges.append(tuple([int(x) for x in l]))
            
    # Compute answer for the second exercice
     
    ans = min_cut(n, edges)
     
    # Check results for the second exercice

    with open('out2.txt', 'r') as fd:
        l_output = fd.readline()
        expected_output = int(l_output)
        
        if expected_output == ans:
            print("Exercice 2 : Correct")
        else:
            print("Exercice 2 : Wrong answer")
            print("Your output : %d ; Correct answer : %d" % (ans, expected_output)) 
