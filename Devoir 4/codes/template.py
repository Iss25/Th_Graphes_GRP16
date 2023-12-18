from collections import deque


class Edge:
    def __init__(self, u, v, capa, weight, residual=None):
        self.u = u
        self.v = v
        self.capa = capa  # capacity that there is left to the edge
        self.weight = weight  # weight of the edge
        self.residual = residual  # corresponding edge in the residual graph


def create_graph(capacities, costs, green_sources: dict, gas_centrals: dict, consumers: dict):

    # TODO

    N = len(capacities)
    s=N
    t=N+1
    graph=[[] for _ in range(N+2)]
    for x in green_sources:
        graph[s].append(Edge(s,x,green_sources[x],0))
    
    for x in gas_centrals:
        l=gas_centrals[x]
        previous = l[0]
        for i in range(1,len(l)):
            this = l[i]
            graph[s].append(Edge(s,x,this[0]-previous[0],(this[1]-previous[1])/(this[0]-previous[0])))
            previous=l[i]

    for x in consumers:
        graph[x].append(Edge(x,t,consumers[x],0))
    
    for i in range(N):
        for j in range(N):
            graph[i].append(Edge(i,j,capacities[i][j],costs[i][j]))
            

    return s, t, graph


def get_residual(graph):

    # TODO

    graph_residual = [[] for _ in range(len(graph))]
    for i in range(len(graph)):
        for edge in graph[i]:
            edge.residual = Edge(edge.v, edge.u, 0, -edge.weight, edge)
            graph_residual[i].append(edge)
            graph_residual[edge.v].append(edge.residual)

    return graph_residual


def min_cost_max_flow(s, t, graph_residual):

    # TODO

    def BellmanFord(parent):
        distance = [float("Inf")]*len(graph_residual)
        visited = [False] * len(graph_residual)
        distance[s] = 0

        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue :
            u = queue.popleft()
            for edge in graph_residual[u]:
                if (edge.capa > 0) and (edge.weight + distance[u] < distance[edge.v]) :
                    distance[edge.v] = edge.weight + distance[u]
                    parent[edge.v] = edge
                    parent_node[edge.v] = u

                    if (visited[edge.v]==False):
                        queue.append(edge.v)
                        visited[edge.v]=True

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]

    parent = [-1] * len(graph_residual)
    parent_node = [-1] * len(graph_residual)

    maximum_flow = 0
    minimum_cost = 0

    # Augment the flow while there is path from source to sink
    while BellmanFord(parent):
        print("OKbf")
        # Find minimum residual capacity of the edges along the
        # path filled by BFS. Or we can say find the maximum flow
        # through the path found.
        path_flow = float("Inf")
        this = t
        print(parent_node)
        while this != s:
            path_flow = min(path_flow, parent[this].capa)
            this = parent[this].u

        # Add path flow to overall flow
        maximum_flow += path_flow
        print("OKpf")
        print(maximum_flow)

        this = t
        while this != s:
            minimum_cost += path_flow*parent[this].weight
            this = parent[this].u
        print("OKmc")
        print(minimum_cost)
        

        # update residual capacities of the edges and reverse edges
        # along the path
        v = t
        while v != s:
            edge = parent[v]
            edge.capa -= path_flow
            edge.residual.capa += path_flow
            v = parent[v].u
        print("OKr")
    

    return maximum_flow, minimum_cost

    # Returns the maximum flow from s to t in the given graph
    def edmonds_karp(self, source, sink):
        # This array is filled by BFS and to store path
        parent = [-1] * self.row

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    def bfs(self, s, t, parent):
        """
        Returns true if there is a path from
        source 's' to sink 't' in residual graph.
        Also fills parent[] to store the path.
        """

        # Mark all the vertices as not visited
        visited = [False] * self.row

        # Create a queue for BFS
        queue = deque()

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS loop
        while queue:
            u = queue.popleft()

            # Get all adjacent vertices of the dequeued vertex u
            # If an adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if (visited[ind] == False) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return visited[t]
