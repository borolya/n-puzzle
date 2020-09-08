
def draw_path(graph, parents):
    current = graph.final_state
    path = []
    while current != graph.state:
        path.append(current)
        current = parents[current]
    path.reverse()
    for state in path:
        graph.draw(state)
    print('{:<41} {}'.format("Number of moves required to transition", len(path)))

def print_result(graph, opened_set, general_set): #(graph, frontier, came_from)

    if (not graph.final_state in general_set):
        print('unsolvable state')
    else:
        draw_path(graph, general_set)
    print('{:<41} {}'.format("Total number of states ever selected in the opened set (time complexity)", opened_set.get_total_size()))
    print('{:<41} {}'.format("Maximum number of states in memory", len(general_set)))



# def print_result(graph, came_from):
    # opened_set = came_from[0]
    # general_set = came_from[1]
    
    