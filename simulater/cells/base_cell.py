# -*- coding:utf-8 -*-

import os
import sys

class BaseCell(object):
    def __init__(self, can_enter, reward, symbol):
        self.reward = reward
        self.can_enter = can_enter
        self.symbol = symbol
        
    def printing(self):
        print(self.symbol)
        
    def __call__(self):
        return self.can_enter, self.reward
