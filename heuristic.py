from graph import *

# def match_priority(state, graph):  for stright order 
#     dist = len(state[0])
#     counter = 1
#     while (counter < len(state[0]) - 1):
#         if (state[0][counter - 1] == counter):
#             dist -= 1
#         counter += 1
#     return dist

def hamming(priveous_state, state, graph): 
    final_state = graph.final_state
    dist = 0
    for pos in range(len(state[0])):
        if (state[0][pos] != 0 and state[0][pos] != final_state[pos]):
            dist +=1
    return dist

def line_conflict(line, i, dest):
    conflicts = 0
    conflict_graph = {}
    for j, u in enumerate(line):
        if u == 0:
            continue
        dest_u = dest(u)
        if i != dest_u[0]:
            continue
        for k in range(j + 1, len(line)):
            v = line[k]
            if v == 0:
                continue
            dest_v = dest(v)
            if dest_v[0] == dest_u[0] and dest_v[1] <= dest_u[1]:
                u_degree, u_nbrs = conflict_graph.get(u) or (0, set())
                u_nbrs.add(v)
                conflict_graph[u] = (u_degree + 1, u_nbrs)
                v_degree, v_nbrs = conflict_graph.get(v) or (0, set())
                v_nbrs.add(u)
                conflict_graph[v] = (v_degree + 1, v_nbrs)
        while sum([v[0] for v in conflict_graph.values()]) > 0:
            popped = max(conflict_graph.keys(),
                        key=lambda k: conflict_graph[k][0])
            for neighbour in conflict_graph[popped][1]:
                degree, vs = conflict_graph[neighbour]
                vs.remove(popped)
                conflict_graph[neighbour] = (degree - 1, vs)
            conflict_graph.pop(popped)
            conflicts += 1
    return (conflicts * 2)

def linear_conflict(priveous_state, state, graph):
    size = graph.size
    dest_row = lambda x: [graph.final_state.index(x) // graph.size, graph.final_state.index(x) % graph.size]
    dest_column = lambda x: [graph.final_state.index(x) % graph.size, graph.final_state.index(x) // graph.size]
    if (priveous_state == None):
        dist = 0
        for i in range(0, graph.size):
            dist += line_conflict(state[0][i * size : (i + 1) * size], i, dest_row)
            dist += line_conflict(state[0][i::size], i, dest_column)
        dist += manhattan_distance(priveous_state, state, graph)
    else:
        dist = priveous_state[2]
        if priveous_state[1] % size == state[1] % size:
            dest = dest_row
            i = priveous_state[1] // size
            dist -= line_conflict(priveous_state[0][i * size : (i + 1) * size], i, dest) 
            dist += line_conflict(state[0][i * size : (i + 1) * size], i, dest)
            i = state[1] // size
            dist -= line_conflict(priveous_state[0][i * size : (i + 1) * size], i, dest) 
            dist += line_conflict(state[0][i * size : (i + 1) * size], i, dest)
        elif priveous_state[1] // size == state[1] // size:
            dest = dest_column
            i = priveous_state[1] % size
            dist -= line_conflict(priveous_state[0][i::size], i, dest) 
            dist += line_conflict(state[0][i::size], i, dest)
            i = state[1] % size
            dist -= line_conflict(priveous_state[0][i::size], i, dest) 
            dist += line_conflict(state[0][i::size], i, dest)
        #add manhattan_distance
        dist -= iteration_manhattan_distance(state[1], priveous_state, graph)
        dist += iteration_manhattan_distance(priveous_state[1], state, graph)
        state[2] = dist
    return dist

# def linear_conflict(priveous_state, state, graph): 
#     index_goal = {} #w
#     for val in range(0, graph.len):
#         index_goal[val] = graph.final_state.index(val) ##olya change to array 
#     # for (i, j) in index_goal.items():
#     #     print(i, j)
#     # graph.draw(state[0])
#     dist = 0

#     #linear_conflict
#     for i in range(0, graph.size):

#         pos_row = [j for j in range(i * graph.size, (i + 1) * graph.size)]
#         pos_row = list(filter(lambda x : 
#             index_goal[x] // graph.size == i, # check value (pos + 1) in row i
#             pos_row))
#         # print("i ", i, pos_row)

#         if len(pos_row) > 1:
#             for pos1 in pos_row:
#                 for pos2 in pos_row:                    
#                     if pos1 < pos2:
#                         if index_goal[pos1] > index_goal[pos2]:
#                             dist += 1
#                     elif pos1 > pos2:
#                         if index_goal[pos1] < index_goal[pos2]:
#                             dist += 1

#         pos_col = [j * graph.size + i for j in range(0, graph.size)]
#         pos_col = list(filter(lambda x : 
#             index_goal[x] % graph.size == i, # check value (pos + 1) in col i
#             pos_col))
#         # print("i ", i, pos_col)

#         if len(pos_col) > 1:
#             for pos1 in pos_col:
#                 for pos2 in pos_col:                    
#                     if pos1 < pos2:
#                         if index_goal[pos1] > index_goal[pos2]:
#                             dist += 1
#                     elif pos1 > pos2:
#                         if index_goal[pos1] < index_goal[pos2]:
#                             dist += 1

#     #corner_conflict 
#     # #olya// can be conflicted with linear conflict
#     # top_left_pos = 0
#     # if index_goal[top_left_pos + 1] != top_left_pos: # corner not match
#     #     near_pos = [top_left_pos + 1, top_left_pos + graph.size] 
#     #     corner_conflict = 0
#     #     if index_goal[near_pos[0] + 1] == near_pos[0]:
#     #         if state[0][near_pos[0]] // graph.size == 0:
#     #             corner_conflict += 1
#     #             # print("top_left_pos ", near_pos)
#     #             # exit()
        
#     #     if index_goal[near_pos[1] + 1] == near_pos[1]:
#     #         if state[0][near_pos[1]] % graph.size == 1:
#     #             corner_conflict += 1
        
#     #     if corner_conflict: dist += 2
        
#     # top_right_pos = graph.size - 1
#     # if index_goal[top_right_pos + 1] != top_right_pos:
#     #     near_pos = [top_right_pos - 1, top_right_pos + graph.size]
#     #     corner_conflict = 0
#     #     if index_goal[near_pos[0] + 1] == near_pos[0]:
#     #         if state[0][near_pos[0]] // graph.size == 0:
#     #             corner_conflict += 1
#     #             # print("top_right_pos ", near_pos)
#     #             # exit()
        
#     #     if index_goal[near_pos[1] + 1] == near_pos[1]:
#     #         if state[0][near_pos[1]] % graph.size == 0:
#     #             corner_conflict += 1
        
#     #     if corner_conflict: dist += 2
        
#     # bot_left_pos = graph.len - graph.size
#     # if index_goal[bot_left_pos + 1] != bot_left_pos:
#     #     near_pos = [bot_left_pos + 1, bot_left_pos - graph.size]
#     #     corner_conflict = 0
#     #     if index_goal[near_pos[0] + 1] == near_pos[0]:
#     #         if state[0][near_pos[0]] // graph.size == graph.size - 1:
#     #             corner_conflict += 1
#     #             # print("bot_left_pos ", near_pos)
#     #             # exit()
        
#     #     if index_goal[near_pos[1] + 1] == near_pos[1]:
#     #         if state[0][near_pos[1]] % graph.size == 1:
#     #             corner_conflict += 1
        
#     #     if corner_conflict: dist += 2
        
#     #last_move
#     #olya don't check
#     # last_move_row = graph.len - 1
#     # if index_goal[last_move_row] % graph.size != graph.size - 1: dist += 2 # not in last col
#     # last_move_cal = graph.len - graph.size
#     # if index_goal[last_move_row] // graph.size != graph.size - 1: dist += 2 # not in last row

#     return dist + manhattan_distance(priveous_state, state, graph)


def iteration_manhattan_distance(state_pos, state, graph):
    if state[0][state_pos] == 0:
        return 0
    final_pos = graph.final_state.index(state[0][state_pos])
    x1, y1 = state_pos % graph.size, state_pos // graph.size
    x2, y2 = final_pos % graph.size, final_pos // graph.size
    dist1 = abs(x1 - x2)
    dist2 = abs(y1 - y2)
    return dist1 + dist2

def manhattan_distance(priveous_state, state, graph): 
    if priveous_state == None:
        dist = 0
        for pos in range(graph.len):
            dist += iteration_manhattan_distance(pos, state, graph)
    else:
        dist = priveous_state[2]
        dist -= iteration_manhattan_distance(state[1], priveous_state, graph)
        dist += iteration_manhattan_distance(priveous_state[1], state, graph)

        state[2] = dist
    #olya I don't understand

    #if state[0] in graph.priority_states:    
        # print(graph.priority_states[state[0]])
        # return graph.priority_states[state[0]] - 100
    #   return dist - 100
    #else:
        #return dist
    return dist


heuristic_dic = {
    'hamming' : hamming,
    'linear_conflict' : linear_conflict,
    'manhattan' : manhattan_distance,
} 