import heapq
import itertools

class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.get_size = 0
        self.unique_sequence_count = 0
        self.entry_finder = {}
        self.counter = itertools.count() 
        self.REMOVED = '<removed-item>'
    
    def empty(self):
        return self.unique_sequence_count == self.get_size
    
    def put(self, item, priority):
        if item[0] in self.entry_finder:
            self.remote_item(item[0])
        else:
            self.unique_sequence_count +=1
        entry = [priority, self.unique_sequence_count, item]
        self.entry_finder[item[0]] = entry
        heapq.heappush(self.elements, entry)

    def remote_item(self, item):
        entry = self.entry_finder[item]
        entry[-1] = self.REMOVED

    def get(self):
        while self.elements:
            priority, count, item = heapq.heappop(self.elements)
            if item is not self.REMOVED:
                del self.entry_finder[item[0]]
                self.get_size += 1
                return item
        raise KeyError('pop from an empty priority queue')
    
    def get_total_size(self):
        return (self.get_size)

    def len(self):
        return len(self.elements)

class TimeComplexity:
    def __init__(self):
        self.time = 0

    def add(self):
        self.time +=1

    def get_total_size(self):
        return (self.time)
    