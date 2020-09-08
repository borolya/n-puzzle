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

def gaschnig(priveous_state, state, graph):
    dist = 0
    candidate = list(state[0])
    while not candidate == list(graph.final_state):
        zero_i = candidate.index(0)
        if zero_i == graph.final_state.index(0):
            for i in range(graph.len):
                if candidate[i] != graph.final_state[i]:
                    candidate[i], candidate[zero_i] = candidate[zero_i], candidate[i]
                    break
        else:
            i = candidate.index(graph.final_state[zero_i])
            candidate[zero_i], candidate[i] = candidate[i], candidate[zero_i]
        dist += 1
    state[2] = dist
    return (dist)



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
    'gaschnig' : gaschnig,
    'hamming' : hamming,
    'linear_conflict' : linear_conflict,
    'manhattan' : manhattan_distance,
} 