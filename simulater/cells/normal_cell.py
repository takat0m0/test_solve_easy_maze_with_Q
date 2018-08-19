# -*- coding:utf-8 -*-

import os
import sys
from .base_cell import BaseCell

class NormalCell(BaseCell):
    def __init__(self):
        super().__init__(can_enter = True,
                         reward = 0.0,
                         symbol = ' ')
