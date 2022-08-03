class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None
        
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dct = defaultdict(list)
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        

    def add(self, node):
        cur = self.head.next
        node.next = cur
        cur.prev = node
        self.head.next = node
        node.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        nxt.prev = prev
        prev.next = nxt
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dct:
            self.remove(self.dct[key])
            self.add(self.dct[key])
            return self.dct[key].value
        return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = Node(key, value)
        
        if key in self.dct:
            self.remove(self.dct[key])
        self.add(node)
        self.dct[key] = node
        
        if len(self.dct) > self.capacity:
            prev = self.tail.prev
            self.remove(prev)
            del self.dct[prev.key]
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)