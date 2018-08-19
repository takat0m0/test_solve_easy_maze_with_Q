# -*- coding:utf-8 -*-

import os
import sys

class PlayBack(object):
    def __init__(self, state, action, next_state, reward):
        self.state = state
        self.action = action
        self.next_state = next_state
        self.reward = reward

class PlayBacks(object):
    def __init__(self):
        self.__data = []
        
    def append(self, pb):
        self.__data.append(pb)
    
    def __len__(self):
        return len(self.__data)
    
    def __iter__(self):
        return self.__data.__iter__()
