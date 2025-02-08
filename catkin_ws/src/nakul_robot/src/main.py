import requests
# import moveRobot
# from follow_display import robot
from centers import get_centers, get_pickup, get_capture, get_piece_ARTag_frame
from robotControl import getType
from findPiece import PieceFinder

URL = "https://nyc.cs.berkeley.edu/universal/v1/"

# Don't TOUCH Code blocks below!
######################### Get All Games #####################################
games_data = requests.get(url=URL).json()
for i in range(len(games_data)):
    print(i, " : ", games_data[i]['name'])
user_game = int(input("Pick the index of the game you want to play: "))

URL = URL + games_data[user_game]["id"] + '/'
#############################################################################


############## Get Variant and Starting Positon #############################
print(URL)
variants_data = requests.get(url=URL).json()['variants']
for j in range(len(variants_data)):
    print(j, " : ", variants_data[j]["id"])
user_variant = int(input("Pick the index of the variant you want to play: "))
variant = variants_data[user_variant]["id"]
URL = URL + variant + '/'
variants_data = requests.get(url=URL).json()
starting_position = variants_data["startPosition"]
##############################################################################


############################# Meta Data  #####################################
Static_URL = URL + "/positions/?p="
centers = get_centers()[games_data[user_game]["id"]]
###############################################################################

# Input: starting position string and ending position string
# Output: List of start coord and end cood [[x1, y1], [x2, y2]]


# def position_to_coord(start, end):
#     start_cord = None
#     end_cord = None

#     start = start[2:]
#     end = end[2:]

#     if len(start) != len(end):
#         print("error")
#         exit()
#     else:
#         for i in range(len(start)):
#             if start[i] != end[i]:
#                 if start[i] == "-":
#                     end_cord = centers[i]
#                 else:
#                     start_cord = centers[i]
#         return [start_cord, end_cord]


# Input: starting coord and ending coord
# Output: List of start position string and end position string ["RA_3_3_000", "RA_3_3_01230"]
# def coor_to_position(postion, start, end):
#     start_index = centers.index(start)
#     end_index = centers.index(end)

#     return postion[:start_index] + postion[end_index] + postion[start_index+1:end_index] + postion[start_index] + postion[end_index+1:]

###############################################################################

def pick_best_move(moves):
    position_values = {}
    for i in range(len(moves)):
        if moves[i]['moveValue'] not in position_values:
            position_values[moves[i]['moveValue']] = [moves[i]['autoguiMove']]
        else:
            position_values[moves[i]['moveValue']].append(moves[i]['autoguiMove'])

    if 'win' in position_values and len(position_values['win']) > 0:
        return position_values['win'][0]
    elif 'draw' in position_values and len(position_values['draw']) > 0:
        return position_values['draw'][0]
    elif 'lose' in position_values and len(position_values['lose']) > 0:
        return position_values['lose'][0]
    else:
        print('error: in pick_best_move')
        exit()

def pick_best_position(moves):
    position_values = {}
    for i in range(len(moves)):
        if moves[i]['moveValue'] not in position_values:
            position_values[moves[i]['moveValue']] = [moves[i]['position']]
        else:
            position_values[moves[i]['moveValue']].append(moves[i]['position'])

    if 'win' in position_values and len(position_values['win']) > 0:
        return position_values['win'][0]
    elif 'draw' in position_values and len(position_values['draw']) > 0:
        return position_values['draw'][0]
    elif 'lose' in position_values and len(position_values['lose']) > 0:
        return position_values['lose'][0]
    else:
        print('error: in pick_best_postion')
        exit()

################################################################################


# Work here!
Dynamic_URL = Static_URL + starting_position

# List of available moves from starting position
moves_data = requests.get(url=Dynamic_URL).json()['moves']

game = games_data[user_game]["id"]
gameType = getType(game)

tags = get_piece_ARTag_frame(game)
pieces = {}
for k, v in tags:
    pieces[k] = PieceFinder(k)

robotControl = gameType(game, centers, pieces, get_pickup(), get_capture())

A_turn = True
while (len(moves_data) > 0):
    if A_turn:
        move = pick_best_move(moves_data)
        new_position = pick_best_position(moves_data)
        move_coords = robotControl.processMove(move, [starting_position, new_position])

        print("A : ", move_coords)

        Dynamic_URL = Static_URL + new_position
        moves_data = requests.get(url=Dynamic_URL).json()['moves']
        starting_position = new_position
        A_turn = False
    else:
        move = pick_best_move(moves_data)
        new_position = pick_best_position(moves_data)
        move_coords = robotControl.processMove(move, [starting_position, new_position])

        print("B : ", move_coords)
        
        Dynamic_URL = Static_URL + new_position
        moves_data = requests.get(url=Dynamic_URL).json()['moves']
        starting_position = new_position
        A_turn = True
