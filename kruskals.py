import math
import graphstructures as n
import customheap as h
    


number_of_nodes = 10
num_of_edges = 18
adjacy_list = {
    "A" : [n.node(1,"E","A"),n.node(4,"D","A"),n.node(5,"B","A")],
    "B" : [n.node(5,"A","B"),n.node(4,"C","B"),n.node(2,"D","B")],
    "C" : [n.node(4,"B","C"),n.node(2,"J","C"),n.node(1,"I","C"),n.node(4,"H","C")],
    "D" : [n.node(2,"B","D"),n.node(4,"A","D"),n.node(2,"E","D"),n.node(5,"F","D"),n.node(11,"G","D"),n.node(2,"H","D")],
    "E" : [n.node(1,"A","E"),n.node(1,"F","E"),n.node(2,"D","E")],
    "F" : [n.node(7,"G","F"),n.node(1,"E","F"),n.node(5,"D","F")],
    "G" : [n.node(11,"D","G"),n.node(1,"H","G"),n.node(4,"I","G"),n.node(7,"F","G")],
    "H" : [n.node(2,"D","H"),n.node(1,"G","H"),n.node(6,"I","H"),n.node(4,"C","H")],
    "I" : [n.node(4,"G","I"),n.node(6,"H","I"),n.node(1,"C","I"),n.node(0,"J","I")],
    "J" : [n.node(0,"I","J"),n.node(2,"C","J")],
}

def show():
    for i in reconstructed_path:
        print(f"{i.origin} to {i.to} = {i.weight}")

def create_visited():
    visited = {}
    for node in adjacy_list:
        visited[node] = False
    return visited



degree = degree = math.ceil(num_of_edges / number_of_nodes) 
heap = h.MinIndexedDHeap(degree)
reconstructed_path = []


def search_and_create_min_heap():
    time = 0
    visited = create_visited()
    for node in adjacy_list:
        visited[node] = True
        search_neighbourings(node,visited)
    reconstruct_path()    
        
def search_neighbourings(node,visited):
    for item in adjacy_list[node]:
        if(visited[item.to] == True):continue
        heap.insert(item)

def does_create_cycle(item,target_node):
    for i in reconstructed_path:
        if(item == i.to):
           if(i.origin == target_node):
               return True 
           return does_create_cycle(i.origin,target_node)


def reconstruct_path():
    counter = 0
    while(counter != number_of_nodes - 1):
       item = heap.remove()
       if(does_create_cycle(item.to,item.origin)):continue
       reconstructed_path.append(item)
       counter += 1
        
             
search_and_create_min_heap()
show()



        
