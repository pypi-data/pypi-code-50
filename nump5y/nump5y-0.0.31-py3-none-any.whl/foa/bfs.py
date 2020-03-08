Ans='''"""

BFS is one of the traversing algorithm used in graphs. This algorithm is implemented using a queue data structure. In this algorithm, the main focus is on the vertices of the graph. Select a starting node or vertex at first, mark the starting node or vertex as visited and store it in a queue. Then visit the vertices or nodes which are adjacent to the starting node, mark them as visited and store these vertices or nodes in a queue. Repeat this process until all the nodes or vertices are completely visited.

 

Advantages of BFS

    It can be useful in order to find whether the graph has connected components or not.
    It always finds or returns the shortest path if there is more than one path between two vertices.

 

Disadvantages of BFS

    The execution time of this algorithm is very slow because the time complexity of this algorithm is exponential.
    This algorithm is not useful when large graphs are used.

    graph = {'A': ['B', 'C', 'E'],
             'B': ['A','D', 'E'],
             'C': ['A', 'F', 'G'],
             'D': ['B'],
             'E': ['A', 'B','D'],
             'F': ['C'],
             'G': ['C']}
             
             
    def bfs(graph, initial):
        
        visited = []
        
        queue = [initial]
     
        while queue:
            
            node = queue.pop(0)
            if node not in visited:
                
                visited.append(node)
                neighbours = graph[node]
     
                
                for neighbour in neighbours:
                    queue.append(neighbour)
        return visited
     
    print(bfs(graph,'A'))

"""
'''
