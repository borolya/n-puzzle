import sys
import re


def is_solvable(graph):
    def polarity(graph, final_state, state):
        invariant = 0
        for pos1 in range(0, graph.len):
            if state[pos1] == 0:
                continue
            for pos2 in range(pos1 + 1, graph.len):
                if state[pos2] == 0:
                    continue
                if final_state.index(state[pos1]) > final_state.index(state[pos2]):
                    invariant +=1
        return (invariant)
    
    if graph.size % 2 == 1:
        if polarity(graph, graph.final_state, graph.state) % 2 == 0:
            print(polarity(graph, graph.final_state, graph.state))
            return True
    elif (polarity(graph, graph.final_state, graph.state) 
            + graph.zero // graph.size) % 2 == 0:
            return True
    return False

def get_input(args):
    initial_state_array = []
    size = None
    if (args.file_name != None or args.input == True):
        if (args.file_name != None):
            try:
                fd = open(args.file_name)
            except IOError as e:
                print(e)
                sys.exit(1)
        else:
            fd = sys.stdin
        while True:
            try:
                line = fd.readline() #check valid
                if line == '':
                    fd.close()
                    break
                line = re.split(r'\s*#|\s*\n', line)[0]
                line = line.strip()
                if line != '':
                    if size == None:
                        if (not line.isdigit() or int(line) < 1):
                            print('parser: invalid size number')
                            sys.exit(1)
                        else:
                            size = int(line)
                    else:
                        content = re.split(r'\s+', line)
                        if (len(set(content)) == size and
                            all(c.isdigit() and int(c) >= 0 and int(c) < size*size for c in content) and
                            set(content) & set(initial_state_array) == set()):
                            initial_state_array.extend(content)
                        else:
                            print('parser: invalid cell')
                            sys.exit(1)
            except Exception as e:
                    print(e)
                    sys.exit(1)
        fd.close()
        initial_state = tuple(map(int, initial_state_array))
    else:
    #random generate by size 3
        initial_state = tuple(range(0, 9))
        size = 3
    return initial_state, size