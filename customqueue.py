import math
import graphstructures

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
    
    
class priorityQueue:
    def __init__(self):
        self.__list = []
        
    def __len__(self):
        return len(self.__list) 

    def add(self,num):
        self.__list.append(num)
        
    def update(self,num):
        self.__list[0].weight = num
        
    def does_exist(self,num):
        for i in range(self.__list.__len__()):
            if(num.to == self.__list[i].to):
                return i
            else:
                return -1
        return -1
    
    def pop(self):
        if self.__len__() > 0:
            min_val = graphstructures.node(weight=math.inf,to=math.inf)
            min_val_index = 0
            for i in range(self.__len__()):
                if(self.__list[i].weight < min_val.weight):
                    min_val_index = i
                    min_val = self.__list[i]
            del self.__list[min_val_index]
            return min_val
    
    def give_list(self):
        return self.__list