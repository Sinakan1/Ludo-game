from player import player_pieces, firstPosition , tokens


def do_move(color , piece , piece_name , kill = False):
    otherPiece = list(player_pieces[color].keys())
    tokensPos = tokens()
    for token in tokensPos:

        if piece == tokensPos[token] and (token in otherPiece) and piece_name != token :
            return False #returning for it moves or not
            
        elif piece == tokensPos[token] and (not (token in otherPiece)) and piece_name != token and kill:
           returnHome(token) 
        elif piece == tokensPos[token] and (not (token in otherPiece)) and piece_name != token and not kill:
            return "yes" 
    else:
        return True
    
def returnHome(token):
    if 'b' in token: temp = 'blue'
    elif 'r' in token: temp = 'red'
    elif 'g' in token: temp = 'green'
    elif 'y' in token: temp = 'yellow'
    player_pieces[temp][token]["pos"] = firstPosition[token]
    return  True 