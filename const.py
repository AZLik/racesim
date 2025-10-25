import configparser

config = configparser.ConfigParser()
config.read('config.ini')

FPS = int(config['Default']['FPS'])
DISTANCE = int(config['Default']['distance']) if 'distance' in config['Default'] else -1

BASHIN_COEFF = 2.5

class stats_names:
    SPEED = 1
    STAMINA = 2
    POWER = 3
    GUTS = 4
    WIT = 5

class moods:
    AWFUL = -2
    SAD = -1
    NORMAL = 0
    GOOD = 1
    GREAT = 2

class track_types:
    TURF = 0
    DIRT = 1

class ground_condition_names:
    FIRM = 0
    GOOD = 1
    SOFT = 2
    HEAVY = 3

class letters:
    G = 0
    F = 1
    E = 2
    D = 3
    C = 4
    B = 5
    A = 6
    S = 7
    SS = 8

class proficiencies:
    DISTANCE = 0
    GROUND = 1
    
class strategy_names:
    FRONT_RUNNER = 0
    PACE_CHASER = 1
    LATE_SURGER = 2
    END_CLOSER = 3
    OONIGE = 4

class race_phase_names:
    EARLY_RACE = 0
    MID_RACE = 1
    LATE_RACE = 2
    LAST_SPURT = 3

class distance_names:
    SPRINT = 0
    MILE = 1
    MEDIUM = 2
    LONG = 3

ITERABLE_STATS_NAMES = [stats_names.SPEED, stats_names.STAMINA, stats_names.POWER, stats_names.GUTS, stats_names.WIT]
ITERABLE_GROUND_CONDITION_NAMES = [ground_condition_names.FIRM,
                                   ground_condition_names.GOOD,
                                   ground_condition_names.SOFT,
                                   ground_condition_names.HEAVY]
ITERABLE_MOOD_NAMES = [moods.AWFUL, moods.SAD, moods.NORMAL, moods.GOOD, moods.GREAT]

BASE_STATS_MOOD_MODIFIER = 0.2
SINGLE_MODE_MODIFIER = 400
STARTING_SPEED = 3

STRATEGY_PROFICIENCY_MODIFIER = {}
STRATEGY_PROFICIENCY_MODIFIER[letters.S] = float(config['Strategy Proficiency Modifier']['S'])
STRATEGY_PROFICIENCY_MODIFIER[letters.A] = float(config['Strategy Proficiency Modifier']['A'])
STRATEGY_PROFICIENCY_MODIFIER[letters.B] = float(config['Strategy Proficiency Modifier']['B'])
STRATEGY_PROFICIENCY_MODIFIER[letters.C] = float(config['Strategy Proficiency Modifier']['C'])
STRATEGY_PROFICIENCY_MODIFIER[letters.D] = float(config['Strategy Proficiency Modifier']['D'])
STRATEGY_PROFICIENCY_MODIFIER[letters.E] = float(config['Strategy Proficiency Modifier']['E'])
STRATEGY_PROFICIENCY_MODIFIER[letters.F] = float(config['Strategy Proficiency Modifier']['F'])
STRATEGY_PROFICIENCY_MODIFIER[letters.G] = float(config['Strategy Proficiency Modifier']['G'])

GROUND_MODIFIER = []
GROUND_MODIFIER[stats_names.SPEED] = {ground_condition_names.FIRM: {track_types.DIRT: 0, track_types.TURF: 0},
                                      ground_condition_names.GOOD: {track_types.DIRT: 0, track_types.TURF: 0},
                                      ground_condition_names.SOFT: {track_types.DIRT: 0, track_types.TURF: 0},
                                      ground_condition_names.HEAVY: {track_types.DIRT: -50, track_types.TURF: -50}}

GROUND_MODIFIER[stats_names.POWER] = {ground_condition_names.FIRM: {track_types.DIRT: -100, track_types.TURF: 0},
                                      ground_condition_names.GOOD: {track_types.DIRT: -50, track_types.TURF: -50},
                                      ground_condition_names.SOFT: {track_types.DIRT: -100, track_types.TURF: -50},
                                      ground_condition_names.HEAVY: {track_types.DIRT: -100, track_types.TURF: -50}}

STRATEGY_PHASE_COEFFICIENT = []
STRATEGY_PHASE_COEFFICIENT[race_phase_names.EARLY_RACE] = {strategy_names.FRONT_RUNNER:1.0,
                                                           strategy_names.PACE_CHASER:0.978,
                                                           strategy_names.LATE_SURGER:0.938,
                                                           strategy_names.END_CLOSER:0.931,
                                                           strategy_names.OONIGE:1.063}
STRATEGY_PHASE_COEFFICIENT[race_phase_names.MID_RACE] = {strategy_names.FRONT_RUNNER:0.98,
                                                           strategy_names.PACE_CHASER:0.991,
                                                           strategy_names.LATE_SURGER:0.998,
                                                           strategy_names.END_CLOSER:1.0,
                                                           strategy_names.OONIGE:0.962}
STRATEGY_PHASE_COEFFICIENT[race_phase_names.LATE_RACE] = {strategy_names.FRONT_RUNNER:0.962,
                                                           strategy_names.PACE_CHASER:0.975,
                                                           strategy_names.LATE_SURGER:0.994,
                                                           strategy_names.END_CLOSER:1.0,
                                                           strategy_names.OONIGE:0.95}
STRATEGY_PHASE_COEFFICIENT[race_phase_names.LAST_SPURT] = {strategy_names.FRONT_RUNNER:0.962,
                                                           strategy_names.PACE_CHASER:0.975,
                                                           strategy_names.LATE_SURGER:0.994,
                                                           strategy_names.END_CLOSER:1.0,
                                                           strategy_names.OONIGE:0.95}

DISTANCE_PROFICIENCY_MODIFIER = {letters.S: 1.05, letters.A: 1.0, letters.B: 0.9,
                                 letters.C: 0.8, letters.D: 0.6, letters.E: 0.4,
                                 letters.F: 0.2, letters.G: 0.1}

BASE_ACCELERATION = 0.0006
BASE_ACCELERATION_UPHILL = 0.0004
START_DASH_MODIFIER = 24

DISTANCE_PROFICIENCY_MODIFIER_ACCELERATION = {letters.S: 1.0, letters.A: 1.0, letters.B: 1.0,
                                              letters.C: 1.0, letters.D: 1.0, letters.E: 0.6,
                                              letters.F: 0.5, letters.G: 0.4}
GROUND_TYPE_PROFICIENCY_MODIFIER = {letters.S: 1.05, letters.A: 1.0, letters.B: 0.9,
                                    letters.C: 0.8, letters.D: 0.7, letters.E: 0.5,
                                    letters.F: 0.3, letters.G: 0.1}

POSITION_KEEP_COEFFICIENT = {}