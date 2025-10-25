from const import *
class Track:
    theshold_stats = {stats_names.SPEED, stats_names.GUTS}
    pass

class Track_info:
    def __init__(self, ground_type_init, threshold_stats_init):
        self.threshold_stats = threshold_stats_init
        self.ground_type = ground_type_init

    def Get_track_modifiers(self, racer_stats):
        track_modifiers = {}

        for stat in ITERABLE_STATS_NAMES:
            if stat not in self.threshold_stats:
                track_modifiers[stat] = 0

        for stat in self.threshold_stats:
            if racer_stats[stat] <= 300:
                track_modifiers[stat] = 0.05
            if 300 < racer_stats[stat] <= 600:
                track_modifiers[stat] = 0.1
            if 600 < racer_stats[stat] <= 900:
                track_modifiers[stat] = 0.15
            if 900 < racer_stats[stat]:
                track_modifiers[stat] = 0.2

        return track_modifiers
    