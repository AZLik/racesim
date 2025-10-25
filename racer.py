import numpy as np
from const import *
from track import *

class Racer: #Long-Term Racer info
    def __init__(self, init_stats, init_proficiencies):
        self.raw_stats = init_stats
        self.proficiencies = init_proficiencies
        self.strategy = strategy_names.PACE_CHASER
    
    def Set_strategy(self, new_strategy):
        self.strategy = new_strategy
    

class InRaceRacer(): #Race-specific race info
    def __init__(self, racer, track_info, race_info):
        self.track_info = track_info
        self.raw_stats = racer.raw_stats
        self.proficiencies = racer.proficiencies
        self.race_info = race_info
        self.mood = race_info.mood
        self.strategy = race_info.strategy
        self.current_speed = STARTING_SPEED
        self.start_dash_over = 0

        self.base_stats = self.Get_base_stats()
        self.adjusted_stats = self.Get_adjusted_stats()

    def Get_base_stats(self):
        return self.raw_stats * (1 + BASE_STATS_MOOD_MODIFIER * self.mood)
    
    def Set_base_speed(self, distance):
        self.base_speed = 20. - (distance - 2000)/1000
    
    def Set_min_speed(self):
        self.min_speed = 0.85 * self.base_speed + np.sqrt(200. * self.adjusted_stats[stats_names.GUTS]) * 0.001

    def Get_adjusted_stats(self):
        base_stats = self.Get_base_stats()

        stats_track_modifiers = self.track_info.Get_track_modifiers()

        adjusted_stats = {}
        adjusted_stats[stats_names.SPEED] = base_stats[stats_names.SPEED] * (1 + stats_track_modifiers[stats_names.SPEED]) + GROUND_MODIFIER[stats_names.SPEED][self.track_info.ground_condition] + self.race_info.is_singlemode * SINGLE_MODE_MODIFIER
        adjusted_stats[stats_names.STAMINA] = base_stats[stats_names.STAMINA] + self.race_info.is_singlemode * SINGLE_MODE_MODIFIER
        adjusted_stats[stats_names.POWER] = base_stats[stats_names.POWER] + GROUND_MODIFIER[stats_names.POWER][self.track_info.ground_condition] + self.race_info.is_singlemode * SINGLE_MODE_MODIFIER
        adjusted_stats[stats_names.GUTS] = base_stats[stats_names.GUTS] + self.race_info.is_singlemode * SINGLE_MODE_MODIFIER
        adjusted_stats[stats_names.WIT] = base_stats[stats_names.WIT] * STRATEGY_PROFICIENCY_MODIFIER[self.proficiencies[self.strategy]] + self.race_info.is_singlemode * SINGLE_MODE_MODIFIER

        return adjusted_stats

    def Get_acceleration(self, is_uphill, race_phase):
        if is_uphill:
            base_accel = BASE_ACCELERATION_UPHILL
        else:
            base_accel = BASE_ACCELERATION
        if self.speed >= 0.85 * self.base_speed and not self.start_dash_over:
            start_dash = 0
            self.start_dash_over = 1
        else:
            start_dash = 1
        return base_accel * np.sqrt(500. * self.adjusted_stats[stats_names.POWER]) * STRATEGY_PHASE_COEFFICIENT[race_phase][self.strategy] * GROUND_TYPE_PROFICIENCY_MODIFIER[self.proficiencies[proficiencies.GROUND]]*DISTANCE_PROFICIENCY_MODIFIER_ACCELERATION[self.proficiencies[proficiencies.DISTANCE]] + start_dash * START_DASH_MODIFIER
    
    def Set_last_spurt_speed(self):
        self.last_spurt_speed = (self.base_target_speed + 0.01 * self.base_speed) * 1.05 + np.sqrt()
    
    def Update_taget_speed(self):
        pass

    def Set_base_target_speed(self, race_phase):
        self.base_target_speed = self.base_speed * STRATEGY_PHASE_COEFFICIENT[race_phase][self.strategy] + np.sqrt(500 * self.adjusted_stats[stats_names.SPEED]) * DISTANCE_PROFICIENCY_MODIFIER[race_phase][self.proficiencies[proficiencies.DISTANCE]] * 0.002
    
    def Update_base_speed(self, random_change):
        max_increase = self.adjusted_stats[stats_names.WIT]/5500 * np.log10(self.adjusted_stats[stats_names.WIT] * 0.1)
        self.base_speed *= (1 + max_increase - random_change)

    
        
        