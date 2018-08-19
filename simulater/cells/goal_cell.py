# -*- coding:utf-8 -*-

import os
import sys
from .base_cell import BaseCell

class GoalCell(BaseCell):
    def __init__(self):
        super().__init__(can_enter = True,
                         reward = 50.0,
                         symbol = 'g')
