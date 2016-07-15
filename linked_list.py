class AbstractLinkedList(object):
    """
    Abstract class representing the LinkedList inteface you must respect.
    
    You must not implement any of the method in this class, and this class
    must never be instantiated. It's just a "guide" of which methods
    the LinkedList class should respect.
    """

    def __str__(self):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __add__(self, other):
        raise NotImplementedError()

    def __iadd__(self, other):
        raise NotImplementedError()

    def __eq__(self, other):
        raise NotImplementedError()

    def append(self, element):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()

    def pop(self, index=None):
        raise NotImplementedError()

class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        return self.elem == other.elem
        
    def __repr__(self):
        return self.__str__()

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """
    def __init__(self, elements=None):
        if elements:
            self.start = Node(elements[0])
            place_holder = self.start
            for elem in elements[1:]:
                current_node = Node(elem)
                place_holder.next = current_node
                place_holder = current_node
            self.end = Node(elements[-1])
        else:
            self.start = None
            self.end = None
                
    def __str__(self):
        return str([n for n in self])
        
    def __repr__(self):
    	return self.__str__()

    def __len__(self):
        return self.count()

    def __iter__(self):
        counter_node = self.start
        while counter_node:
            yield counter_node
            counter_node = counter_node.next

    def __getitem__(self, index):
        counter = 0
        for node in self:
            if counter == index:
                return node
            counter += 1
            
    def __add__(self, other):
        return self.__class__([n.elem for n in self] + [n.elem for n in other])    
        
    def __iadd__(self, other):
        return self + other        
        
    def __eq__(self, other):
    	
        return [n for n in self] == [n for n in other] 

    def append(self, elem):
        new_end = Node(elem)
        if self.end:
            self.end.next = self.end = new_end
        else:
            self.start = self.end = new_end

    def count(self):
        counter = 0
        for item in self:
            counter +=1
        return counter

    def pop(self, index = None):
        if index is None:
            index = self.count()-1
            
        if len(self) == 0 or index >= self.count():
            raise IndexError()
            
        if index == 0:
            dummy = self.start.elem
            self.start = self.start.next
            return dummy
            
        node = self[index-1]
        popped_item = self[index].elem
        node.next = self[index].next
        return popped_item
