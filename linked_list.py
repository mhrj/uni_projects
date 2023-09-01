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


class linkedList:
    def __init__(self):
        self.first = None
        self.length = 0

    class node:
        def __init__(self,element,next):
            self.element = element
            self.next = next
    
    def add_to_first(self,element):
        self.first = self.node(element, self.first)
        self.length += 1
    
    def add_to_last(self,element):
        item = self.first
        for i in range(self.length - 1):
           item = item.next
        new_node = self.node(element, None)
        item.next = new_node
        self.length += 1

    def print(self):
        item = self.first
        print(item.element)
        for i in range(self.length - 1):
            item = item.next
            print(item.element)

    def delete_from_top(self):
        f = self.first.next
        del self.first
        self.first = f
        self.length -= 1

    def delete_from_last(self):
        item = self.first
        for i in range(self.length - 2):
           item = item.next
        item.next = None
        del item.next
        self.length -= 1


class stackedLinkedList:
    def __init__(self):
        self.first = None
        self.length = 0

    class node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def print(self):
        item = self.first
        print(item.element)
        for i in range(self.length - 1):
            item = item.next
            print(item.element)
    
    def add(self,element):
        self.first = self.node(element, self.first)
        self.length += 1

    def delete(self):
        f = self.first.next
        first = self.first
        del self.first
        self.first = f
        self.length -= 1
        return first


class queuedLinkedList:
    def __init__(self):
        self.first = None
        self.length = 0

    class node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def print(self):
        item = self.first
        print(item.element)
        for i in range(self.length - 1):
            item = item.next
            print(item.element)
    
    def add(self,element):
        if self.first == None:
            self.first = self.node(element, None)
            self.length += 1
        else:
            item = self.first
            for i in range(self.length - 1):
                item = item.next
            new_node = self.node(element, None)
            item.next = new_node
            self.length += 1

    def delete(self):
        f = self.first.next
        first = self.first
        del self.first
        self.first = f
        self.length -= 1
        return first


class orderedLinkedList:
    def __init__(self):
        self.first = None
        self.h = None
        self.length = 0

    class node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def show_as_list(self):
        item = self.first
        arr = [item.element]
        for i in range(self.length - 1):
            item = item.next
            arr.append(item.element)
        return arr


    def delete_from_top(self):
        f = self.first.next
        del self.first
        self.first = f
        self.length -= 1


    def add_ordered(self,stck):
        element = stck.pop()
        if self.first == None:
            self.first = self.node(element, self.first)
            self.length += 1
        else:
            self.h = self.first
            first = self.first
            while(self.h != None):
                if element == self.h.element or element == self.first.element: break
                elif element < first.element:
                    new_node = self.node(element, first)
                    self.first = new_node
                    self.length += 1
                    break
                elif element < self.h.element:
                    new_node = self.node(element, self.h)
                    first.next = new_node
                    self.length += 1
                    break
                first = self.h
                self.h = first.next
            if self.h == None:
                    new_node = self.node(element, None)
                    first.next = new_node
                    self.length += 1



class GraphLinkedList:
    def __init__(self):
        self.list = []
        self.v_count = []

    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next

    def make_linked_list(self,num_of_nodes):
        for i in range(num_of_nodes):
            new_node = self.Node(i,None)
            self.list.append(new_node)
            self.v_count.append(0)


    def add_neighbours(self,from_v,to_v):
        p = self.list[from_v]
        for i in range(self.v_count[from_v]):
            p = p.next
        p.next = self.Node(to_v, None)
        self.v_count[from_v] += 1
        
        
    def adjacency_to_linked_list(self,num_of_nodes,adjacency):
        self.make_linked_list(num_of_nodes)
        for i in self.list:
            from_v = i.element
            for j in range(num_of_nodes):
                if(adjacency[from_v][j] == 1):
                    to_v = j
                    self.add_neighbours(from_v,to_v)

    def print(self):
        for i in self.list:
            if i.next == None: continue
            print(f"node {i.element} ===>")
            p = i.next
            for j in range(self.v_count[i.element]):
                print(f"   {p.element}")
                p = p.next




    

    





        
        


