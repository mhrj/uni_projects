import math

class MaxHeap:
    
    def __init__(self,heap):
        self.__heap = heap
        self.__length = len(heap)
        
        
    def show_heap(self):
        return self.__heap
        
        
    def swap_child_and_parent(self,parent_index,child_index):
            child_val = self.__heap[child_index]
            self.__heap[child_index] = self.__heap[parent_index]
            self.__heap[parent_index] = child_val
            
            
    def rearrange_from_bottom_to_top(self,element):
            child_index = self.__length - 1
            parent_index = math.floor((self.__length / 2)) - 1
            while(element > self.__heap[parent_index]):
                self.swap_child_and_parent(parent_index,child_index)
                child_index = parent_index
                parent_index = math.floor(child_index / 2)
        
        
    def rearange_from_top_to_bottom(self,element_to_compare):
        compare_index = 1
        while(self.__length - 1 > compare_index):
            element_to_compare_index = math.floor(compare_index / 2)
            if(self.__heap[compare_index] > self.__heap[compare_index + 1]):
                if(self.__heap[compare_index] > element_to_compare and compare_index <= self.__length):
                    self.swap_child_and_parent(element_to_compare_index,compare_index)
                    compare_index = (compare_index * 2) + 1
                else:
                    break
            elif(self.__heap[compare_index] < self.__heap[compare_index + 1]):
                if(self.__heap[compare_index + 1] > element_to_compare and compare_index + 1 <= self.__length):
                    self.swap_child_and_parent(element_to_compare_index,compare_index + 1)
                    compare_index = (compare_index * 2) + 3
                else:
                    break

         
         
    def insert(self,element):
        if self.__length > 0:
            self.__heap.append(element)
            self.__length += 1
            self.rearrange_from_bottom_to_top(element)
        else:
            self.__heap.append(element)
            self.__length += 1
            
            
    def remove(self):
        if(self.__length - 1 != 0):
            element = self.__heap[0]
            self.__heap[0] = self.__heap[self.__length - 1]
            self.rearange_from_top_to_bottom(self.__heap[0])
            self.__heap[self.__length - 1] = element
            self.__length -= 1
            return element
        else:
            return None
        
    
    def sort(self):
        for i in range(self.__length - 1):
            self.remove()
        return self.show_heap()
    
    
    
class MinHeap():
    
    def __init__(self,heap):
        self.__heap = heap
        self.__length = len(heap)
        
        
    def show_heap(self):
        return self.__heap
        
        
    def swap_child_and_parent(self,parent_index,child_index):
            child_val = self.__heap[child_index]
            self.__heap[child_index] = self.__heap[parent_index]
            self.__heap[parent_index] = child_val
            
            
    def rearrange_from_bottom_to_top(self):
            element = self.__heap[-1]
            child_index = self.__length - 1
            parent_index = math.floor((self.__length / 2)) - 1
            while(element < self.__heap[parent_index]):
                self.swap_child_and_parent(parent_index,child_index)
                child_index = parent_index
                parent_index = math.floor(child_index / 2)
        
        
    def rearange_from_top_to_bottom(self):
        compare_index = 1
        element_to_compare = self.__heap[0]
        while(self.__length - 1 > compare_index):
            element_to_compare_index = math.floor(compare_index / 2)
            if(self.__heap[compare_index] < self.__heap[compare_index + 1]):
                if(self.__heap[compare_index] < element_to_compare and compare_index <= self.__length):
                    self.swap_child_and_parent(element_to_compare_index,compare_index)
                    compare_index = (compare_index * 2) + 1
                else:
                    break
            elif(self.__heap[compare_index] > self.__heap[compare_index + 1]):
                if(self.__heap[compare_index + 1] < element_to_compare and compare_index + 1 <= self.__length):
                    self.swap_child_and_parent(element_to_compare_index,compare_index + 1)
                    compare_index = (compare_index * 2) + 3
                else:
                    break

         
         
    def insert(self,element):
        if self.__length > 0:
            self.__heap.append(element)
            self.__length += 1
            self.rearrange_from_bottom_to_top()
        else:
            self.__heap.append(element)
            self.__length += 1
            
            
    def remove(self):
        if(self.__length - 1 != 0):
            element = self.__heap[0]
            self.__heap[0] = self.__heap[self.__length - 1]
            self.rearange_from_top_to_bottom()
            self.__heap[self.__length - 1] = element
            self.__length -= 1
            return element
        else:
            return None
        
    
    def sort(self):
        for i in range(self.__length - 1):
            self.remove()
        return self.show_heap()
        
        
        
class Heapify():
    def __init__(self,arr):
        self.__heap = arr
        self.__length = len(arr)
        
    def get_heap(self):
        return self.__heap
        
         
    def swap_child_and_parent(self,parent_index,child_index):
            child_val = self.__heap[child_index]
            self.__heap[child_index] = self.__heap[parent_index]
            self.__heap[parent_index] = child_val
    
    def __rearange_from_bottom_to_top_min_heapify(self,parent_index):
        current_point = None
        child_index = (parent_index * 2) + 1
        while(parent_index >= 0):
            if(child_index <= self.__length - 1):
                if(self.__heap[child_index] > self.__heap[child_index + 1]):
                    if(self.__heap[child_index + 1] < self.__heap[parent_index]):
                        self.swap_child_and_parent(parent_index,child_index)
                    if(current_point == None): current_point = parent_index - 1
                    parent_index = child_index
                    child_index = (parent_index * 2) + 1
                else:
                    if(self.__heap[child_index] < self.__heap[parent_index]):
                        self.swap_child_and_parent(parent_index,child_index)  
                    if(current_point == None): current_point = parent_index - 1
                    parent_index = child_index
                    child_index = (parent_index * 2) + 1
            else: 
                if current_point != None:
                    parent_index = current_point
                    current_point = None
                else:
                    parent_index -= 1
                child_index = (parent_index * 2) + 1
                
    def __rearange_from_bottom_to_top_max_heapify(self,parent_index):
        current_point = None
        child_index = (parent_index * 2) + 1
        while(parent_index >= 0):
            if(child_index <= self.__length - 1):
                if(self.__heap[child_index] > self.__heap[child_index + 1]):
                    if(self.__heap[child_index] > self.__heap[parent_index]):
                        self.swap_child_and_parent(parent_index,child_index)
                    if(current_point == None): current_point = parent_index - 1
                    parent_index = child_index
                    child_index = (parent_index * 2) + 1
                else:
                    if(self.__heap[child_index + 1] > self.__heap[parent_index]):
                        self.swap_child_and_parent(parent_index,child_index + 1)  
                    if(current_point == None): current_point = parent_index - 1
                    parent_index = child_index
                    child_index = (parent_index * 2) + 1
            else:
                if current_point != None:
                    parent_index = current_point
                    current_point = None
                else:
                    parent_index -= 1
                child_index = (parent_index * 2) + 1
    
    
    def create_min_heap(self):
        parent_index = self.__length - 1
        self.__rearange_from_bottom_to_top_min_heapify(parent_index)
        
    
    def create_max_heap(self):
        parent_index = self.__length - 1
        self.__rearange_from_bottom_to_top_max_heapify(parent_index)

class MinIndexedDHeap():
    
    def __init__(self,degree):
        self.__heap = []
        self.__length = 0
        self.__degree = degree
         
    
    def show_heap(self):
        return self.__heap
    
    def show_length(self):
        return self.__length
    

    def swap_child_and_parent(self,parent_index,child_index):
            child_val = self.__heap[child_index]
            self.__heap[child_index] = self.__heap[parent_index]
            self.__heap[parent_index] = child_val

        
    def __rearrange_from_bottom_to_top(self):
            element = self.__heap[-1]
            child_index = self.__length - 1
            parent_index = math.floor((child_index - 1) / self.__degree)
            while(element.weight < self.__heap[parent_index].weight and child_index > 0):
                self.swap_child_and_parent(parent_index,child_index)
                child_index = parent_index
                parent_index = math.floor((child_index - 1) / self.__degree)
                
                
    def __rearange_from_top_to_bottom(self):
        child_index = 1
        element_to_compare = self.__heap[0].weight
        while(self.__length - 1 > child_index):
            least_index = child_index
            num_of_repeat = 0
            element_to_compare_index = math.floor((child_index - 1) / self.__degree)
            while(child_index + 1 < self.__length - 1 and num_of_repeat < self.__degree - 1):
                if(self.__heap[least_index].weight < self.__heap[child_index + 1].weight):
                    least_index = least_index
                else:
                    least_index = child_index + 1
                child_index += 1
                num_of_repeat += 1
            if(self.__heap[least_index].weight < element_to_compare):
                self.swap_child_and_parent(element_to_compare_index,least_index)
                child_index = ((least_index + 1) * self.__degree) - (self.__degree - 1)
            else:
                break
            
            
    def __rearange_from_a_point_to_top(self,element_index):
        element = self.__heap[element_index].weight
        child_index = element_index
        parent_index = math.floor((child_index - 1) / self.__degree)
        while(element < self.__heap[parent_index].weight and child_index > 0):
            self.swap_child_and_parent(parent_index,child_index)
            child_index = parent_index
            parent_index = math.floor((child_index - 1) / self.__degree)
        
        
    def insert(self,element):
        if self.__length > 0:
            self.__heap.append(element)
            self.__length += 1
            self.__rearrange_from_bottom_to_top()
        else:
            self.__heap.append(element)
            self.__length += 1
    
    
    def remove(self):
        if(self.__length <= 0) : return
        element = self.__heap[0]
        if(self.__length - 1 != 0):
            self.__heap[0] = self.__heap[-1]
            del self.__heap[-1]
            self.__rearange_from_top_to_bottom()
            self.__length -= 1
            return element
        else:
            self.__length -= 1
            del self.__heap[-1]
            return element
        
    
    def update(self,element,val,origin = 0):
        for i in range(self.__length):
            if(element == self.__heap[i].to):
                self.__heap[i].weight = val
                self.__heap[i].origin = origin
                self.__rearange_from_a_point_to_top(i)


    def does_exist(self,node):
        for i in range(self.__length):
            if(node.to == self.__heap[i].to):
                return self.__heap[i]
        return -1
