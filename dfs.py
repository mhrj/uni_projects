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
    return l
    
adjacency_list = adjacency_to_linked(number_of_nodes,adjacy_matrices)
visited = [False,False,False,False,False,False,False]
components = [0 for i in range(number_of_nodes)]

def find_components(num_of_nodes):
    counter = 0
    for node in adjacency_list.list:
        if(visited[node.element] == False):
            counter += 1
            dfs(-1,node , counter)
            print(f"{counter} : {components}")
            

def dfs(p,node , counter):
    visited[node.element] = True
    adjacency_list.time += 1
    node.d = adjacency_list.time
    node.p = p 
    components[node.element] = counter
    n = node.next
    while(n != None):
        if(visited[n.element] == False):
            dfs(node.element,adjacency_list.list[n.element],counter)
        n = n.next
    adjacency_list.time += 1
    node.f = adjacency_list.time

def find_cycles(starting_node):
    u = starting_node
    v = adjacency_list.list[starting_node.next.element]
    while(v != None):
        if(v.d > u.d and u.f > v.f and v.p != u.element):
            u = v
            v = adjacency_list.list[u.next.element]
        else:
            print("cycle") 


find_components(number_of_nodes)
print(adjacency_list)
find_cycles(adjacency_list.list[0])


