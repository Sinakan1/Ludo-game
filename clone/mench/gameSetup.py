player_quantity = input("How many player will played (2 - 4) : ")
color = ['red' , 'green' , "yellow" , "blue"]
playersColor = []

for num in range(1 , int(player_quantity)+1):
    colorPicked = input(f"which color is player {num} {color} : ").lower()
    playersColor.append(colorPicked)
    color.remove(colorPicked)
