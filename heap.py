import math

class maxHeap:
    def __init__(self,arr):
        self.__list = arr
        self.__length = len(arr)
        self.__d = {}
       
    def show_simplified(self):
        length = self.__length
        for i in self.__list:
            self.__d[i] = []
        while(length != 1):
            self.__d[self.__list[math.floor(length / 2 - 1)]].append(self.__list[length - 1]) 
            length -= 1
        return self.__d
    
    def m_add(self,num):
        self.__list.append(num)
        self.__length += 1
        index = self.__length
        p = self.__list[math.floor(self.__length / 2 - 1)]
        while(num > p or index != -1):
            parent = self.__list[math.floor(index / 2 - 1)]
            child = self.__list[math.floor(index - 1)] 
            self.__list[index - 1] = parent
            self.__list[math.floor(index / 2 - 1)] = child
            index = math.floor(index / 2 - 1)
            p = self.__list[math.floor(math.floor(index / 2))]
        
            
        
compelete_binary_search = [50,30,20,15,10,8,16]
m_heap = maxHeap(compelete_binary_search)
m_heap.m_add(60)
print(m_heap.show_simplified())