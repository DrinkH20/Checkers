import pygame
scrnw, scrnh = 500, 500
WIN = pygame.display.set_mode((scrnw, scrnh))
pygame.display.set_caption("Red's turn")
pieces = []
white_pieces = [(50, 100), (150, 100), (250, 100), (350, 100),
                (0, 50), (100, 50), (200, 50), (300, 50),
                (50, 0), (150, 0), (250, 0), (350, 0)]

black_pieces = [(0, 250), (100, 250),  (200, 250), (300, 250),
                (50, 300), (150, 300), (250, 300), (350, 300),
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
current_team = white_pieces
part1 = 0
part2 = 0
imbedded_list = []
force_end_turn = 0


def move(re1, re2, item):
    global turn
    global current_piece
    global possible_moves
    global jumped
    global opposite_team_pieces
    global part1
    global part2
    global part
    global current_team
    if turn == '1':
        part1 = 0
        dist = white_pieces[item]
        # This part is for jumping over a black player
        if abs(dist[0] - re1) == 100:
            pygame.display.set_caption("Red's turn")
            # This is where it keeps it our turn and tells that we've jumped over someone
            turn = '1'
            jumped = 1
            # This is where is deletes the jumped player
            replace = black_pieces.index((re1 + (dist[0] - re1)/2, re2 + (dist[1] - re2)/2))
            black_pieces.remove(black_pieces[replace])
            current_piece = [(), (), (), "1"]

            # This is where it moves the player
            white_pieces[item] = re1, re2
            opposite_team_pieces = black_pieces
            current_team = white_pieces

        #     Notice: I didn't reset the current_player, this is because we want to keep are player's turn going
        else:
            pygame.display.set_caption("Black's turn")

            # This is for moving 1 space at the beginning of ur turn
            if jumped == 0:
                # This is saying that we didn't jump over someone and that its the black's turn
                jumped = 0
                turn = '-1'
                # Making it so that there is no piece selected to move
                current_piece = [(), (), (), ""]
                white_pieces[item] = re1, re2

            # This is for moving when 1 space after jumping, so u can't move 1 space :P
            else:
                jumped = 0
                turn = '-1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Black's turn")
            opposite_team_pieces = white_pieces
            current_team = black_pieces

    elif turn == '-1':
        part2 = 0
        dist = black_pieces[item]
        if abs(dist[0] - re1) == 100:
            jumped = 1
            pygame.display.set_caption("Black's turn")
            turn = '-1'
            replace = white_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
            white_pieces.remove(white_pieces[replace])
            black_pieces[item] = re1, re2
            current_piece = [(), (), (), "-1"]
            opposite_team_pieces = white_pieces
            current_team = black_pieces

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
            current_team = white_pieces
        part = 0


def can_move(place, moves):
    global part
    global part1
    global part2
    if moves == '1':
        part = part1
    else:
        part = part2

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

    if moves == '1':
        part1 = part
    elif moves == '-1':
        part2 = part


piece_movement = [(0, 1),
                  ((Dist, 0), (0, Dist)),
                  ((1, 2), (2, 1), (-1, 2), (1, -2), (-1, -2), (-2, -1), (-2, 1), (2, -1)),
                  ((Dist, Dist), (Dist, -Dist), (-Dist, Dist), (-Dist, -Dist)),
                  ((1, -1), (1, 0), (1, 1), (0, 1), (0, 0), (-1, -1), (-1, 0), (-1, 0)),
                  ((Dist, Dist), (Dist, -Dist), (-Dist, Dist), (-Dist, -Dist), (Dist, 0), (0, Dist))]


def screen_draw(w, h, re=0, repeat=0, repeat2=0):
    global part
    global current_piece
    global part1
    global part2
    part = 0
    part1 = 0
    part2 = 0

    while repeat < w:
        while repeat2 < h:
            if white_pieces.__contains__((repeat, repeat2)):
                if current_piece[1] == (repeat, repeat2):
                    pygame.draw.rect(WIN, (250, 80, 80), (repeat + 50, repeat2 + 50, 45, 45))
                else:
                    pygame.draw.rect(WIN, (250, 50, 50), (repeat + 50, repeat2 + 50, 45, 45))

                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '1':
                        current_piece = white_pieces.index((repeat, repeat2)), (repeat, repeat2)
            elif black_pieces.__contains__((repeat, repeat2)):
                if current_piece[1] == (repeat, repeat2):
                    pygame.draw.rect(WIN, (20, 20, 20), (repeat + 50, repeat2 + 50, 45, 45))
                else:
                    pygame.draw.rect(WIN, (30, 30, 30), (repeat + 50, repeat2 + 50, 45, 45))

                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '-1':
                        current_piece = black_pieces.index((repeat, repeat2)), (repeat, repeat2)

            else:
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    can_move((repeat, repeat2), turn)
                    pygame.draw.rect(WIN, (100, 100, 100), (repeat + 50, repeat2 + 50, 45, 45))
                    if click[0]:
                        if possible_moves.__contains__((repeat, repeat2)) and current_piece[0] != ():
                            move(repeat, repeat2, current_piece[0])
                else:
                    if repeat % 20 == repeat2 % 20:
                        pygame.draw.rect(WIN, (110, 110, 110), (repeat + 50, repeat2 + 50, 45, 45))
                    else:
                        if possible_moves.__contains__((repeat, repeat2)):
                            pygame.draw.rect(WIN, (90, 90, 90), (repeat + 50, repeat2 + 50, 45, 45))
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


def no_more_moves(possible, current):
    global turn
    global imbedded_list
    global force_end_turn
    global opposite_team_pieces
    global jumped
    global imbedded_list
    global current_team
    global current_piece
    force_end_turn = 0
    # This is computing whether u can move anymore after jumping someone
    if jumped >= 5:
        for i in possible:
            imbedded_list = current[1]
            if imbedded_list != () and i != ():
                # This is calculating the distance between u and the possible moves,
                # so if it = 100 then that means u can go again.
                if abs(int(imbedded_list[0]) - int(i[0])) == 100:
                    force_end_turn = 1
        # If it doesn't find any that = 100 then u can't go again
        if force_end_turn == 0:
            jumped = 0
            if opposite_team_pieces == white_pieces:
                opposite_team_pieces = black_pieces
                current_team = white_pieces
                pygame.display.set_caption("Red's turn")
                turn = '1'
                current_piece = [(), (), (), '1']
            elif opposite_team_pieces == black_pieces:
                opposite_team_pieces = white_pieces
                current_team = black_pieces
                pygame.display.set_caption("Black's turn")
                turn = '-1'
                current_piece = [(), (), (), '-1']


while run:
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    WIN.fill((10, 10, 10))
    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    screen_draw(scrnw - 100, scrnh - 100)
    pygame.display.update()
    ground = []

    if jumped > 0:
        jumped += 1

    no_more_moves(possible_moves, current_piece)

    if current_piece[0:2] == [(), ()]:
        possible_moves = [(), (), (), ()]

    for event in pygame.event.get():
        if event.type == pygame.QUIT or len(black_pieces) == 0 or len(white_pieces) == 0:
            run = False
            break
pygame.quit()
