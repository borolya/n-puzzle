import graph as g
import bfs_algo as bfs
import sys

import parser as pr
import heuristic as h
import draw as draw
import argparse

parser = argparse.ArgumentParser(description=' ', add_help=True, conflict_handler='resolve')
parser.add_argument('-f', '--file', action='store', type = str, dest='file_name', help='file name')
parser.add_argument('-n', '--input', action='store_true', dest='input', help='to use input format')
parser.add_argument('-t', '--track', action='store_true', dest='track', help='to show answer track')
parser.add_argument('-h', '--heuristic', choices=('hamming', 'manhattan', 'gaschnig', 'linear_conflict'), default = 'manhattan')
parser.add_argument('-a', '--algorithm', choices=('a_star', 'ida', 'greedy', 'uniform_cost'), default = 'a_star')

args = parser.parse_args(sys.argv[1::])
initial_state, size = pr.get_input(args)
zero_index = initial_state.index(0)
graph = g.Graph(initial_state, size, zero_index)

print "We use " + args.algorithm + " search algorithm",
if (args.algorithm != "uniform_cost"):
    print ("with " + args.heuristic + " heuristic function\n")
    opened_set, general_set = bfs.algo_dic[args.algorithm](graph, [initial_state, zero_index, 0], h.heuristic_dic[args.heuristic])
else:
    print('\n')
    opened_set, general_set = bfs.algo_dic["uniform_cost"](graph, [initial_state, zero_index])

if (not graph.final_state in general_set):
     print('unsolvable state')
elif args.track:
    draw.draw_path(graph, general_set)
print('{:<41} {}'.format("Total number of states ever selected in the opened set (time)", opened_set.get_total_size()))
print('{:<41} {}'.format("Maximum number of states in memory", len(general_set)))


    #in function
#print(initial_state)








# if (args.file_name != None):
# try:
# fd = open(args.file_name)
# try:
# content = fd.read()
# content = re.sub(r'(?m)#.*\n?', '\n', content).split() #what is mean (?m)
# if content[0].isdigit() and int(content[0]) > 0:
# size = int(content[0])
# else:
# print("parsing: invalid size")
# sys.exit(1)
# #parsing content
# except Exception as e:
# print(e)
# finally:
# fd.close()
# except IOError:
# print("there is no '{0}' file name".format(args.file_name))
# elif (args.input == True):
# while True:
# if ()

# print(initial_state)


#print argsstr

