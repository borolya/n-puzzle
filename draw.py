
def draw_path(graph, parents):
    if type(parents) == dict:
        current = graph.final_state
        path = []
        while current != graph.state:
            path.append(current)
            current = parents[current]
        path.append(current)
        path.reverse()
    else:
        path = parents
    for state in path:
        graph.draw(state)
    print('{:<41} {}'.format("Number of moves required to transition", len(path) - 1))

# def print_result(graph, came_from):
    # opened_set = came_from[0]
    # general_set = came_from[1]
    
    