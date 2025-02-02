from player import player_pieces , pieces
from boardAndPiece import main_path , draw_board , draw_pieces
from player import  endHouse , startCell , tokens , firstPosition
# Move a piece

tokensPos= tokens()

def move_piece(color, dice_roll,piece_name = "r1"):
    
    global tokensPos                
    otherPiece = list(player_pieces[color].keys())
    otherPiece.remove(piece_name)
    
    if player_pieces[color]:
        piece =player_pieces[color][piece_name]["pos"]  # Get the first piece of the player

        if piece in main_path:  # Check if the piece is on the main path

            current_index = main_path.index(piece)  # Find current position in the main path
            new_index = (current_index + dice_roll) % len(main_path)  # Calculate new position
            end_point = main_path[new_index]
            
            if move_statments(color,end_point,piece_name):
                
                countor = 0
                for repeat in range(dice_roll):
                    piece =player_pieces[color][piece_name]["pos"]
                    if piece == endHouse[color][0] :
                        rem_dice = dice_roll - countor
                        if rem_dice > 0:
                            move_piece_house(color,rem_dice,piece_name)
                            break
                        elif rem_dice <= 0 :
                            break
                                    
                    current_index = main_path.index(piece)  # Find current position in the main path
                    new_index = (current_index + 1) % len(main_path)  # Calculate new position

                    tokensPos = tokens()
                    
                    player_pieces[color][piece_name]["pos"] = main_path[new_index]  # Update the piece position
                    countor += 1
                return True
            else:
                return False

        elif piece in endHouse[color]:
            move_piece_house(color , dice_roll,piece_name)

        else:
            tokensPos = tokens()
                # If the piece is not on the main path, move it to the starting position
            if dice_roll == 6:
                
                for token in tokensPos:
                    print(f"------------------------{token}")
                    print(tokensPos[token],"--------tokens")
                    print(startCell[color],"--------start")         
                    if tokensPos[token] == startCell[color] and token in otherPiece:
                        tokensPos = tokens()
                        return False
                    
                    elif tokensPos[token] == startCell[color] and piece_name != token and (not token in otherPiece):
                        print("salam")
                        if 'b' in token: temp = 'blue'
                        elif 'r' in token: temp = 'red'
                        elif 'g' in token: temp = 'green'
                        elif 'y' in token: temp = 'yellow'
                        player_pieces[temp][token]["pos"] = firstPosition[token]
                        player_pieces[color][piece_name]["pos"] = startCell[color]
                                     
                        tokensPos = tokens()
                        return True
                else:
                    player_pieces[color][piece_name]["pos"] = startCell[color]
                    tokensPos = tokens()
                    return True
            else :
                return True
                pass
                    # change turn

    
def move_piece_house(color , dice_roll , piece_name):
    tokensPos = tokens()
    piece = tokensPos[piece_name]
    index = endHouse[color].index(piece)
    new_index = index + dice_roll
    if new_index >= 6 :
        return False
    else:
        print("somthing")
        end_point = endHouse[color][new_index] 
        if move_statments(color , end_point , piece_name):
            player_pieces[color][piece_name]["pos"] = end_point
        else:
            return


    

def move_statments(color , piece , piece_name):
    otherPiece = list(player_pieces[color].keys())
    tokensPos = tokens()
    for token in tokensPos:

        if piece == tokensPos[token] and (token in otherPiece) and piece_name != token :
            return False #returning for it moves or not
            
        elif piece == tokensPos[token] and (not (token in otherPiece)) and piece_name != token:
            if 'b' in token: temp = 'blue'
            elif 'r' in token: temp = 'red'
            elif 'g' in token: temp = 'green'
            elif 'y' in token: temp = 'yellow'
            player_pieces[temp][token]["pos"] = firstPosition[token]
            return  True 

    else:
        return True
            
            