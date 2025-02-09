from gameSetup import selection
import copy


playersColor = selection()

# Player pieces
pieces = {
    "red": {"r1":{"pos":(1, 1),"play":False},"r2":{"pos":(1, 4),"play":False},"r3":{"pos":(4, 4),"play":False},"r4":{"pos":(4, 1),"play":False}},
    "blue": {"b1":{"pos":(1, 13),"play":False},"b2":{"pos":(4, 13),"play":False},"b3":{"pos":(1, 10),"play":False},"b4":{"pos":(4, 10),"play":False}},
    "green": {"g1":{"pos":(13, 1),"play":False},"g2":{"pos":(10, 1),"play":False},"g3":{"pos":(10, 4),"play":False},"g4":{"pos":(13, 4),"play":False}},
    "yellow": {"y1":{"pos":(13, 13),"play":False},"y2":{"pos":(10, 10),"play":False},"y3":{"pos":(13, 10),"play":False},"y4":{"pos":(10, 13),"play":False}}
}




player_pieces={}

# make players list for games
for color in pieces.keys():
    if color in playersColor:
        player_pieces[color] = copy.deepcopy(pieces[color])



# make list of position of Tokens
def tokens():
    tokensPos = {}
    for color in player_pieces:
        for piece in player_pieces[color]:
            tokensPos[piece] = copy.deepcopy(player_pieces[color][piece]["pos"])
    return tokensPos

firstPosition = tokens()


# player Start Cell
startCell ={
    "red":    (1,6), 
    "blue":   (6, 13),
    "green":  (8,1),
    "yellow": (13 ,8)
}


# player End Cell

endHouse = {
    "red": [(j,7) for j in range(0,6) ], 
    "blue":   [(7, i) for i in range(14,8,-1)],
    "green":  [(7,i) for i in range(0 ,6)],
    "yellow": [(j ,7) for j in range(14,8,-1)]
}

