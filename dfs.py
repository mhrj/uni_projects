import linked_list as li
import draft


# dfs with recursive functionality
number_of_nodes = 6
adjacy_matrices = [[0,1,1,0,0,0],
                   [1,0,1,1,0,0],
                   [1,1,0,1,0,1],
                   [0,1,1,0,1,0],
                   [0,0,0,1,0,1],
                   [0,0,1,0,1,0]]

def adjacency_to_linked(number_of_nodes,adjacency):
    l = li.GraphLinkedList()
    l.adjacency_to_linked_list(number_of_nodes,adjacency)
    return l.list
    
adjacency_list = adjacency_to_linked(number_of_nodes,adjacy_matrices)
visited = [False,False,False,False,False,False,False]
cycle_visited = [False for i in range(number_of_nodes)]
components = [0 for i in range(number_of_nodes)]
parent = [-1 for i in range(number_of_nodes)]
path = draft.stack()

def find_components(num_of_nodes):
    counter = 0
    parent[0] = -1
    for node in adjacency_list:
        if(visited[node.element] == False):
            counter += 1
            dfs(node , counter)
            print(f"{counter} : {components}")
            

def dfs(node , counter):
    visited[node.element] = True
    components[node.element] = counter
    n = node.next
    while(n != None):
        if(visited[n.element] == False):
            parent[n.element] = node.element 
            path.add([node.element,n.element])
            dfs(adjacency_list[n.element],counter)
            n = n.next
            if(n != None and cycle_visited[n.element] == True):
                n = n.next
        elif(parent[node.element] != n.element):
            path.add([node.element,n.element])
            cycle_visited[node.element] = True
        if(n != None):
            n = n.next
        
find_components(number_of_nodes)

