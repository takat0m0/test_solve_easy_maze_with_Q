# -*- coding:utf-8 -*-

import os
import sys
from .base_cell import BaseCell

class Wall(BaseCell):
    def __init__(self):
        super().__init__(can_enter = False,
                         reward = -1.0,
                         symbol = 'x')

if __name__ == '__main__':
    w = Wall()
    w.printing()
