import pygame 

pygame.init()

WHITE = (255,255,255)


screen = pygame.display.set_mode((800,600))
select_piece_page = pygame.image.load("assets/select_piece_page.png")
navigator = pygame.image.load("assets/navigator.png")
navigator = pygame.transform.scale(navigator,(210,210))
navigator_pos =[(180,90),(405,90),(180,300),(405,300)]


font = pygame.font.Font('assets/Font/PixelifySans-Regular.ttf', 120)


num_position = [(250,120) , (475,120) , (255,330) ,(475,330)]
colors = ['red' , 'green' ,"blue" , "yellow"]
index = 0 
playersColor = []
picked_color = colors[index]



def navigation(i = index , e = "") :
    global picked_color
    global index

    if e.type == pygame.KEYDOWN:

        if e.key == pygame.K_RETURN:
            if picked_color in playersColor:
                playersColor.remove(picked_color)              
            else:
                playersColor.append(picked_color)
        
        elif e.key == pygame.K_SPACE:
            return "done"

        elif e.key == pygame.K_DOWN or e.key == pygame.K_UP:
            match i:
                case 0 : i = 2 
                case 1 : i = 3
                case 2 : i = 0
                case 3 : i = 1
        elif e.key == pygame.K_RIGHT or e.key == pygame.K_LEFT:
            match i:
                case 0 : i = 1
                case 2 : i = 3
                case 1 : i = 0
                case 3 : i = 2

        
        picked_color = colors[i]
        index = i
        return picked_color


def selection():
    while True:
        screen.blit(select_piece_page,(0,0))
        screen.blit(navigator,navigator_pos[index])
        

        for color in playersColor:
            num = playersColor.index(color)+1
            position_index = colors.index(color)
            position = num_position[position_index]
            text = font.render(f"{num}" , True , WHITE)
            screen.blit(text , position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
            finished = navigation(index , event)
            if finished == "done":
                return playersColor

            
        pygame.display.flip()

    

