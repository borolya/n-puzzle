
def draw_path(graph, parents, del_track):
    if type(parents) == dict:
        current = graph.final_state
        path = []
        while current != graph.state:
            path.append(current)
            current = parents[current]
        path.reverse()
    else:
        path = parents
    if del_track == False:
        for state in path:
            graph.draw(state)
    print('{:<41} {}'.format("Number of moves required to transition", len(path)))

    
    