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


stck = stack()
stck.add(3)
stck.add(4)
stck.add(1)
stck.add(5)
stck.add(7)
stck.add(8)
stck.add(4)
stck.add(6)





class orderedLinkedList:
    def __init__(self):
        self.first = None
        self.h = None
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





l = orderedLinkedList()
l.add_ordered()
l.add_ordered()
l.add_ordered()
l.print()





        
        


