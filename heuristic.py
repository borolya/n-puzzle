from graph import *

# def match_priority(state, graph):  for stright order 
#     dist = len(state[0])
#     counter = 1
#     while (counter < len(state[0]) - 1):
#         if (state[0][counter - 1] == counter):
#             dist -= 1
#         counter += 1
#     return dist

def hamming(state, graph): 
    final_state = graph.final_state
    dist = 0
    for pos in range(len(state[0])):
        if (state[0][pos] != 0 and state[0][pos] != final_state[pos]):
            dist +=1
    return dist

def linear_conflict(state, graph):
    conflicts = 0
    size = grph.size
    for i in range(0, graph.size):
        conflicts += line_conflict(state[0][i * size : (i + 1) * size], i, lambda x: graph.final_state.index(x) // graph.size, graph.final_state.index(x) % graph.size) + 
            line_conflict(state[0][i::size], i, lambda x: graph.final_state.index(x) % graph.size, graph.final_state.index(x) // graph.size)
    return conflicts

def line_conflict(line, i, dest):
    conflicts = 0
    for j, u in enumerate(line):
        if u == 0:
            continue
        x, y = dest(u)
        if i != x:
            continue

        for k in range(j + 1, len(line))
            v = line[k]
            if v == 0:
                continue
            tx, ty = dest(v)
            if tx == x and ty == y:
                conflicts +=2
    return (conflicts)


# def linear_conflict_old(state, graph): 
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

#     graph.draw(state[0])
#     graph.draw(graph.final_state)
#     print(dist)
#     return dist + manhattan_distance(state, graph)



def manhattan_distance(state, graph): 
    dist = 0
    for pos1 in range(0, graph.len):
        if graph.final_state[pos1] == 0:
            continue
        pos2 = state[0].index(graph.final_state[pos1])
        x1, y1 = pos1 % graph.size, pos1 // graph.size
        x2, y2 = pos2 % graph.size, pos2 // graph.size
        dist1 = abs(x1 - x2)
        dist2 = abs(y1 - y2)
        dist += dist1 + dist2
   
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