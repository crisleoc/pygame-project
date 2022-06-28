import Puzzle.settings.main as settings
import random
import pygame
import io
from urllib.request import urlopen


def isGameOver(board, size):
    assert isinstance(size, int)
    num_cells = size * size
    for i in range(num_cells-1):
        if board[i] != i:
            return False
    return True


def moveR(board, blank_cell_idx, num_cols):
    if blank_cell_idx % num_cols == 0:
        return blank_cell_idx
    board[blank_cell_idx -
          1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-1]
    return blank_cell_idx - 1


def moveL(board, blank_cell_idx, num_cols):
    if (blank_cell_idx+1) % num_cols == 0:
        return blank_cell_idx
    board[blank_cell_idx +
          1], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+1]
    return blank_cell_idx + 1


def moveD(board, blank_cell_idx, num_cols):
    if blank_cell_idx < num_cols:
        return blank_cell_idx
    board[blank_cell_idx-num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx-num_cols]
    return blank_cell_idx - num_cols


def moveU(board, blank_cell_idx, num_rows, num_cols):
    if blank_cell_idx >= (num_rows-1) * num_cols:
        return blank_cell_idx
    board[blank_cell_idx+num_cols], board[blank_cell_idx] = board[blank_cell_idx], board[blank_cell_idx+num_cols]
    return blank_cell_idx + num_cols


def CreateBoard(num_rows, num_cols, num_cells):
    board = []
    for i in range(num_cells):
        board.append(i)

    blank_cell_idx = num_cells - 1
    board[blank_cell_idx] = -1
    for i in range(settings.RANDNUM):

        direction = random.randint(0, 3)
        if direction == 0:
            blank_cell_idx = moveL(board, blank_cell_idx, num_cols)
        elif direction == 1:
            blank_cell_idx = moveR(board, blank_cell_idx, num_cols)
        elif direction == 2:
            blank_cell_idx = moveU(board, blank_cell_idx, num_rows, num_cols)
        elif direction == 3:
            blank_cell_idx = moveD(board, blank_cell_idx, num_cols)
    return board, blank_cell_idx


def ShowEndInterface(screen, width, height):
    screen.fill(settings.BACKGROUND_COLOR)
    font = pygame.font.Font(None, width//15)
    text_1 = font.render('Good Job! You Won!', True, settings.BLACK)
    text_2 = font.render('Press space to play again', True, settings.BLACK)
    text_3 = font.render('Press scape to exit', True, settings.BLACK)
    rect_1 = text_1.get_rect()
    rect_2 = text_2.get_rect()
    rect_3 = text_3.get_rect()
    rect_1.midtop = (width/2, height/2.6)
    rect_2.midtop = (width/2, height/2)
    rect_3.midtop = (width/2, height/1.8)
    screen.blit(text_1, rect_1)
    screen.blit(text_2, rect_2)
    screen.blit(text_3, rect_3)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return True
        pygame.display.update()


def ShowStartInterface(screen, width, height):
    screen.fill(settings.BACKGROUND_COLOR)
    tfont = pygame.font.Font(None, width//4)
    cfont = pygame.font.Font(None, width//20)
    title = tfont.render('Puzzle', True, settings.BLACK)
    content1 = cfont.render(
        'Presiona las siguientes teclas para ajustar la dificultad', True, settings.BLACK)
    content2 = cfont.render('H - 5x5, M - 4x4, L - 3x3', True, settings.BLACK)
    trect = title.get_rect()
    trect.midtop = (width/2, height/3)
    crect1 = content1.get_rect()
    crect1.midtop = (width/2, height/2)
    crect2 = content2.get_rect()
    crect2.midtop = (width/2, height/1.8)
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('l'):
                    return 3
                elif event.key == ord('m'):
                    return 4
                elif event.key == ord('h'):
                    return 5
        pygame.display.update()


def runGame():
    clock = pygame.time.Clock()

    image_url = f"https://source.unsplash.com/{settings.SCREENSIZE[0]}x{settings.SCREENSIZE[1]}/"
    image_str = urlopen(image_url).read()
    image_file = io.BytesIO(image_str)

    game_img_used = pygame.image.load(image_file)
    game_img_used = pygame.transform.scale(game_img_used, settings.SCREENSIZE)
    game_img_used_rect = game_img_used.get_rect()

    screen = pygame.display.set_mode(settings.SCREENSIZE)
    size = ShowStartInterface(
        screen, game_img_used_rect.width, game_img_used_rect.height)
    assert isinstance(size, int)
    num_rows, num_cols = size, size
    num_cells = size * size
    cell_width = game_img_used_rect.width // num_cols
    cell_height = game_img_used_rect.height // num_rows
    while True:
        game_board, blank_cell_idx = CreateBoard(num_rows, num_cols, num_cells)
        if not isGameOver(game_board, size):
            break
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    blank_cell_idx = moveL(
                        game_board, blank_cell_idx, num_cols)
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    blank_cell_idx = moveR(
                        game_board, blank_cell_idx, num_cols)
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    blank_cell_idx = moveU(
                        game_board, blank_cell_idx, num_rows, num_cols)
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    blank_cell_idx = moveD(
                        game_board, blank_cell_idx, num_cols)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                x_pos = x // cell_width
                y_pos = y // cell_height
                idx = x_pos + y_pos * num_cols
                if idx == blank_cell_idx-1:
                    blank_cell_idx = moveR(
                        game_board, blank_cell_idx, num_cols)
                elif idx == blank_cell_idx+1:
                    blank_cell_idx = moveL(
                        game_board, blank_cell_idx, num_cols)
                elif idx == blank_cell_idx+num_cols:
                    blank_cell_idx = moveU(
                        game_board, blank_cell_idx, num_rows, num_cols)
                elif idx == blank_cell_idx-num_cols:
                    blank_cell_idx = moveD(
                        game_board, blank_cell_idx, num_cols)
        if isGameOver(game_board, size):
            game_board[blank_cell_idx] = num_cells - 1
            is_running = False
        screen.fill(settings.BACKGROUND_COLOR)
        for i in range(num_cells):
            if game_board[i] == -1:
                continue
            x_pos = i // num_cols
            y_pos = i % num_cols
            rect = pygame.Rect(y_pos*cell_width, x_pos *
                               cell_height, cell_width, cell_height)
            img_area = pygame.Rect((game_board[i] % num_cols)*cell_width,
                                   (game_board[i]//num_cols)*cell_height, cell_width, cell_height)
            screen.blit(game_img_used, rect, img_area)
        for i in range(num_cols+1):
            pygame.draw.line(screen, settings.BLACK, (i*cell_width, 0),
                             (i*cell_width, game_img_used_rect.height))
        for i in range(num_rows+1):
            pygame.draw.line(screen, settings.BLACK, (0, i*cell_height),
                             (game_img_used_rect.width, i*cell_height))
        pygame.display.update()
        clock.tick(settings.FPS)
    ShowEndInterface(screen, game_img_used_rect.width,
                     game_img_used_rect.height)


def main():
    pygame.init()
    pygame.display.set_caption('Puzzle')
    continue_game = True
    while continue_game == True:
        runGame()
    else:
        pygame.quit()
