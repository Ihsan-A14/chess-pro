import chess as engine
import pygame

def make_move(move):
    for i in valid:
        if move == i:
            chess.move(move)
            return True
    else:
        blink_red(move)
        print("Invalid Move")
        return False

def blink_red(move):
    global blink_now
    time = pygame.time.get_ticks()
    if blink_now is not None and time - blink_now < 1000:
        row, col = move[0]
        if chess.board_arr[row][col] == '--':
            return 
        pygame.draw.rect(screen, "#ff0000", (20 + 85 * col, 20 + 85 * row, 85, 85))
        time = pygame.time.get_ticks()
    else:
        blink_now = None
    return

    

# Dictionary that matches name of chess piece with its image
piece_img = {}
for i in ['br', 'bn', 'bb', 'bq', 'bk','bp', 'wr', 'wn', 'wb', 'wq', 'wk','wp']:
    image = pygame.image.load("./images/"+ i + ".png")
    image = pygame.transform.scale(image, (85, 85))
    piece_img[i] = image


board_coord = []
blink_now = None

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

chess = engine.BoardRep()

#tuple to store current squares that was selected
select_sqr = ()
# List stores initial and final position of the movement of piece
player_sqr = []

# Boolean to check if player's move have been completed. Resets after each completion of move done by player
move_made = False

# Pre generates all the valid moves
valid = chess.valid_moves()

# Boolean to indicate if the game is over or not - only by checking if its checkmate or stalemate
game_over = False

while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # If the board is in a checkmate or stalemate position then program crashes
    if chess.checkmate == True or chess.stalemate == True:
        game_over = True

    board = chess.board_arr

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 == 0:
                pygame.draw.rect(screen, "#B68E65", (20 + 85 * i, 20 + 85 * j, 85, 85))
                board_coord.append([20 + 85 * i, 20 + 85 * j])
            else:
                pygame.draw.rect(screen, "#966F33", (20 + 85 * i, 20 + 85 * j, 85, 85))
                board_coord.append([20 + 85 * i, 20 + 85 * j])

    for i in range(8):
        for j in range(8):
            if board[i][j] == '--':
                continue
            screen.blit(piece_img[board[i][j]], (20 + 85 * j, 20 + 85 * i))


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            blink_now = pygame.time.get_ticks()
            x, y = event.pos
            if x < 20 or x > 700 or y < 20 or y > 700:
                continue
            col = x // 85
            row = y // 85
            if (row, col) == select_sqr:
                select_sqr = ()
                player_sqr = []
                continue
            select_sqr = (row, col)
            player_sqr.append(select_sqr)
            print(player_sqr)
    
    if len(player_sqr) == 2:
        move_made = make_move(player_sqr)
        print(move_made)
        if move_made == True:
            valid = chess.valid_moves()
        move_made = False
        player_sqr = []

    if game_over == True:
        # When game finishes a translucent screen overlay with the text showing Game over
        dim_surface = pygame.Surface((720, 720))
        dim_surface.fill(pygame.Color("#000000"))
        dim_surface.set_alpha(150)
        screen.blit(dim_surface, (0, 0))
        
        
        font = pygame.font.SysFont("Times New Roman", 72, True, True)
        text = font.render('Game Over', 0, pygame.Color("white"))
        screen.blit(text, (210, 310))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()