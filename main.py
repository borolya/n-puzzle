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
parser.add_argument('-t', '--del_track', action='store_true', dest='del_track', help='not show the answer track')
parser.add_argument('-h', '--heuristic', choices=('hamming', 'manhattan', 'gaschnig', 'linear_conflict'), default = 'manhattan')
parser.add_argument('-a', '--algorithm', choices=('a_star', 'ida', 'greedy', 'uniform_cost'), default = 'a_star')

args = parser.parse_args(sys.argv[1::])
initial_state, size = pr.get_input(args)
zero_index = initial_state.index(0)
graph = g.Graph(initial_state, size, zero_index)

if pr.is_solvable(graph) == False:
    graph.draw(initial_state)
    print ("Unsolvable state")
    sys.exit()
print ("\nWe use " + args.algorithm + " search algorithm", end = ' ')
if (args.algorithm != "uniform_cost"):
    print ("with " + args.heuristic + " heuristic function\n")
    graph.draw(initial_state)
    opened_set, general_set = bfs.algo_dic[args.algorithm](graph, [initial_state, zero_index, 0], h.heuristic_dic[args.heuristic])
else:
    print('\n')
    graph.draw(initial_state)
    opened_set, general_set = bfs.algo_dic["uniform_cost"](graph, [initial_state, zero_index])

if (not graph.final_state in general_set):
     print('Unsolvable state')
elif args.del_track == False:
    draw.draw_path(graph, general_set)
print('{:<41} {}'.format("Total number of states ever selected in the opened set (time)", opened_set.get_total_size()))
print('{:<41} {}'.format("Maximum number of states in memory", len(general_set)))