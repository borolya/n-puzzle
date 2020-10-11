from queue import *
import draw as draw
import heuristic as h

def uniform_cost_search(graph, start):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    level = {}
    level[start[0]] = 0
    while not frontier.empty():
        current = frontier.get()
        current_level = level[current[0]] + 1
        if (graph.check_valid(current[0])):
            break
        for next in graph.neighbors(current):
            if next[0] not in came_from:
                priority = current_level
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
                level[next[0]] = current_level
    return frontier, came_from

def gready_search(graph, start, heuristic):
    frontier = PriorityQueue()
    start[2] = heuristic(None, start, graph)
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    while not frontier.empty():
        current = frontier.get()

        if (graph.check_valid(current[0])):
            break

        for next in graph.neighbors(current):
            if next[0] not in came_from:
                priority = heuristic(current, next, graph)
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
    return frontier, came_from

def a_star(graph, start, heuristic):
    frontier = PriorityQueue()
    start[2] = heuristic(None, start, graph)
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    level = {}
    level[start[0]] = 0
    while not frontier.empty():
        current = frontier.get()
        current_level = level[current[0]] + 1
        if (graph.check_valid(current[0])):
            break
        for next in graph.neighbors(current):
            if (next[0] not in came_from or level[next[0]] > current_level):     
                priority = heuristic(current, next, graph) + current_level
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
                level[next[0]] = current_level
    return frontier, came_from


def ida_search(graph, start, heuristic):
    def search(path, graph, level, bound, heuristic, time):
        current = path[-1]
        f = level + current[2]
        time.add()
        if f > bound:
            return f, False
        if current[0] == graph.final_state:
            return f, True
        next_bound = float('inf')
        for next in graph.neighbors(current):
            if next[0] not in map(lambda x : x[0], path):
                next[2] = heuristic(current, next, graph)
                path.append(next)
                f, found = search(path, graph, level + 1, bound, heuristic, time)
                if found == True:
                    return f, True
                if f < next_bound:
                    next_bound = f
                path.pop()
        return next_bound, False
    
    start[2] = heuristic(None, start, graph)
    path = [start]
    bound = start[2]
    time = TimeComplexity()
    while True: 
        f, found = search(path, graph, 0, bound, heuristic, time)
        if found == True:
            path = list(map(lambda x : x[0], path))
            return (time, path[1:])
        if f == float('inf'):
            print("not found")
            return (time, list(map(lambda x : x[0], path)))
        bound = f

algo_dic = {
    "uniform_cost" : uniform_cost_search,
    "greedy" : gready_search,
    "a_star" : a_star,
    "ida" : ida_search
}


