
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

# def print_result(graph, came_from):
    # opened_set = came_from[0]
    # general_set = came_from[1]
    
    