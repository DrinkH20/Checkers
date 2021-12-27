import pygame
scrnw, scrnh = 500, 500
WIN = pygame.display.set_mode((scrnw, scrnh))
pygame.display.set_caption("Red's turn")
pieces = []
white_pieces = [(0, 50), (100, 50), (200, 50), (300, 50),
                (50, 0), (150, 0), (250, 0), (350, 0)]
black_pieces = [(50, 300), (150, 300), (250, 300), (350, 300),
                (0, 350), (100, 350),  (200, 350), (300, 350)]
Dist = 0
mx, my = pygame.mouse.get_pos()
run = True
click = 0
current_piece = [0, 0, 0, 0]
turn = "1"
possible_moves = [(), (), (), ()]
ground = []
part = 0
jumped = 0
still_goin = 0
opposite_team_pieces = black_pieces


def move(re1, re2, item):
    global turn
    global current_piece
    global possible_moves
    global jumped
    global opposite_team_pieces
    if turn == '1':
        dist = white_pieces[item]
        if abs(dist[0] - re1) == 100:
            jumped = 1
            pygame.display.set_caption("Red's turn")
            turn = '1'
            replace = black_pieces.index((re1 + (dist[0] - re1)/2, re2 + (dist[1] - re2)/2))
            black_pieces.remove(black_pieces[replace])
            print(jumped)
            white_pieces[item] = re1, re2
        else:
            if jumped == 0:
                jumped = 0
                turn = '-1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Black's turn")
                white_pieces[item] = re1, re2

            else:
                jumped = 0
                turn = '-1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Black's turn")
                print("problem")
        opposite_team_pieces = white_pieces

    elif turn == '-1':
        dist = black_pieces[item]
        if abs(dist[0] - re1) == 100:
            jumped = 1
            pygame.display.set_caption("Black's turn")
            turn = '-1'
            replace = white_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
            white_pieces.remove(white_pieces[replace])
            print(jumped)
            black_pieces[item] = re1, re2
        else:
            if jumped == 0:
                jumped = 0
                turn = '1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Red's turn")
                black_pieces[item] = re1, re2

            else:
                jumped = 0
                turn = '1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Red's turn")
        opposite_team_pieces = black_pieces


def can_move(place, moves):
    global part
    part = 0

    if current_piece.__contains__((place[0] + 50, place[1] + 50)):
        possible_moves[part] = place
        part += 1
    elif opposite_team_pieces.__contains__((place[0] + 50, place[1] + 50)):
        if current_piece.__contains__((place[0] + 100, place[1] + 100)):
            possible_moves[part] = place
            part += 1

    if current_piece.__contains__((place[0] - 50, place[1] + 50)):
        possible_moves[part] = place
        part += 1
    elif opposite_team_pieces.__contains__((place[0] - 50, place[1] + 50)):
        if current_piece.__contains__((place[0] - 100, place[1] + 100)):
            possible_moves[part] = place
            part += 1

    if current_piece.__contains__((place[0] - 50, place[1] - 50)):
        possible_moves[part] = place
        part += 1
    elif opposite_team_pieces.__contains__((place[0] - 50, place[1] - 50)):
        if current_piece.__contains__((place[0] - 100, place[1] - 100)):
            possible_moves[part] = place
            part += 1

    if current_piece.__contains__((int(place[0]) + 50, place[1] - 50)):
        possible_moves[part] = place
        part += 1
    elif opposite_team_pieces.__contains__((int(place[0]) + 50, place[1] - 50)):
        if current_piece.__contains__((int(place[0]) + 100, place[1] - 100)):
            possible_moves[part] = place
            part += 1


piece_movement = [(0, 1),
                  ((Dist, 0), (0, Dist)),
                  ((1, 2), (2, 1), (-1, 2), (1, -2), (-1, -2), (-2, -1), (-2, 1), (2, -1)),
                  ((Dist, Dist), (Dist, -Dist), (-Dist, Dist), (-Dist, -Dist)),
                  ((1, -1), (1, 0), (1, 1), (0, 1), (0, 0), (-1, -1), (-1, 0), (-1, 0)),
                  ((Dist, Dist), (Dist, -Dist), (-Dist, Dist), (-Dist, -Dist), (Dist, 0), (0, Dist))]


def screen_draw(w, h, re=0, repeat=0, repeat2=0):
    global part
    part = 0
    global current_piece

    while repeat < w:
        while repeat2 < h:
            if white_pieces.__contains__((repeat, repeat2)):
                pygame.draw.rect(WIN, (250, 50, 50), (repeat + 50, repeat2 + 50, 45, 45))
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '1':
                        current_piece = white_pieces.index((repeat, repeat2)), (repeat, repeat2)
            elif black_pieces.__contains__((repeat, repeat2)):
                pygame.draw.rect(WIN, (30, 30, 30), (repeat + 50, repeat2 + 50, 45, 45))
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '-1':
                        current_piece = black_pieces.index((repeat, repeat2)), (repeat, repeat2)

            else:
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    can_move((repeat, repeat2), turn)
                    pygame.draw.rect(WIN, (100, 150, 100), (repeat + 50, repeat2 + 50, 45, 45))
                    if click[0]:
                        if possible_moves.__contains__((repeat, repeat2)) and current_piece[0] != ():
                            print(current_piece)
                            move(repeat, repeat2, current_piece[0])
                else:
                    if repeat % 20 == repeat2 % 20:
                        pygame.draw.rect(WIN, (110, 110, 110), (repeat + 50, repeat2 + 50, 45, 45))
                    else:
                        pygame.draw.rect(WIN, (70, 70, 70), (repeat + 50, repeat2 + 50, 45, 45))
                        ground.append((repeat, repeat2))
                        can_move((repeat, repeat2), turn)

            repeat2 += 50
            re += 1

        repeat += 50
        repeat2 = 0
        re += 1
    if part < 3:
        while part < 3:
            part += 1
            possible_moves[part] = ()


while run:
    # dist_move(current_piece, possible_moves)
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    WIN.fill((10, 10, 10))
    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    screen_draw(scrnw - 100, scrnh - 100)
    pygame.display.update()
    ground = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
