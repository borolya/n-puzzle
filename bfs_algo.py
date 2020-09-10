from queue import *
import draw as draw
import heuristic as h

# def calc_priority(heuristic, state, graph):
#     priority = 0
#     if "md" in heuristic:
#         priority += h.manhattan_distance(state, graph)
#     if "lc" in heuristic:
#         priority += h.linear_conflict(state, graph)
#     if "lc" in heuristic:
#         priority += h.linear_conflict(state, graph)


def uniform_cost_search(graph, start): # = breadth_first_search == dejstra
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    level = {} #cost
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

def gready_search(graph, start, heuristic): #start = (initial_state, zero_index, cost)
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
                priority = heuristic(current, next, graph)# + h.linear_conflict(next, graph) #???
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
            #if (next[0] not in came_from):
                priority = heuristic(current, next, graph) + current_level #+ h.linear_conflict(next, graph)
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
            path = map(lambda x : x[0], path)
            return (time, path[1:])
        if f == float('inf'):
            print("not found")
            return (time, map(lambda x : x[0], path))
        bound = f

algo_dic = {
    "uniform_cost" : uniform_cost_search,
    "greedy" : gready_search,
    "a_star" : a_star,
    "ida" : ida_search
}

# def create_mask(graph):
#     mask = {}
#     state = graph.final_state
#     mask[0] = state[0]
#     counter = 1
#     while (counter < graph.size):
#         mask[graph.size * counter] = state[graph.size * counter]
#         mask[counter] = state[counter]
#         counter += 1
#     return mask

# def gready_search(graph, start, heuristic):
#     print("\ngready_search:\n")
#     frontier = PriorityQueue()
#     frontier.put(start, 0)
#     came_from = {}
#     came_from[start[0]] = None
#     final_states = []
    
#     while not frontier.empty():
#         current = frontier.get()
#         # print("current", current)
#         # graph.draw(current[0])

#         if (graph.check_valid(current)):
#             graph.draw(current[0])
#             graph.final_state = current[0]
#             break

#         for next in graph.neighbors(current):
#             if next[0] not in came_from:
#                 priority = heuristic(next, graph)
#                 # print(priority)
#                 frontier.put(next, priority)
#                 came_from[next[0]] = current[0]
#             # else: print(None, next)
#         # print("\n\n\n")
#     return [frontier, came_from, current[0]]

