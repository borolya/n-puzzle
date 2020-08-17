from graph import *

def match_priority(state, graph):
    dist = len(state[0])
    counter = 1
    while (counter < len(state[0]) - 1):
        if (state[0][counter - 1] == counter):
            dist -= 1
        counter += 1
    return dist

def linear_conflict(state, graph):
    index_state = {}
    for val in range(0, graph.len):
        index_state[val] = state[0].index(val)
    # for (i, j) in index_state.items():
    #     print(i, j)
    # graph.draw(state[0])
    dist = 0

    #linear_conflict
    for i in range(0, graph.size):

        pos_row = [j for j in range(i * graph.size, (i + 1) * graph.size)]
        pos_row = list(filter(lambda x : 
            index_state[(x + 1) % graph.len] // graph.size == i, # check value (pos + 1) in row i
            pos_row))
        # print("i ", i, pos_row)

        if len(pos_row) > 1:
            for pos1 in pos_row:
                for pos2 in pos_row:                    
                    if pos1 < pos2:
                        if index_state[(pos1 + 1) % graph.len] > index_state[(pos2 + 1) % graph.len]:
                            dist += 1
                    elif pos1 > pos2:
                        if index_state[(pos1 + 1) % graph.len] < index_state[(pos2 + 1) % graph.len]:
                            dist += 1


        pos_col = [j * graph.size + i for j in range(0, graph.size)]
        pos_col = list(filter(lambda x : 
            index_state[(x + 1) % graph.len] % graph.size == i, # check value (pos + 1) in col i
            pos_col))
        # print("i ", i, pos_col)

        if len(pos_col) > 1:
            for pos1 in pos_col:
                for pos2 in pos_col:                    
                    if pos1 < pos2:
                        if index_state[(pos1 + 1) % graph.len] > index_state[(pos2 + 1) % graph.len]:
                            dist += 1
                    elif pos1 > pos2:
                        if index_state[(pos1 + 1) % graph.len] < index_state[(pos2 + 1) % graph.len]:
                            dist += 1

    #corner_conflict
    top_left_pos = 0
    if index_state[top_left_pos + 1] != top_left_pos: # corner not match
        near_pos = [top_left_pos + 1, top_left_pos + graph.size] 
        corner_conflict = 0
        if index_state[near_pos[0] + 1] == near_pos[0]:
            if state[0][near_pos[0]] // graph.size == 0:
                corner_conflict += 1
                # print("top_left_pos ", near_pos)
                # exit()
        
        if index_state[near_pos[1] + 1] == near_pos[1]:
            if state[0][near_pos[1]] % graph.size == 1:
                corner_conflict += 1
        
        if corner_conflict: dist += 2
        
    top_right_pos = graph.size - 1
    if index_state[top_right_pos + 1] != top_right_pos:
        near_pos = [top_right_pos - 1, top_right_pos + graph.size]
        corner_conflict = 0
        if index_state[near_pos[0] + 1] == near_pos[0]:
            if state[0][near_pos[0]] // graph.size == 0:
                corner_conflict += 1
                # print("top_right_pos ", near_pos)
                # exit()
        
        if index_state[near_pos[1] + 1] == near_pos[1]:
            if state[0][near_pos[1]] % graph.size == 0:
                corner_conflict += 1
        
        if corner_conflict: dist += 2
        
    bot_left_pos = graph.len - graph.size
    if index_state[bot_left_pos + 1] != bot_left_pos:
        near_pos = [bot_left_pos + 1, bot_left_pos - graph.size]
        corner_conflict = 0
        if index_state[near_pos[0] + 1] == near_pos[0]:
            if state[0][near_pos[0]] // graph.size == graph.size - 1:
                corner_conflict += 1
                # print("bot_left_pos ", near_pos)
                # exit()
        
        if index_state[near_pos[1] + 1] == near_pos[1]:
            if state[0][near_pos[1]] % graph.size == 1:
                corner_conflict += 1
        
        if corner_conflict: dist += 2
        
    #last_move
    last_move_row = graph.len - 1
    if index_state[last_move_row] % graph.size != graph.size - 1: dist += 2 # not in last col
    last_move_cal = graph.len - graph.size
    if index_state[last_move_row] // graph.size != graph.size - 1: dist += 2 # not in last row

    return dist

def manhattan_distance(state, graph):
    dist = 0
    for pos1 in range(0, graph.len):
        pos2 = state[0].index((pos1 + 1) % graph.len)
        x1, y1 = pos1 % graph.size, pos1 // graph.size
        x2, y2 = pos2 % graph.size, pos2 // graph.size
        dist1 = abs(x1 - x2)
        dist2 = abs(y1 - y2)
        dist += dist1 + dist2

    if state[0] in graph.priority_states:
        # print(graph.priority_states[state[0]])
        # return graph.priority_states[state[0]] - 100
        return dist - 100
    else:
        return dist
    # return dist


heuristic_dic = {
    'linear_conflict' : linear_conflict,
    'manhattan' : manhattan_distance,
} 