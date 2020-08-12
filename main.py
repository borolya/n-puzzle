import graph as g
import bfs as bfs
import sys
import re
#import heuristic as h
#import draw as draw
import argparse

parser = argparse.ArgumentParser(description=' ', add_help=True, conflict_handler='resolve')
parser.add_argument('--file', action='store', type = str, dest='file_name', help='file name')
parser.add_argument('-n', '--input', action='store_true', dest='input', help='to use input format')
parser.add_argument('-gen', '--generate', action='store', type=int, dest='gen_numb', help='print number to generate size of board')
parser.add_argument('-f', choices=('manhattan', 'linear_conflict'), default = 'manhattan')
parser.add_argument('-a', choices=('a_star', 'ida*', 'greedy', 'uniform_cost'), default = 'a_star')

#parser.add_argument('-ida*', action='store_true', help='to use ida*')
#parser.add_argument('-g', action='store_true', help='to use greedy search')
#parser.add_argument('-g', action='store_true')
#parser.add_argument('-uc', action='store_true', help='to use uniform_cost search')
args = parser.parse_args(sys.argv[1::])

#heuristic_dic = {
#    'manhattan' : h.manhattan,
#    'linear_conflict' : h.linear_conflict
#    }

alg_dic = {
    'a_star' : bfs.a_star,
    'ida*' : bfs.ida
    }    

initial_state_array = []
print(args)

if (args.file_name != None or args.input == True):
    #in function
    if (args.file_name != None):
        try:
            fd = open(args.file_name)
        except IOError as e:
            print(e)
            sys.exit(1)
    else:
        fd = sys.stdin
    size = None
    while True:
        try:
            line = fd.readline() #check valid
            if line == '':
                fd.close()
                break
            line = re.split(r'\s*#|\s*\n', line)[0]
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
                        all(c.isdigit() and int(c)>=0 and int(c)<size*size for c in content) and
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
zero_index = initial_state.index(0)
graph = g.Graph(initial_state, size, zero_index)
print "We are starting frome this instance and using " + args.a + " search algorithm",
if (args.a != "uniform_cost"):
    print ("with " + args.f + " heuristic function")
else:
    print('\n')
graph.draw(initial_state)

alg_dic[args.a]()








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

