def getType(gameId):
    types_of_games = {"Type4": ["3spot", "allqueenschess", "beeline", "change", "dao", "fivefieldkono", "foxandhounds", "hareandhounds", "jan", "joust"],
                      "Type6": ["dinododgem", "dodgem"]}
    types = {"Type1" : Type1, "Type2" : Type2, "Type3" : Type3, "Type4" : Type4, "Type5" : Type5,
            "Type6" : Type6, "Type7" : Type7, "Type8" : Type8, "Type9" : Type9, "Type10" : Type10,
            "Type11" : Type11}
    
    for gameType in types_of_games:
        if gameId in types_of_games[gameType]:
            return types[gameType]
    
    print("Error in RobotControl GameType!")
    return None

"""
Place
"""
class Type1:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None
    
"""
Captures
"""
class Type2:
    def __init__(self, centers, pickup, capture):
        self.centers = centers
        self.pickup = pickup
        self.capture = capture

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])

        start_cord = self.centers[start_index]
        end_cord = self.centers[end_index]

        start_position, end_position = positions
        if start_position[end_index] != end_position[end_index] and start_position[end_index] != '-':
            return [[end_cord, self.capture], [start_cord, end_cord]]
        return [start_cord, end_cord]
    
"""
Removal
"""
class Type3:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None
    
"""
Re-Arranger
"""
class Type4:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])

        start_cord = self.centers[start_index]
        end_cord = self.centers[end_index]
        return [start_cord, end_cord]

"""
Place + Re-Arranger
"""
class Type5:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None

"""
Re-Arranger + Removal
"""
class Type6:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])

        start_cord = self.centers[start_index]
        end_cord = self.centers[end_index]
        return [start_cord, end_cord]


"""
Re-Arranger + Capture
"""
class Type7:
    def __init__(self, centers, pickup, capture):
        self.centers = centers
        self.pickup = pickup
        self.capture = capture

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])

        start_cord = self.centers[start_index]
        end_cord = self.centers[end_index]

        start_position, end_position = positions
        if start_position[end_index] != end_position[end_index] and start_position[end_index] != '-':
            return [[end_cord, self.capture], [start_cord, end_cord]]
        return [start_cord, end_cord]

"""
Place + Re-Arranger + Removal
"""
class Type8:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None

"""
Place + Re-Arranger + Capture
"""
class Type9:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None
    
"""
Re-Arranger + Capture + Removal
"""
class Type10:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None

"""
Place + Re-Arranger + Capture + Removal
"""
class Type11:
    def __init__(self, centers):
        self.centers = centers

    def processMove(self, move, positions=None):
        move_string_split = move.split('_')
        start_index = int(move_string_split[1])
        end_index = int(move_string_split[2])
        return None
