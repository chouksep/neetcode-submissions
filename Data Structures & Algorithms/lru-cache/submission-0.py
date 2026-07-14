## Defining a class to create double linked list data structure
class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        # Initiate and store capacity value
        self.cap = capacity
        # Initiate a hash map called cache to store key mapped to Node
        self.cache = {}

        # Create two pointers- left, right. Left next represents least recently used
        # right prev represents most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            # Since this key is recently used
            # it should come at rightmost part of the linked list
            # Remove from current position
            self.remove(self.cache[key]) #TODO
            self.insert(self.cache[key]) #TODO
            return self.cache[key].value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Then we need to update the value
            # also make it most recent
            self.remove(self.cache[key])
        # Update cache with updated key-value pair
        self.cache[key] = Node(key, value)
        # Insert into linked list
        self.insert(self.cache[key])
        # if capacity exceeds, remove least recently used key
        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

    # Helper functions
    def remove(self, node):
        # Access its previous and next nodes
        prev_node, next_node = node.prev, node.nxt
        # Point previous and next nodes to each other
        # thus removing the node
        prev_node.nxt, next_node.prev = next_node, prev_node
    
    def insert(self, node):
        # when inserting, we want to insert at the 
        # rightmost side since it is recently used
        right_node_prev = self.right.prev 
        right_node_prev.nxt  = node
        self.right.prev = node
        node.prev = right_node_prev
        node.nxt = self.right


        
