
def draw_path(graph, parents, start):
    counter = 0
    # print(start in parents, start)
    # for k in parents:
    #     print(k)
    while (parents[start] != None):
        counter += 1
        # graph.draw(start)
        start = parents[start]
    print('{:<41} {}'.format("Number of moves required to transition", counter))

def print_result(graph, opened_set, general_set):
# def print_result(graph, came_from):
    # opened_set = came_from[0]
    # general_set = came_from[1]
    draw_path(graph, general_set, graph.final_state)
    print('{:<41} {}'.format("Total number of states in the opened set", opened_set.len()))
    print('{:<41} {}'.format("Maximum number of states in memory", len(general_set)))