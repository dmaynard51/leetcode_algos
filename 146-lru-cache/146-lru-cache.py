class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dct = defaultdict(list)

        
    def add(self, node):
        
        cur = self.head.next
        node.next = cur
        node.prev = self.head
        cur.prev = node
        self.head.next = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        
        
        
        
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dct:
            self.remove(self.dct[key])
            self.add(self.dct[key])
            return self.dct[key].val
        
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
            last = self.tail.prev
            self.remove(last)
            del self.dct[last.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)