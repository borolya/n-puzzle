import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.total_size = 0
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, [priority, item])
    
    def get(self):
        self.total_size += 1
        elem = heapq.heappop(self.elements)
        return elem[1]
    
    def get_total_size(self):
        return (self.total_size)

    def len(self):
        return len(self.elements)
