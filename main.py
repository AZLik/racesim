import numpy as np
import random as rd
import time
from const import *
from racer import *
from track import *

class Simulator():
    def __init__(self, track, racers, strategies):
        self.track = track
        self.racers = racers
        
        self.distance_per_section = track.distance / 24
        
        self.early_race_thresh = 0
        self.mid_race_thresh = np.floor(self.distance_per_section * 4)
        self.late_race_thresh = np.floor(self.distance_per_section * 16)
        self.last_spurt_thresh = np.floor(self.distance_per_section * 20)

        self.track.Set_ground_condition(rd.choice(ITERABLE_GROUND_CONDITION_NAMES))
        self.track_info = self.track.Generate_info()

        for racer in racers:
            racer.Generate_adjusted_stats(self.track_info)
    
    def Generate_weather(self):
        pass

    def Generate_racer_objects(self):
        pass
    
    def run():
        working = True
        while working:
            time.sleep(1/FPS)