from node import Node

class LinkedList(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False # data not found      
    
    def find(self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None


my_list = LinkedList()
my_list.add(5)
my_list.add(8)
my_list.add(12)
my_list.remove(8)
print(my_list.remove(12))
print(my_list.find(5))