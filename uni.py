# import numpy as np
import math

# a = int(input())
# b = int(input())
# c = int(input())

# if(a + b > c or c + b > a or a + c > b):
#     print("N")
# else:
#     print("Y")



# radious = int(input())
# x_1 = int(input())
# y_1 = int(input())
# x_2 = int(input())
# y_2 = int(input())

# if((x_2 - x_1 > 2 and y_2 - y_1 > 2)):
#     print("N")
# else:
#     print("Y")
    
    
# s_of_hexagon = int(input())
# radious_of_circle = int(input())    
# aria_of_hexagon = 3 * 3 ** 0.5 * (s_of_hexagon ** 2) / 2
# aria_of_circle = 3.14159265359 * (radious_of_circle ** 2)

# print(aria_of_hexagon - aria_of_circle)

# is_offside = True
# num_of_def = int(input())
# a_x = int(input())
# a_y = int(input())
# for i in range(num_of_def):
#    d_x = int(input())
#    d_y = int(input())
#    if(d_y > a_y):
#        is_offside = False

# if(is_offside):
#     print("Y")
# else:
#     print("N")   
      

# a = int(input())
# b = int(input())
# c = int(input())

# y = -a * 0 / b - c / b
# x = -a * 0 / a - c / a

# coordinate_x = int(input())
# coordinate_y = int(input())

# fin = int(input())

# fin_x = (math.fabs(coordinate_x) + fin) * (1 if coordinate_x == 0 else ((math.fabs(coordinate_x)) / (coordinate_x)))
# fin_y = (math.fabs(coordinate_y) + fin) * (1 if coordinate_y == 0 else ((math.fabs(coordinate_y)) / (coordinate_y)))

# if(fin_x > x or fin_y > y || ):
#     print("Y")
# else:
#     print("N")




# is_whole = True
# sum = 0
# num_of_vertices = int(input())


# arr = []
# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
           
# while(True):
#     origin_v = int(input())
#     if(origin_v < 0): break
#     destination_vertice = int(input())
#     origin_vertice = arr[origin_v]
#     arr[destination_vertice][origin_v] = 1
#     origin_vertice[destination_vertice] = 1
    
# for i in range(num_of_vertices):
#     for j in range(num_of_vertices):
#         sum += arr[i][j]
#     if(sum == num_of_vertices - 1 and arr[i][i] == 0):
#         is_whole = True       
#     else:
#         is_whole = False 
#         break
#     sum = 0
        
        
# if(is_whole):
#     print("Y")
# else:
#     print("N")

# ras = input()
# size = int(input())
# sum = 0

# for i in range(size):
#     first = int(input())
#     second = int(input())
#     if(first == second):
#         sum += 1

# print(sum)






# num_of_vertices = int(input())

# num_of_edges = int(input())
    
# for i in range(num_of_edges):
#     edge_1 = int(input())
#     edge_2 = int(input())
    
# if((num_of_vertices - 1) * 2 == num_of_edges and num_of_vertices >= 4):
#         print("Y")
# else:
#     print("N")
  
  
  
  
  
  
  
  




# max_edge = 0
# sum = 0
# vertice_with_most_edges = 0
# num_of_vertices = int(input())
# num_of_edges = int(input())
# arr = []

# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
  

# for i in range(num_of_edges):
#     origin_vertice = int(input())
#     destination_vertice = int(input())
#     arr[origin_vertice][destination_vertice] = 1

# for i in range(num_of_vertices):
#     for j in range(num_of_vertices):
#         sum += arr[i][j]
#     if(sum > max_edge):
#         max_edge = sum
#         vertice_with_most_edges = arr.index(arr[i])
#     sum = 0


# print(vertice_with_most_edges)



# num_of_c = 0
# num_of_vertices = int(input())
# num_of_edges = int(input())
# arr = []

# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
        
# for i in range(num_of_edges):
#     origin_vertice = int(input())
#     destination_vertice = int(input())
#     arr[origin_vertice][destination_vertice] = 1
    
# for i in range(num_of_vertices):
#     for j in range(i,num_of_vertices):
#         if (arr[i][j] != 0 and arr[i][j] == arr[j][i]):
#             num_of_c += 1
        

# print(num_of_c)












# vertices = int(input())
# arr_of_center = []
# ecc = 0
# center = vertices

# for i in range(vertices):
#     for j in range(vertices):
#         row = int(input())
#         if(row > ecc):
#             ecc = row        
#     if(center > ecc ):
#        center = ecc
#        arr_of_center = []
#     if(center == ecc):
#         arr_of_center.append(i)    
#     ecc = 0

# for i in arr_of_center:
#     print(i)
    

    
    



        
        
          
        
        
# num_of_vertices = int(input())
# num_of_edges = int(input())
# arr = []

# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
        
# for i in range(num_of_edges):
#     origin_v = int(input())
#     destination_vertice = int(input())
#     origin_vertice = arr[origin_v]
#     arr[destination_vertice][origin_v] = 1
#     origin_vertice[destination_vertice] = 1
    
# for i in range(num_of_vertices):
#     for j in range(num_of_vertices):
#         if(arr[i][j] == 1):
#             arr[i][j] = 0
#         else:
#             arr[i][j] = 1
#     arr[i][i] = 0
    
    
# for i in range(num_of_vertices):
#     for j in range(num_of_vertices):
#         print(arr[i][j],end=" ")
#     print()
        
# num_of_vertices = int(input())
# num_of_edges = int(input())

# if(((num_of_vertices) * (num_of_vertices - 1)) / 2 == num_of_edges):
#     print("C")
# else:
#     print("NC")
    
        


# num_of_vertices = int(input())
# num_of_edges = int(input())
# edges_of_vertice = 0
# arr = []

# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
            

# for i in range(num_of_edges):
#     origin_v = int(input())
#     destination_vertice = int(input())
#     origin_vertice = arr[origin_v]
#     arr[destination_vertice][origin_v] = 1
#     origin_vertice[destination_vertice] = 1           

# sum_edges_of_vertice = sum(arr[0])


# for i in range(num_of_vertices):
#     if(sum(arr[i]) != sum_edges_of_vertice):
#         print("N")
#         break
# print("Y")
        
        
        
        
        
        
        
        
# num_of_vertices = int(input())
# sum = 0

# for i in range(num_of_vertices):
#     num_of_edges = int(input())
#     sum += num_of_edges

# print(sum // 2)








# num_of_vertices = int(input())
# num_of_edges = int(input())
# is_semi_graph = False
# edges_of_vertice = 0
# arr = []

# for i in range(num_of_vertices):
#     arr.append([]) # [[0]]
#     for j in range(num_of_vertices):
#         arr[i].append(0)
            

# for i in range(num_of_edges):
#     origin_v = int(input())
#     destination_vertice = int(input())
#     origin_vertice = arr[origin_v]
#     arr[destination_vertice][origin_v] += 1
#     origin_vertice[destination_vertice] += 1  
    
# for i in range(num_of_vertices):
#     for j in range(num_of_vertices):
#         if(arr[i][j] > 1):
#             is_semi_graph = True
#             break

# if(is_semi_graph):
#     print("Y")
# else:
#     print("N")



       






# bfs ======> 

# q = queue()
# color = ["w" for i in range(num_of_vertices)]
# distance = [0 for i in range(num_of_vertices)]
# p = [-1 for i in range(num_of_vertices)]
# distance_matrices = []



# for n in range(num_of_vertices):
#     q.add(n)
#     while q.give_length() - 1 >= 0:
#         u = q.pop()
#         if u != -1:
#             for i in range(len(dic[u])):
#                 j = dic[u][i]
#                 if color[j] == "w":
#                     color[j] = "g"
#                     distance[j] = distance[u] + 1
#                     p[j] = u
#                     q.add(j)
#             color[u] = "B"
#     print()
#     print(f"{n} + : + {color},{distance},{p}")
#     distance_matrices.append(distance)
#     color = ["w" for i in range(num_of_vertices)]
#     distance = [0 for i in range(num_of_vertices)]
#     p = [-1 for i in range(num_of_vertices)] 



# def get_greatest_distance(dist_matrices):
#     greatest_num = 0
#     for i in range(num_of_vertices):
#         for j in range(num_of_vertices):
#             if(greatest_num < dist_matrices[i][j]):
#                 greatest_num = dist_matrices[i][j]
#     return greatest_num

# print()
# print(get_greatest_distance(distance_matrices))


#==>

# q.add(0)

# while q.give_length() - 1 >= 0:
#     u = q.pop()
#     if u != -1:
#         for i in range(len(dic[u])):
#             j = dic[u][i]
#             if color[j] == "w":
#                 color[j] = "g"
#                 distance[j] = distance[u] + 1
#                 p[j] = u
#                 q.add(j)
#         color[u] = "B"
#     print(u)        

# num_of_vertices = int(input())
# q = queue()
# color = ["W" for i in range(num_of_vertices)]
# distance = [0 for i in range(num_of_vertices)]
# p = [-1 for i in range(num_of_vertices)]
# q.add(0)

# while q.give_length() >= 0:
#     item = q.pop()
#     if item != -1:
#         for i in range(num_of_vertices):
#             if(adjacy[item][i] == 1):
#                 if color[i] == "W":
#                     color[i] = "G"
#                     p[i] = item
#                     distance[i] = distance[item] + 1
#                     q.add(i)
#         color[item] = "B"
#         print(item)
# print()
# print(f"{color},{distance},{p}")


# while q.give_length() - 1 >= 0:
#     item = q.pop()
#     if item != -1:
#         for i in range(num_of_vertices ** 2):
#             vertex = i % num_of_vertices
#             drayer = int(input())
#             if(drayer == 1):
#                 if color[vertex] == "W":
#                     color[vertex] = "G"
#                     p[vertex] = item
#                     distance[vertex] = distance[item] + 1
#                     q.add(vertex)
#             if(vertex == 0):
#                 color[item] = "B"
#             if(vertex == num_of_vertices - 1):
#                 item = q.pop()
#         print(item)

# print(f"{color},{distance},{p}")
# print()
 


# def determin_path_to_destinationVertex(vertex):
#     while(p[vertex] != -1):
#         print(vertex)
#         vertex = p[vertex]
#     print(vertex)
         
# determin_path_to_destinationVertex(4) 


    



# def create_matrix(vertex_count):
#     return [0 for i in range(vertex_count)]

# vertex_count = int(input())
# matrix = create_matrix(vertex_count)   
        
# for i in range(vertex_count**)



class queue:
    
    def __init__(self):
        self.__list = []
        
    def __len__(self):
        return len(self.__list)

    def add(self,num):
        self.__list.append(num)
    
    def pop(self):
        if(len(self.__list)- 1 >= 0):
           item = self.__list[0]
           del self.__list[0]
           return item
        else:
            return -1
    
    def give_item(self,index):
       if(len(self.__list) > 0):
           item = list[index]
           return item
       else:
           return -1
   
    def give_queue(self):
        return self.__list
    
            
    def give_length(self):
        return self.__length
    
    
    
    
class stack:
    
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)
        
    def add(self,num):
        self.__list.insert(0,num)
    
    def pop(self):
        if(self.__len__() - 1 >= 0):
           item = self.__list[0]
           del self.__list[0]
           return item
        else:
            return -1
        
    def give_stack(self):
        return self.__list
    
    def top(self):
        return self.__list[-1]
        

class graph:
    
    def __init__(self,vertices):
        self.__vertices = vertices
        self.__dict = {}
        self.__adjacy_matrices = []
        for i in range(self.__vertices):
            self.__dict[i] = []

    def create_graph_with_edge(self,num_of_edges):
        num_of_edges = num_of_edges
        for i in range(num_of_edges):
            origin_vertice = int(input())
            destination_vertice = int(input())
            self.__dict[origin_vertice].append(destination_vertice)
            self.__dict[destination_vertice].append(origin_vertice)
        return self.__dict

    def create_adjacy_graph(self,drayer):
        for i in range(self.__vertices):
            self.__adjacy_matrices.append([])
            for j in range(self.__vertices):
                drayer = drayer
                self.__adjacy_matrices[i].append(drayer) 
        return self.__adjacy_matrices
        
    
    def get_num_of_vertices(self):
        return self.__vertices
    
    def get_graph(self):
        return self.__dict
    
    def get_adjacy_matrices(self):
        return self.__adjacy_matrices
        


class BFS:

   def __init__(self,dict_graph,num_of_vertices):
       self.__dict_graph = dict_graph
       self.__num_of_vertices = num_of_vertices
       self.__queue = queue()
       self.__distance_matrices = []
       self.__color = ["w" for i in range(num_of_vertices)]
       self.__distance = [0 for i in range(num_of_vertices)]
       self.__parent = [-1 for i in range(num_of_vertices)]

   def reset_C_D_P(self):
        self.__color = ["w" for i in range(self.__num_of_vertices)]
        self.__distance = [0 for i in range(self.__num_of_vertices)]
        self.__parent = [-1 for i in range(self.__num_of_vertices)] 
    
   def get_distance_for_all_vertices(self):
        for n in range(self.__num_of_vertices):
            self.__queue.add(n)
            while len(self.__queue) - 1 >= 0:
                u = self.__queue.pop()
                if u != -1:
                    for i in range(len(self.__dict_graph[u])):
                        j = self.__dict_graph[u][i]
                        if self.__color[j] == "w":
                            self.__color[j] = "g"
                            self.__distance[j] = self.__distance[u] + 1
                            self.__parent[j] = u
                            self.__queue.add(j)
                    self.__color[u] = "B"
            self.__distance_matrices.append(self.__distance)
            self.reset_C_D_P()    
        return self.__distance_matrices


   def get_distance_for_one_vertex_matrice_method(self):
       while len(self.__queue) - 1 >= 0:
        item = self.__queue.pop()
        if item != -1:
            for i in range(self.__num_of_vertices ** 2):
                vertex = i % self.__num_of_vertices
                drayer = int(input())
                if(drayer == 1):
                    if self.__color[vertex] == "W":
                        self.__color[vertex] = "G"
                        self.__parent[vertex] = item
                        self.__distance[vertex] = self.__distance[item] + 1
                        self.__queue.add(vertex)
                if(vertex == 0):
                    self.__color[item] = "B"
                if(vertex == self.__num_of_vertices - 1):
                    item = self.__queue.pop()
            print(item)

       print(f"{self.__color},{self.__distance},{self.__parent}")
       self.reset_C_D_P()


   def get_greatest_distance(self,distance_matrices):
        greatest_num = 0
        for i in range(self.__num_of_vertices):
            for j in range(self.__num_of_vertices):
                if(greatest_num < distance_matrices[i][j]):
                    greatest_num = distance_matrices[i][j]
        return greatest_num


   def determin_path_to_destinationVertex(self,vertex):
      self.__distance_matrices[vertex]
      while(self.__parent[vertex] != -1):
          print(vertex)
          vertex = self.__parent[vertex]
      print(vertex)
         

    
    

# vertices = int(input())
# num_of_edges = int(input())
# def create_matrix(vertices,num_of_edges):
#     grph = graph(vertices)
#     return grph.create_graph_with_edge(num_of_edges)
    

# def get_greatest_distance(dict_graph,vertices):
#     bfs = BFS(dict_graph, vertices)
#     distance_matrices = bfs.get_distance_for_all_vertices()
#     greatest_distance = bfs.get_greatest_distance(distance_matrices)
#     print()
#     print(f" greatest distance is : {greatest_distance}")




# dict_graph = create_matrix(vertices,num_of_edges)
# get_greatest_distance(dict_graph, vertices)




# dfs ===> 

# number_of_nodes = 6
# adjacy_matrices = [[0,1,0,0,0,0],[1,0,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,0,1,0,0],[0,0,0,0,0,0]]
# visited = [False,False,False,False,False,False]
# components = [0 for i in range(number_of_nodes)]
# stck = stack()


# def go_forward(vertex , i):
#     stck.add(vertex)
#     print(f"went forward from {vertex} to {i}")
#     print()

# def back_track(i,j):
#     vertex = stck.pop()
#     print(f"backtracked from {i} to {j}")
#     print()




# def find_components(number_of_nodes):
#     counter = 0
#     for i in range(number_of_nodes):
#         if(visited[i] == False):
#             counter += 1
#             dfs(i,counter)
#             print(f"{counter} : {components}")
            

# def dfs(at,counter):
#     visited[at] = True
#     components[at] = counter
#     for i in range(number_of_nodes):
#         if(adjacy_matrices[at][i] == 1):
#             if(visited[i] == False):
#                 dfs(i,counter)
            
# find_components(number_of_nodes)
    


# def dfs(num_of_nodes):
#     go_forward(0,1)
#     last_length = 0
#     i = 0
#     while(len(stck) != 0):
#         for j in range(number_of_nodes):
#             if visited[j] == False and adjacy_matrices[i][j] == 1:
#                 visited[j] = True
#                 go_forward(j, i)
#                 break
#         current_stack  = stck.give_length()
#         if last_length == current_stack:
#             back_track(i,stck.give_stack()[-1])
#         last_length = stck.give_length()
#         if(stck.give_length() > 0):
#             i = stck.give_stack()[-1]
                


# vertices = int(input())
# num_of_edges = int(input())
# grph = graph(vertices)
# grph.create_graph_with_edge(num_of_edges)
# bfs = BFS(grph.get_graph(), vertices)
# dist = bfs.get_distance_for_all_vertices()


# s_vertice = int(input())
# destination_vertice_1 = int(input())
# destination_vertice_2 = int(input())


# if dist[s_vertice][destination_vertice_1] < dist[s_vertice][destination_vertice_2]:
#     print(destination_vertice_1)
# else:
#     print(destination_vertice_2)



# for i in range(vertices):
#     for j in range(vertices):
#         print(dist[i][j],end=" ")
#     print()


# vertex_count = int(input())
# edge_count = int(input())
# is_E =True
# matrix = [[0]*vertex_count for i in range(vertex_count)]
# for i in range(edge_count):
#     from_ver=int(input())
#     to_ver=int(input())
#     matrix[from_ver][to_ver] = 1
#     matrix[to_ver][from_ver] = 1
# for i in range(vertex_count):
#     if sum(matrix[i]) % 2 != 0:
#         is_E = False
#         break
# if is_E:
#     print("E")
# else:
#     print("NE")


# def dfs(number_of_nodes):
#     counter = 0
#     for i in range(number_of_nodes):
#         if(visited[i] == False) :
#             counter = counter + 1
#             visited[i] = True
#             components[i] = counter
#             stck.add(i)
#             while(stck.give_length() -1 >= 0):
#                 u = stck.pop()
#                 for n in range(number_of_nodes):
#                     if(adjacy_matrices[u][n] == 1):
#                         if(visited[n] != True):
#                             visited[n] = True
#                             stck.add(n)
#                             components[n] = counter
#     print(f"{components}")




# stck = stack()

# while(True):
#     print("1) Create",end="\n")
#     print("2) Push",end="\n")
#     print("3) Pop",end="\n")
#     print("4) Top",end="\n")
#     print("5) print",end="\n")
#     print("6) Exit",end="\n")
        
    
#     intput = int(input())

#     if(intput == 1):
#         print(stck)
#     elif(intput == 2):
#         print("Please enter a value : ")
#         inp = int(input())
#         stck.add(inp)
#         print(f"{inp} has been added",end="\n")
#     elif(intput == 3):
#         v = stck.pop()
#         print(f"{v} has been poped",end="\n")
#     elif(intput == 4):
#         print(f"the top one is {stck.top()}",end="\n")
#     elif(intput == 5):
#         print(f"{stck.give_stack()}")
#     elif(intput == 6):
#         print("the operation has been ended!",end="\n")
#         break



# stck = stack()
# que = queue()

# while(True):
#     print("1) Create stack",end="\n")
#     print("2) Create queue",end="\n")
#     print("3) push",end="\n")
#     print("4) pop",end="\n")
#     print("5) pop & add to queue",end="\n")
#     print("6) remove queue",end="\n")
#     print("7) Exit",end="\n")
    
#     intput = int(input())

#     if(intput == 1):
#         print(stck,end="\n")
#     elif(intput == 2):
#         print(que,end="\n")
#     elif(intput == 3):
#         print("Please enter a value : ")
#         inp = int(input())
#         stck.add(inp)
#         print(f"{inp} has been added",end="\n")
#     elif(intput == 4):
#         v = stck.pop()
#         print(f"{v} has been poped",end="\n")
#     elif(intput == 5):
#         v = stck.pop()
#         q = que.add(v)
#         print(f"{v} has been removed from stack and added to queue : {stck.give_stack()} stack : {que.give_queue()}",end="\n")
#     elif(intput == 6):
#         print("the operation has been ended!",end="\n")
#         break
    
    


# number_of_nodes = 7
# adjacy_matrices = [[0,1,0,0,0,0,0],[1,0,1,0,0,1,0],[0,1,0,1,1,0,0],[0,0,1,0,0,0,0],[0,0,1,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0]]
# visited = [False,False,False,False,False,False,False]
# components = [0 for i in range(number_of_nodes)]
# stck = stack()




# def find_components(num_of_nodes):
#     counter = 0
#     for i in range(number_of_nodes):
#         if(visited[i] == False):
#             counter += 1
#             dfs(i , counter)
#             print(f"{counter} : {components}")
            



# def dfs(node , counter):
#     visited[node] = True
#     components[node] = counter
#     for index,val in enumerate(adjacy_matrices[node]):
#         if(val == 1 and visited[index] == False):
#             dfs(index,counter)



# find_components(number_of_nodes)





# grid 

# grid = [[0,1],
#         [2,3],
#         [4,5]]

# adjacy = [[0,1,1,0,0,0],
#           [1,0,0,1,0,0],
#           [1,0,0,1,1,0],
#           [0,1,1,0,0,1],
#           [0,0,1,0,0,1],
#           [0,0,0,1,1,0]]


# N_DR ==> -1 = north , 1 = south
# S_DR ==> -1 = east , 1 = west
 
# N_DR = [-1,1,0,0]
# S_DR = [0,0,1,-1]

# R = 3
# C = 3
# r = 0
# c = 0


# #     -1 
# # -1 __|__ 1  
# #      |
# #      1
# for i in range(4):
#     rr = r + N_DR[i]
#     cc = c + S_DR[i]
    
#     print(f"({rr} , {cc})",end="\n")
    
#     if(rr < 0 or cc < 0): continue
#     if(rr >= R or cc >= C): continue
    
    
    
    
# impelimenting bfs on a grid 


# while(q.give_length() - 1 >= 0 and is_exit == False):
#     item = q.pop()
#     parent_dict[str(item)] = []
#     current_position = item
#     if item != -1:
#         for i in range(4):
#             rr = current_position[0] + N_DR[i]
#             cc = current_position[1] + S_DR[i]
#             if(rr < 0 or cc < 0): continue
#             if(rr >= R or cc >= C): continue
#             new_position = [rr,cc]
#             if(problem_grid[rr][cc] == "E"):
#                 is_exit = True
#                 parent_dict[str(current_position)].append(new_position)
#                 give_shortest_path([0,0],new_position)
#                 break
#             if(problem_grid[rr][cc] != "."): continue
#             if color[rr][cc] == "W":
#                 q.add(new_position)
#                 color[rr][cc] = "G"
#                 parent_dict[str(current_position)].append(new_position)
#                 new_position = []
#         color[current_position[0]][current_position[1]] = "B"





# class grid:
#     def __init__(self):
#         self.N_DR = [-1,1,0,0]   
#         self.S_DR = [0,0,1,-1]
#         self.x = 0
#         self.y = 0  
    

# # consider every move as 1 minute
# # "." as open ways and "#" as closed ways or rocks
# # problem name : dungon problem

# problem_grid = [["S",".",".","#",".",".","."],
#                 [".","#",".",".",".","#","."],
#                 [".","#",".",".",".",".","."],
#                 [".",".","#","#",".",".","."],
#                 ["#",".","#","E",".","#","."]]

# R = 5
# C = 7
# #bfs on grid
# is_exit = False
# color = [["W" for i in range(C)] for i in range(R)]
# parent_dict = {}
# q = queue()

# # takes parent , starting point and end point to determine quickest way to the exit
# def give_shortest_path(s,e):
#     shortest_path = []
#     str_e = str(e)
#     for key,values in parent_dict.items().__reversed__():
#         for value in values:
#             if(str_e == str(value)):
#                 shortest_path.append(value)
#                 str_e = key
#     shortest_path.append(s)
#     shortest_path.reverse()    
#     print(f"the shortest path is : {shortest_path} \n and it takes about {len(shortest_path)} minutes to reach the exit")
    

# # add neibourings to the queue if possible
# def add_neigbour(new_position,current_position):
#     if(problem_grid[new_position.x][new_position.y] == "E"):
#             is_exit = True
#             parent_dict[str(current_position)].append([new_position.x,new_position.y])
#             give_shortest_path([0,0],[new_position.x,new_position.y])
#     if(problem_grid[new_position.x][new_position.y] != "."): return
#     if color[new_position.x][new_position.y] == "W":
#         q.add([new_position.x,new_position.y])
#         color[new_position.x][new_position.y] = "G"
#         parent_dict[str(current_position)].append([new_position.x,new_position.y])
#         new_position = []    
    
    
# # looks for neibourings of a point on grid(up,down,left,right)
# def search_for_neigbours(current_position,i):
#     g = grid()
#     g.x = current_position[0] + g.N_DR[i]
#     g.y = current_position[1] + g.S_DR[i]
#     if(g.x < 0 or g.y < 0): return
#     if(g.x >= R or g.y >= C): return
#     return g
    
    


# def bfs_in_grid(current_position):
#     q.add(current_position)
#     while(q.give_length() - 1 >= 0 and is_exit == False):
#         item = q.pop()
#         parent_dict[str(item)] = []
#         current_position = item
#         if item != -1:
#             # looks for neibourings of a point on grid(up,down,left,right)
#             for i in range(4):
#                 new_position = search_for_neigbours(current_position,i)
#                 if new_position == None: continue
#             # add neibourings to the queue if possible
#                 add_neigbour(new_position,current_position)
#             color[current_position[0]][current_position[1]] = "B"
        

# # place u wanna start on grid
# current_position = [0,0]
# bfs_in_grid(current_position)



# alternate approach on dungon problem

# problem_grid = [["S",".",".","#",".",".","."],
#                 [".","#",".",".",".","#","."],
#                 [".","#",".",".",".",".","."],
#                 [".",".","#","#",".",".","."],
#                 ["#",".","#","E",".","#","."]] 

# R = 5
# C = 7
# color = [["W" for i in range(C)] for i in range(5)]

# r_q = queue()
# c_q = queue()
# rp = 0
# cp = 0

# move_count = 0
# nodes_left_in_layer = 1
# nodes_in_next_layer = 0
# found_exit = False

# r_q.add(rp)
# c_q.add(cp)
# while(len(r_q) > 0 and found_exit == False):
#     c = c_q.pop()
#     r = r_q.pop()
#     nodes_left_in_layer -= 1
#     if(c != -1 and r != -1):
#         for i in range(4):
#             N_DR = [-1,1,0,0]   
#             S_DR = [0,0,1,-1]
#             cp = c + N_DR[i] 
#             rp = r + S_DR[i]
#             if(cp < 0 or rp < 0): continue
#             elif(cp >= C or rp >= R): continue
#             if(color[rp][cp] != "W"): continue
#             if(problem_grid[rp][cp] == "#"): continue
#             if(problem_grid[rp][cp] == "E"):
#                 found_exit = True
#             c_q.add(cp)
#             r_q.add(rp)
#             nodes_in_next_layer += 1
#             color[rp][cp] = "G"
#         color[r][c] = "B"
#         if(nodes_left_in_layer == 0):
#             nodes_left_in_layer = nodes_in_next_layer
#             nodes_in_next_layer = 0
#         move_count += 1

# print(move_count)





# topological sorting
# in order to make this work ==> 
# we need DAG(directed acyclic graph) 
# a graph with directed edges and no cycles 

# num_of_nodes = 13

# graph_list = {
#     "A":["D"],
#     "B":["D"],
#     "C":["A","B"],
#     "D":["H","G"],
#     "E":["A","D","F"],
#     "F":["K","J"],
#     "G":[],
#     "H":["J","I"],
#     "I":["L"],
#     "J":["M","L"],
#     "K":["J"],
#     "L":[],
#     "M":[],
# }

# visited = {}
# for i in graph_list:
#     visited[i] = False

# stck = stack()



# def dfs(node):
#     visited[node] = True
#     for value in graph_list[node]:
#         if visited[value] == False:
#             dfs(value)
#             stck.add(value)

# for i in graph_list:
#     if visited[i] == False:
#         dfs(i)
#         stck.add(i)
        
        
# print(stck.give_stack())
        
        


# longest and shortest path on DAG

weight_graph_list = {
    "H":[],
    "A":[["B",3],["C",6]],
    "E":[["H",9]],    
    "F":[["H",1]],
    "B":[["C",4],["D",4],["E",11]],
    "C":[["D",8],["G",11]],
    "G":[["H",2]],
    "D":[["E",-4],["F",5],["G",2]],
}

# shortest path

visited = {}
q = queue()
prev_dist = 0
for i in weight_graph_list:
    visited[i] = False

stck = stack()


def top_sort():
    search_all_nodes()
    return stck.give_stack()


def search_all_nodes():
    for i in weight_graph_list:
        if visited[i] == False:
            dfs(i)
            stck.add(i)

def dfs(node):
    visited[node] = True
    for value in weight_graph_list[node]:
        if visited[value[0]] == False:
            dfs(value[0])
            stck.add(value[0])

top_sorted_graph = top_sort()

distance = {}
for i in top_sorted_graph:
    distance[i] = 0
    
    
def DAG_shortest_path():
    q.add(0)
    for i in top_sorted_graph:
        prev_dist = distance[i]
        if prev_dist != -1:
            for item in weight_graph_list[i]:
                if(distance[item[0]] == 0):
                    distance[item[0]] = prev_dist + item[1]
                elif(distance[item[0]] > prev_dist + item[1]):
                    distance[item[0]] = prev_dist + item[1]
        
    print(f"shortest paths : {distance}")
    

# longest path

def DAG_longest_path():
    q.add(0)
    for i in top_sorted_graph:
        prev_dist = distance[i]
        if prev_dist != -1:
            for item in weight_graph_list[i]:
                if(distance[item[0]] == 0):
                    distance[item[0]] = prev_dist + item[1]
                elif(distance[item[0]] < prev_dist + item[1]):
                    distance[item[0]] = prev_dist + item[1]
        
    print(f"longest paths : {distance}")       



DAG_shortest_path()
DAG_longest_path()





            
        
            
            
            

            

        
        
        










    



                            
                    
                    
    
    