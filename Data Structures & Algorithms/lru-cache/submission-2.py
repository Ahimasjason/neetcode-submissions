
# from collections import deque

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key

    def __repr__(self):
        return f"Node(val = {self.val} , key = {self.key})"
class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.slots = []
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self.slots.remove(n)
            self.slots.append(n)
            return n.val
        return -1


    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.d:
            
            self.slots.remove(self.d[key])
        self.slots.append(node)
        self.d[key] = node
        if len(self.slots) > self.cap:
            n = self.slots.pop(0)
            del self.d[n.key]
        
