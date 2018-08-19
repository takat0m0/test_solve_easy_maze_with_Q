# -*- coding:utf-8 -*-

import os
import sys

import numpy as np

from simulater import Simulater
from play_back import PlayBack, PlayBacks


COMMAND = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def get_max_command(target_dict):
    return max([(v,k) for k,v in target_dict.items()])[1]

def simplify(command):
    return command[0]

def print_Q(Q, x, y):
    ret = []
    for i in range(y):
        ret.append(['0' for _ in range(x)])
    for k in Q:
        ret[k[1]][k[0]] = simplify(get_max_command(Q[k]))
    for this_line in ret:
        print(''.join(this_line))

    
if __name__ == '__main__':
    # parameters
    file_name = 'default.txt'
    epoch_num = 1000
    max_trial = 5000
    gamma = 0.1
    alpha = 0.1
    epsilon = 0.5
    
    # make simulater
    sim = Simulater(file_name)

    # initialize Q value
    x, y = sim.map_size()
    Q = {}
    for i in range(x):
        for j in range(y):
            Q[(i, j)] = {_:np.random.normal() for _ in COMMAND}
            #Q[(i, j)] = {_:0.0 for _ in COMMAND}  

    # main
    minimum_pbs = None
    for epoch in range(epoch_num):
        sim.reset()
        this_pbs = PlayBacks()
        for i in range(max_trial):
            # get current
            current_x, current_y = sim.get_current()

            # select_command
            tmp_Q = Q[(current_x, current_y)]
            command = get_max_command(tmp_Q) if np.random.uniform() > epsilon else np.random.choice(COMMAND)
            current_value = tmp_Q[command]
            
            # reward
            reward = sim(command)

            # update
            next_x, next_y = sim.get_current()
            next_max_command = get_max_command(Q[(next_x, next_y)])
            next_value = Q[(next_x, next_y)][next_max_command]
            tmp_Q[command] += alpha * (reward + gamma * next_value - current_value)
            
            # play back
            this_pbs.append(PlayBack((current_x, current_y),
                                     command,
                                     (next_x, next_y),
                                     reward))
            # end check
            if sim.end_episode():
                print('find goal')
                epsilon *= 0.95
                if epsilon < 0.05:
                    epsilon = 0.05
                if minimum_pbs is None:
                    minimum_pbs = this_pbs
                elif len(minimum_pbs) > len(this_pbs):
                    minimum_pbs = this_pbs
                print(epsilon)
                break
        # update with minimum_pbs
        if minimum_pbs is not None:
            for pb in minimum_pbs:
                tmp_Q = Q[pb.state]
                current_value = tmp_Q[pb.action]
                next_Q = Q[pb.next_state]
                next_max_command = get_max_command(next_Q)
                next_value = next_Q[next_max_command]
                tmp_Q[pb.action] += alpha * (pb.reward + gamma * next_value - current_value)
        sim.printing()
        print('---')
        print_Q(Q, x, y)
        print('---')
