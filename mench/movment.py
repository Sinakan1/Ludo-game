from player import player_pieces
from boardAndPiece import main_path , draw_board , draw_pieces
from player import endCell , endHouse , startCell
# Move a piece
def move_piece(color, dice_roll,piece_name = "r1"):
    if player_pieces[color]:
        piece =player_pieces[color][piece_name]["pos"]  # Get the first piece of the player
        if piece in main_path:  # Check if the piece is on the main path
            countor = 0
            for repeat in range(dice_roll):
                piece =player_pieces[color][piece_name]["pos"]
                if piece == endCell[color] :
                    rem_dice = dice_roll - countor
                    if rem_dice > 0:
                        move_piece_house(color,rem_dice,piece_name)
                        break
                    elif rem_dice <= 0 :
                        break                   
                current_index = main_path.index(piece)  # Find current position in the main path
                new_index = (current_index + 1) % len(main_path)  # Calculate new position
                
                player_pieces[color][piece_name]["pos"] = main_path[new_index]  # Update the piece position
                countor += 1

        elif piece in endHouse[color]:
            move_piece_house(color , dice_roll,piece_name)

        else:
             # If the piece is not on the main path, move it to the starting position
            if dice_roll == 6:
                player_pieces[color][piece_name]["pos"] = startCell[color]
                pass
                # player_pieces[color][0] = start_pos
            else :
                pass
                # change turn
            

def move_piece_house(color , dice_roll , piece_name):
    match color :
        case 'red':
            for dice in range(dice_roll):
                piece =player_pieces[color][piece_name]["pos"]
                if piece == endHouse[color][-1]:
                    break
                new_piece = (piece[0]+1 , piece[1])
                player_pieces[color][piece_name]["pos"] = new_piece

        case 'green':
            for dice in range(dice_roll):
                piece =player_pieces[color][piece_name]["pos"]["pos"]
                if piece == endHouse[color][-1]:
                    break
                new_piece = (piece[0] , piece[1]+1)
                player_pieces[color][piece_name]["pos"] = new_piece

        case 'yellow':
            for dice in range(dice_roll):
                piece =player_pieces[color][piece_name]["pos"]
                if piece == endHouse[color][-1]:
                    break
                new_piece = (piece[0]-1 , piece[1])
                player_pieces[color][piece_name]["pos"] = new_piece
        
        case 'blue':
            for dice in range(dice_roll):
                piece =player_pieces[color][piece_name]["pos"]
                if piece == endHouse[color][-1]:
                    break
                new_piece = (piece[0] , piece[1]-1)
                player_pieces[color][piece_name]["pos"] = new_piece