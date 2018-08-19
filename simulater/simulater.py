# -*- codinf:utf-8 -*-

from .my_map import Map

class Simulater(object):
    def __init__(self, file_name):
        self.sim_map = Map(file_name)
        self.reset()
        
    def map_size(self):
        return self.sim_map.map_size()
    
    def printing(self):
        self.sim_map.printing(self.player_x, self.player_y)

    def end_episode(self):
        x = self.player_x == self.sim_map.goal_x
        y = self.player_y == self.sim_map.goal_y
        return x and y
    
    def reset(self):
        self.player_x = self.sim_map.start_x
        self.player_y = self.sim_map.start_y
        
    def get_current(self):
        return self.player_x, self.player_y
    
    def __call__(self, mode):
        tmp_x, tmp_y = self.player_x, self.player_y
        if mode == 'UP':
            tmp_y -= 1
        elif mode == 'DOWN':
            tmp_y += 1
        elif mode == 'LEFT':
            tmp_x -= 1
        elif mode == 'RIGHT':
            tmp_x += 1
        else:
            exit()
        can_enter, reward = self.sim_map.get_can_enter_reward(tmp_x, tmp_y)
        if can_enter:
            self.player_x, self.player_y = tmp_x, tmp_y
        return reward
    
if __name__ == '__main__':
    sim = Simulater('default.txt')
    sim.printing()
    sim('LEFT')
    sim.printing()
    sim('DOWN')
    sim.printing()    
    sim('RIGHT')
    sim.printing()
    sim('UP')
    sim.printing()
    sim('RIGHT')
    sim.printing()
    sim('RIGHT')
    sim.printing()    
    sim('RIGHT')
    sim.printing()    
