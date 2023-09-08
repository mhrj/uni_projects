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

    

def create_path(index,p,s):
    reconstructed_path = draft.stack()
    reconstructed_path.add(s)
    compare_node = s
    for i in range(index,len(p)):
        if (p[i][1] == compare_node[0]):
            reconstructed_path.add(p[i])
            compare_node = p[i]
        if(s[1] == compare_node[0]): break
    print(f"cycle on {s[1]} ==>")
    print(f"path : {reconstructed_path.give_stack()}")
        
        
def re_path(cycle_nodes,p):
    for node in cycle_nodes:
        for index,n in enumerate(p.give_stack()):
            if(node == n):
                create_path(index + 1,p.give_stack(),n)
                break
                
def find_cycles():
    p = draft.stack()
    cycle_nodes = []
    for target_node in adjacency_list.list:
        next_node = target_node.next
        while(next_node!= None):
            v = adjacency_list.list[next_node.element]
            if(target_node.d > v.d and target_node.f < v.f and target_node.p != v.element):
                cycle_nodes.append([target_node.element,next_node.element])
            p.add([target_node.element,next_node.element])
            next_node = next_node.next    

    if(cycle_nodes != []):
        re_path(cycle_nodes,p)
    else:
        print("there is no cycle!")


find_components(number_of_nodes)
find_cycles()


