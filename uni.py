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
        self.__length = 0
        self.__list = []
        
    def add(self,num):
        self.__length += 1
        self.__list.append(num)
    
    def pop(self):
        if(self.__length - 1 >= 0):
           item = self.__list[0]
           del self.__list[0]
           self.__length -= 1
           return item
        else:
            return -1
    
    def give_item(self,index):
       if(self.__length > 0):
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
        self.__length = 0
        self.__list = []
        
    def add(self,num):
        self.__length += 1
        self.__list.append(num)
    
    def pop(self):
        if(self.__length - 1 >= 0):
           item = self.__list[-1]
           del self.__list[-1]
           self.__length -= 1
           return item
        else:
            return -1
        
    def give_stack(self):
        return self.__list
    
            
    def give_length(self):
        return self.__length
        
    

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
            while self.__queue.give_length() - 1 >= 0:
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
       while self.__queue.give_length() - 1 >= 0:
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
                        q.add(vertex)
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
          vertex = p[vertex]
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

number_of_nodes = 6
adjacy_matrices = [[0,1,0,0,0,0],[1,0,1,1,0,0],[0,1,0,0,1,0],[0,1,0,0,1,0],[0,0,0,1,0,0],[0,0,0,0,0,0]]
visited = [False,False,False,False,False,False]
components = [0 for i in range(number_of_nodes)]
stck = stack()


def go_forward(vertex , i):
    stck.add(vertex)
    print(f"went forward from {vertex} to {i}")
    print()

def back_track(i,j):
    vertex = stck.pop()
    print(f"backtracked from {i} to {j}")
    print()




def find_components(number_of_nodes):
    counter = 0
    for i in range(number_of_nodes):
        if(visited[i] == False):
            counter += 1
            dfs(i,counter)
            print(f"{counter} : {components}")
            

def dfs(at,counter):
    visited[at] = True
    components[at] = counter
    for i in range(number_of_nodes):
        if(adjacy_matrices[at][i] == 1):
            if(visited[i] == False):
                dfs(i,counter)
            
find_components(number_of_nodes)
    
            
                









# def dfs(num_of_nodes):
#     go_forward(0,1)
#     last_length = 0
#     i = 0
#     while(stck.give_length() != 0):
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



# dfs(number_of_nodes)
                            
                    
                    
    
    