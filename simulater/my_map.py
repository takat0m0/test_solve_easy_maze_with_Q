# -*- coding:utf-8 -*-

import os
import sys

from .cells import Wall, NormalCell, StartCell, GoalCell

class Map(object):
    def __init__(self, file_name):
        self.cells = []
        with open(file_name, 'r') as f:
            for l in f:
                tmp = l.strip()
                this_line = [self._chose_cell(_) for _ in tmp]
                self.cells.append(this_line)
        self.start_y, self.start_x = self.get_start_coord()
        self.goal_y, self.goal_x = self.get_goal_coord()

    def map_size(self):
        return len(self.cells[0]), len(self.cells)
    
    def get_can_enter_reward(self, x, y):
        return self.cells[y][x]()
    
    def get_start_coord(self):
        for i, this_line in enumerate(self.cells):
            for j, c in enumerate(this_line):
                if c.symbol == 's':
                    return i, j
                
    def get_goal_coord(self):
        for i, this_line in enumerate(self.cells):
            for j, c in enumerate(this_line):
                if c.symbol == 'g':
                    return i, j
                
    def printing(self, player_x, player_y):
        ret = []
        for this_line in self.cells:
            ret.append([_.symbol for _ in this_line])
        ret[player_y][player_x] = 'p'
        
        for this_line in ret:
            print(''.join(this_line))

    def _chose_cell(self, input_figure):
        if input_figure == ' ':
            return NormalCell()
        elif input_figure == 'x':
            return Wall()
        elif input_figure == 'g':
            return GoalCell()
        elif input_figure == 's':
            return StartCell()
        else:
            exit()

if __name__ == '__main__':
    m = Map('default.txt')
    m.printing(1, 1)
    print(m.get_can_enter_reward(0, 0))
    print(m.get_can_enter_reward(6, 1))
    print(m.get_can_enter_reward(1, 6))
    print(m.get_can_enter_reward(2, 6))        
