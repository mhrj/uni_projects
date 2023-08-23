# this algorithm is better for dense graphs remove cost > update cost
# djikstra with dense graph

import math

# to priortize the node with less wieght to be next in the queue
class priorityQueue:
    def __init__(self):
        self.__list = []
        
    def __len__(self):
        return len(self.__list) 

    def add(self,weight):
        self.__list.append(weight)
        
    def update(self,weight):
        self.__list[0].weight = weight
        
    def does_exist(self,weight):
        for i in range(self.__list.__len__()):
            if(weight.to == self.__list[i].to):
                return i
            else:
                return -1
        return -1
    
    def pop(self):
        if self.__len__() > 0:
            min_val = node(weight=math.inf,to=math.inf)
            min_val_index = 0
            for i in range(self.__len__()):
                if(self.__list[i].weight < min_val.weight):
                    min_val_index = i
                    min_val = self.__list[i]
            del self.__list[min_val_index]
            return min_val


num_of_nodes = 6
# pseudo_matrix representing matrix
pseudo_matrix = [
    [0,5,1,0,0,0],
    [0,0,2,3,20,0],
    [0,3,0,0,12,0],
    [0,0,3,0,2,6],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0]
]
               
class node:
    def __init__(self,weight = None,to = None) -> None:
        self.weight = weight
        self.to = to

def create_node(to,weight):
    return node(to=to,weight=weight)

def create_graph_list():
    weight_graph_list = {}
    for vertice in range(num_of_nodes):
        weight_graph_list[vertice] = []
        for index,edge in enumerate(pseudo_matrix[vertice]):
            if edge != 0:
                weight_graph_list[vertice].append(create_node(index,edge)) 
    return weight_graph_list

def create_parent(weight_graph_list):
    parent = {}
    for i in weight_graph_list:
        parent[i] = -1
    return parent

def create_dist(weight_graph_list,starting_node):
   dist = [math.inf for i in weight_graph_list]
   dist[starting_node] = 0
   return dist

def create_visited(weight_graph_list):
   return [False for i in weight_graph_list]


starting_node = 0
end_node = 5
weight_graph_list = create_graph_list()
parent = create_parent(weight_graph_list)
dist = create_dist(weight_graph_list,starting_node)
visited = create_visited(weight_graph_list)
p_q = priorityQueue()


def find_path(s,parent):
    for i in weight_graph_list:
        path = []
        path.append(i)
        p = i
        while p != 0 and p != -1:
            a = parent[p]
            path.append(parent[p])
            p = parent[p]
        path.reverse()
        print(f"path from {s} to {i} is {path}")
        
        
        
def djkstra_with_Dheap():
    n = create_node(0,0)
    p_q.add(n)
    while len(p_q) > 0:
        n = p_q.pop()
        visited[n.to] = True
        if(dist[n.to] < n.weight) : continue
        for neighbour in weight_graph_list[n.to]:
            if visited[neighbour.to] == True : continue
            new_dist = dist[n.to] + neighbour.weight
            if  new_dist < dist[neighbour.to]:
                does_exist = p_q.does_exist(neighbour) 
                if(does_exist != -1):
                    dist[neighbour.to] = new_dist
                    p_q.update(new_dist)
                    parent[neighbour.to] = n.to
                else:
                    dist[neighbour.to] = new_dist
                    neighbour.weight = new_dist
                    p_q.add(neighbour)
                    parent[neighbour.to] = n.to
    find_path(starting_node,parent)
    print(dist)   
    
djkstra_with_Dheap()