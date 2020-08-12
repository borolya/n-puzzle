import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        elem = heapq.heappop(self.elements)
        return elem[1]
    
    def len(self):
        return len(self.elements)
