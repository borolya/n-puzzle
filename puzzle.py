def a_star(start, pheuristic) #start -- graph_tipe
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    level = {}
    came_from[start] = None
    level[start] = 0
    while not frontier.empty():
        current = frontier.get()

        if current == start.final_state():
            break

        for next in current.neighbors():
            new_level = level[current] + 1
            if next not in level or new_level < level[next]
                level[next] = new_level
                priority = new_level + next.heuristic(pheuristic)
                frontier.put(next, priority)
                came_from[next] = current


class PriorityQueue:


class Graph: # == puzzle
    def __init__(self, initial_state, size, zero_pos):
        self.size = size
        self.array = array
        
        #if created it

    def __del__(self):
        #if i deleted it

    def h_score(self, h):
    
    def child(self):
    


class Graph: 
    def __init__(self, root, goal):

    def child(self, puzzle)
        return puzzle1, puzzle2, puzzle3, puzzle4
    