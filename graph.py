from queue import *
import sys

class Graph:
    def __init__(self, initial_state, size, zero_pos):
        self.state = initial_state
        self.size = size
        self.len = size * size
        self.zero = zero_pos
        self.final_state = self.__get_final_state()

    def check_valid(self, state):
        return state == self.final_state

    def __get_final_state(self):
        size = self.size
        dist = size
        state = [0] * self.len
        numb = 1
        current_cell = 0
        while dist > 0:
            for i in range(current_cell, current_cell+dist):
                state[i] = numb
                numb +=1
            dist -=1
            current_cell = i + size
            if numb == self.len:
                break
            for i in range(current_cell, current_cell + dist*size, size): 
                state[i] = numb
                numb +=1
            if numb == self.len:
                break
            current_cell = i -1
            for i in range(current_cell, current_cell - dist, -1):
                state[i] = numb
                numb +=1
            if numb == self.len:
                break
            current_cell = i - size
            dist -=1
            for i in range(current_cell, current_cell - dist*size, -size):
                state[i] = numb
                numb +=1
            if numb == self.len:
                break
            current_cell = i + 1
        return tuple(state)

    def __swap(self, to, zero, state):
        l = list(state)
        l[to], l[zero] = l[zero], l[to]
        return [tuple(l), to, None]

    def draw(self, node):
        i = 0
        while i < len(node):
            if (((i + 1) % self.size)):
                print (node[i], end = ' ')
            else:
                print(node[i])
            i += 1
        print('')

    def neighbors(self, state):
        zero = state[1]
        neighbors = []
        if (zero // self.size):
            neighbors.append(self.__swap(zero - self.size, zero, state[0]))
        if (zero // self.size != self.size - 1):
            neighbors.append(self.__swap(zero + self.size, zero, state[0]))
        if (zero % self.size):
            neighbors.append(self.__swap(zero - 1, zero, state[0]))
        if (zero % self.size != self.size - 1):
            neighbors.append(self.__swap(zero + 1, zero, state[0]))
        return neighbors
