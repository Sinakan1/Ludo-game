from player import player_pieces
from main import colorTurn

BLACK = (0,0,0)
inList = []
endList = []
mainList = list(player_pieces[colorTurn].keys())
# select peice
def selectPiece(colorTurn , dice_value):
    for piece in player_pieces[colorTurn]:
            if player_pieces[colorTurn][piece]["play"]:
                inList.append(piece)
            else:
                endList.append(piece)

    