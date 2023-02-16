class node(object):
    def __init__(self , val):
        self.val = val
        self.next = None
    
    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class linked_list(object):
    def __init__(self, head = None):
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        item = self.head
        while item != None:
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()
        return None
    
    def delete_at(self, idx):
        if idx > self.count:
            return
        if idx == 0:
            self.head = self.head.get_next()
        else:
            temp_idx = 0
            node = self.head
            while temp_idx < idx - 1:
                node = node.get_next()
                temp_idx += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1
            

    def dump_list(self):
        tempnode = self.head
        while tempnode != None:
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()

# Create a linked list and add items
item_list = linked_list()
item_list.insert(25)
item_list.insert(56)
item_list.insert(39)
item_list.insert(32)
item_list.dump_list()

# Exercise the list
# print("Item count: ", item_list.get_count())
# print("Find item: ", item_list.find(25))
# print("Find item: ", item_list.find(14))

# Deleting items
item_list.delete_at(3)
print("Item count: ", item_list.get_count())
print("Finding item:", item_list.find(25))
item_list.dump_list()