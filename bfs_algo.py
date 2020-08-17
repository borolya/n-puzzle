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

def uniform_cost_search(graph, start): #start = (state, zero_pos)
    print("\nuniform_cost_search:\n")
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
            graph.draw(current[0])
            break
        
        for next in graph.neighbors(current):
            if next[0] not in came_from:
                priority = current_level
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
                level[next[0]] = current_level
    draw.print_result(graph, frontier, came_from)

def gready_search(graph, start, heuristic):
    print("\ngready_search:\n")
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    came_from[start[0]] = None
    
    while not frontier.empty():
        current = frontier.get()

        if (graph.check_valid(current[0])):
            graph.draw(current[0])
            graph.final_state = current[0]
            break

        for next in graph.neighbors(current):
            if next[0] not in came_from:
                priority = heuristic(next, graph) + h.linear_conflict(next, graph)
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
    draw.print_result(graph, frontier, came_from)

def a_star(graph, start, heuristic):
    print("\nA*:\n")
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
            graph.draw(current[0])
            graph.final_state = current[0]
            break
        for next in graph.neighbors(current):
            # if (next[0] not in came_from or level[next[0]] > current_level):
            if (next[0] not in came_from):
                priority = heuristic(next, graph) + current_level + h.linear_conflict(next, graph)
                frontier.put(next, priority)
                came_from[next[0]] = current[0]
                level[next[0]] = current_level
    draw.print_result(graph, frontier, came_from)


def ida_search(graph, start, heuristic):
    print("ida search in developing")


algo_dic = {
    "uniform_cost" : uniform_cost_search,
    "greedy" : gready_search,
    "a_star" : a_star,
    "ida*" : ida_search
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

