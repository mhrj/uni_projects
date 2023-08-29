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


    def add_ordered(self):
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






        
        


