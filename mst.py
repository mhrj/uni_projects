import math
import customqueue
import graphstructures
import heap


# number_of_nodes = 8
# semi_matrix = [[-1,10,1,4,-1,-1,-1,-1],
#                [10,-1,3,-1,0,-1,-1,-1],
#                [1,3,-1,2,-1,8,-1,-1],
#                [4,-1,2,-1,-1,2,7,-1],
#                [-1,0,-1,-1,-1,1,-1,8],
#                [-1,-1,8,2,1,-1,6,9],
#                [-1,-1,-1,7,-1,6,-1,12],
#                [-1,-1,-1,-1,8,9,12,-1]]

# def create_visited():
#     visited = [False] * number_of_nodes
#     visited[0] = True
#     return visited
    

# def create_mst_dict():
#     mst = {}
#     for i in range(0,number_of_nodes):
#         mst[i] = []
#     return mst

# def re_create_path(origin,to,weight):
#     global node_counter
#     global path_cost
#     mst[origin].append(to)
#     node_counter += 1
#     path_cost += weight  
    
# path_cost = 0
# node_counter = 1
# visited = create_visited()
# p_q = customqueue.priorityQueue()
# mst = create_mst_dict()

# def lazy_prim():
#     p_q.add(graphstructures.node(0,0,0))
                            
#     while(len(p_q) != 0 and node_counter != number_of_nodes):
#         item = p_q.pop()
#         if(visited[item.to] == False):
#             re_create_path(item.origin,item.to,item.weight)
#         visited[item.to] = True
#         for index,weight in enumerate(semi_matrix[item.to]):
#             if(weight == -1):continue
#             if(visited[index] == True):continue
#             p_q.add(graphstructures.node(weight,index,item.to))
            
# lazy_prim()
# print(mst)
# print(f"with cost of : {path_cost}")


number_of_nodes = 7
semi_matrix = [[-1,9,0,5,-1,7,-1],
               [9,-1,-1,-2,3,-1,4],
               [0,-1,-1,-1,-1,6,-1],
               [5,-2,-1,-1,-1,2,3],
               [-1,3,-1,-1,-1,-1,6],
               [7,-1,6,2,-1,-1,1],
               [4,-1,-1,3,6,1,-1]]


def create_visited():
    visited = [False] * number_of_nodes
    visited[0] = True
    return visited
    

def create_mst_dict():
    mst = {}
    for i in range(0,number_of_nodes):
        mst[i] = []
    return mst

def re_create_path(origin,to,weight):
    global node_counter
    global path_cost
    mst[origin].append(to)
    node_counter += 1
    path_cost += weight  

def calculate_all_edges():
    edge = 0
    for row in semi_matrix:
        for node in row:
            if(node != -1):
                edge += 1
    return edge


path_cost = 0
node_counter = 1
visited = create_visited()
mst = create_mst_dict()
edges = calculate_all_edges()
degree = math.ceil(edges / number_of_nodes)
ipq = heap.MinIndexedDHeap(degree)


def eager_prim():
    ipq.insert(graphstructures.node(0,0,0))
    while(ipq.show_length() != 0 and node_counter != number_of_nodes):
        item = ipq.remove()
        if(visited[item.to] == False):
            re_create_path(item.origin,item.to,item.weight)
        visited[item.to] = True
        for index,weight in enumerate(semi_matrix[item.to]):
            if(weight == -1):continue
            if(visited[index] == True):continue
            prev_item = ipq.does_exist(graphstructures.node(weight,index))
            if(prev_item != -1):
                if(prev_item.weight > weight):
                    ipq.update(index,weight,item.to)
            else:
                ipq.insert(graphstructures.node(weight,index,item.to))
eager_prim()
print(mst)
print(f"with cost of : {path_cost}")