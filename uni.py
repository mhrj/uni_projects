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






class queue:
    
    def __init__(self):
        self.__length = 0
        self.__list = []
        
    def add(self,num):
        self.__length += 1
        self.__list.append(num)
    
    def pop(self):
        if(self.__length >= 0):
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
        
    

class graph:
    
    def __init__(self):
        self.__vertices = int(input())
        self.__dict = {}
        for i in range(self.__vertices):
            self.__dict[i] = []

    
    def create_graph_with_edge(self):
        num_of_edges = int(input())
        for i in range(num_of_edges):
            origin_vertice = int(input())
            destination_vertice = int(input())
            self.__dict[origin_vertice].append(destination_vertice)
            self.__dict[destination_vertice].append(origin_vertice)
        
    
    def get_num_of_vertices(self):
        return self.__vertices
    
    def get_graph(self):
        return self.__dict
        
        
            


grph = graph()
create_grph = grph.create_graph_with_edge()
num_of_vertices = grph.get_num_of_vertices()
dic = grph.get_graph()
print(dic)

# bfs ======> 

q = queue()
color = ["w" for i in range(num_of_vertices)]
distance = [0 for i in range(num_of_vertices)]
p = [-1 for i in range(num_of_vertices)]

q.add(0)

while q.give_length() >= 0:
    u = q.pop()
    if u != -1:
        for i in range(len(dic[u])):
            j = dic[u][i]
            if color[j] == "w":
                color[j] = "g"
                distance[j] = distance[u] + 1
                p[j] = u
                q.add(j)
        color[u] = "B"
    print(u)        
        




        
        
    
    
    
    
    
    
    
    