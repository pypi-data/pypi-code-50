Ans='''"""

This algorithm is a recursive algorithm which follows the concept of backtracking and implemented using stack data structure. But, what is backtracking.

Backtracking:-

It means whenever a tree or a graph is moving forward and there are no nodes along the existing path, the tree moves backwards along the same path which it went forward in order to find new nodes to traverse. This process keeps on iterating until all the unvisited nodes are visited.

How stack is implemented in DFS:-

    Select a starting node, mark the starting node as visited and push it into the stack.
    Explore any one of adjacent nodes of the starting node which are unvisited.
    Mark the unvisited node as visited and push it into the stack.
    Repeat this process until all the nodes in the tree or graph are visited.
    Once all the nodes are visited, then pop all the elements in the stack until the stack becomes empty.

    import sys
    def ret_graph():
        return {
            'A': {'B':5.5, 'C':2, 'D':6},
            'B': {'A':5.5, 'E':3},
            'C': {'A':2, 'F':2.5},
            'D': {'A':6, 'F':1.5},
            'E': {'B':3, 'J':7},
            'F': {'C':2.5, 'D':1.5, 'K':1.5, 'G':3.5},
            'G': {'F':3.5, 'I':4},
            'H': {'J':2},
            'I': {'G':4, 'J':4},
            'J': {'H':2, 'I':4},
            'K': {'F':1.5}
        }
    start = 'A'                 
    dest = 'J'                  
    visited = []                
    stack = []                  
    graph = ret_graph()
    path = []
    stack.append(start)                  
    visited.append(start)                
    while stack:                         
        curr = stack.pop()            
        path.append(curr)
        for neigh in graph[curr]:        
            if neigh not in visited:       
                visited.append(neigh)       
                stack.append(neigh)         
                if neigh == dest :            
                    print("FOUND:", neigh)
                    print(path)
                    sys.exit(0)
    print("Not found")
    print(path)

"""
'''
