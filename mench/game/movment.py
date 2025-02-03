from player import player_pieces , pieces
from boardAndPiece import main_path
from player import  endHouse , startCell , tokens , firstPosition
from moveStates import do_move , returnHome
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
            state = do_move(color,end_point,piece_name,False)
            if state:
                for repeat in range(dice_roll):
                    piece =player_pieces[color][piece_name]["pos"]
                    if piece == endHouse[color][0] :
                        rem_dice = dice_roll - repeat
                        if rem_dice > 0:
                            move_piece_house(color,rem_dice,piece_name,repeat)
                            break
                        elif rem_dice <= 0 :
                            break
                                    
                    current_index = main_path.index(piece)  # Find current position in the main path
                    new_index = (current_index + 1) % len(main_path)  # Calculate new position
                    point = main_path[new_index]
                    state_temp = do_move(color,point,piece_name,False)
                    if state_temp == "yes" == state :
                        
                        do_move(color,end_point,piece_name,True)

                    player_pieces[color][piece_name]["pos"] = main_path[new_index]  # Update the piece position


                    tokensPos = tokens()
                return True
            else:
                return False

        elif piece in endHouse[color]:
            return move_piece_house(color , dice_roll,piece_name)

        else:
            tokensPos = tokens()
                # If the piece is not on the main path, move it to the starting position
            if dice_roll == 6:
                
                for token in tokensPos:        
                    if tokensPos[token] == startCell[color] and token in otherPiece:
                        tokensPos = tokens()
                        return False
                    
                    elif tokensPos[token] == startCell[color] and piece_name != token and (not token in otherPiece):
                        
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
    
    
def move_piece_house(color , dice_roll , piece_name, repeate = 0 ):
    tokensPos = tokens()
    Cell = endHouse[color][0]
    indexCell = main_path.index(Cell)
    piece = tokensPos[piece_name]
    index = endHouse[color].index(piece)
    new_index = index + dice_roll
    if new_index >= 6 :
        return False
    else:
        end_point = endHouse[color][new_index] 
        if do_move(color , end_point , piece_name , False):
            
            player_pieces[color][piece_name]["pos"] = end_point
            if index >= 2 or new_index >= 2 : 
                player_pieces[color][piece_name]["play"] = True
            return True
        elif (not do_move(color , end_point , piece_name , False)) and piece == endHouse[color][0]:
            
            player_pieces[color][piece_name]["pos"] = main_path[indexCell - repeate]
            return False
        else:
            return 


    




