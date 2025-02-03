from player import player_pieces

# check if the player has won   
def winning(color):
    for piece  in player_pieces[color]:
        if player_pieces[color][piece]["play"] == False:
            return False
    else:
        print(f"Player {color} has won")
        return True
    