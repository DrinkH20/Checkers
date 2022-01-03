import pygame
scrnw, scrnh = 500, 500
WIN = pygame.display.set_mode((scrnw, scrnh))
pygame.display.set_caption("Red's turn")
pieces = []
black_pieces = [(50, 100), (150, 100), (250, 100), (350, 100),
                (0, 50), (100, 50), (200, 50), (300, 50),
                (50, 0), (150, 0), (250, 0), (350, 0)]
black_kings = [0, 0, 0, 0,
               0, 0, 0, 0,
               0, 0, 0, 0]

red_pieces = [(0, 250), (100, 250), (200, 250), (300, 250),
              (50, 300), (150, 300), (250, 300), (350, 300),
              (0, 350), (100, 350), (200, 350), (300, 350)]
red_kings = [0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0]

Dist = 0
mx, my = pygame.mouse.get_pos()
run = True
click = 0
current_piece = [0, 0, 0, 0]
turn = "-1"
possible_moves = [(), (), (), ()]
ground = []
part = 0
jumped = 0
still_going = 0
opposite_team_pieces = black_pieces
current_team = red_pieces
part1 = 0
part2 = 0
embedded_list = []
force_end_turn = 0
moved = 0
color_black = (200, 50, 50)
color_black_select = (200, 80, 80)
color_black_king = (150, 50, 50)
color_red = (30, 30, 30)
color_red_select = (20, 20, 20)
color_red_king = (15, 15, 15)


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
    global moved
    if turn == '1':
        part1 = 0
        dist = black_pieces[item]
        # This part is for jumping over a black player
        calc = dist[1] - re2
        if abs(calc) == 100:
            if black_kings[item] == 0:
                if calc == -100:
                    pygame.display.set_caption("Black's turn")
                    # This is where it keeps it our turn and tells that we've jumped over someone
                    turn = '1'
                    jumped = 1
                    # This is where is deletes the jumped player
                    replace = red_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
                    red_pieces.pop(replace)
                    red_kings.pop(replace)
                    current_piece = [(), (), (), "1"]

                    # This is where it moves the player
                    black_pieces[item] = re1, re2
                    opposite_team_pieces = red_pieces
                    current_team = black_pieces
                    moved = 1
            else:
                pygame.display.set_caption("Black's turn")
                # This is where it keeps it our turn and tells that we've jumped over someone
                turn = '1'
                jumped = 1
                moved = 1

                # This is where is deletes the jumped player
                replace = red_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
                red_pieces.pop(replace)
                red_kings.pop(replace)
                current_piece = [(), (), (), "1"]

                # This is where it moves the player
                black_pieces[item] = re1, re2

                # This is where it sets the current team and opposing team
                opposite_team_pieces = red_pieces
                current_team = black_pieces

        else:
            # This is for moving 1 space at the beginning of ur turn
            if jumped == 0:
                if black_kings[item] == 0:
                    if calc == -50:
                        # This is saying that we didn't jump over someone and that its the black's turn
                        jumped = 0
                        turn = '-1'
                        moved = 0
                        # Making it so that there is no piece selected to move
                        current_piece = [(), (), (), ""]
                        black_pieces[item] = re1, re2
                        pygame.display.set_caption("Red's turn")

                else:
                    # This is saying that we didn't jump over someone and that its the black's turn
                    jumped = 0
                    turn = '-1'
                    moved = 0
                    # Making it so that there is no piece selected to move
                    current_piece = [(), (), (), ""]
                    black_pieces[item] = re1, re2
                    pygame.display.set_caption("Red's turn")

            # This is for moving when 1 space after jumping, so u can't move 1 space :P
            else:
                jumped = 0
                moved = 0
                turn = '-1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Red's turn")
            opposite_team_pieces = black_pieces
            current_team = red_pieces

        # This makes the piece a king if it gets to the other side
        if re2 == 350:
            black_kings[item] = 1

    elif turn == '-1':
        part2 = 0
        dist = red_pieces[item]
        calc = dist[1] - re2
        if abs(calc) == 100:
            if red_kings[item] == 0:
                if calc == 100:
                    jumped = 1
                    pygame.display.set_caption("Red's turn")
                    turn = '-1'
                    replace = black_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
                    black_pieces.pop(replace)
                    black_kings.pop(replace)
                    print(replace)
                    red_pieces[item] = re1, re2
                    current_piece = [(), (), (), "-1"]
                    opposite_team_pieces = black_pieces
                    current_team = red_pieces
                    moved = 1
            else:
                jumped = 1
                moved = 0
                pygame.display.set_caption("Red's turn")
                turn = '-1'
                replace = black_pieces.index((re1 + (dist[0] - re1) / 2, re2 + (dist[1] - re2) / 2))
                black_pieces.pop(replace)
                black_kings.pop(replace)
                print(replace)
                red_pieces[item] = re1, re2
                current_piece = [(), (), (), "-1"]
                opposite_team_pieces = black_pieces
                current_team = red_pieces

        else:
            if jumped == 0:
                if abs(calc) == 50:
                    if red_kings[item] == 0:
                        if calc == 50:
                            jumped = 0
                            turn = '1'
                            current_piece = [(), (), (), ""]
                            pygame.display.set_caption("Black's turn")
                            red_pieces[item] = re1, re2
                    else:
                        jumped = 0
                        turn = '1'
                        current_piece = [(), (), (), ""]
                        pygame.display.set_caption("Black's turn")
                        red_pieces[item] = re1, re2
            else:
                jumped = 0
                turn = '1'
                current_piece = [(), (), (), ""]
                pygame.display.set_caption("Black's turn")
            opposite_team_pieces = red_pieces
            current_team = black_pieces
        part = 0
        if re2 == 0:
            red_kings[item] = 1


# This is for finding if the piece is available to move to
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

            # This for making the black pieces
            if black_pieces.__contains__((repeat, repeat2)):
                if current_piece[1] == (repeat, repeat2):
                    # This highlights the player that is selected
                    pygame.draw.rect(WIN, color_red_select, (repeat + 50, repeat2 + 50, 45, 45))
                else:
                    # This makes the color of the kings and the regular players different
                    if black_kings[black_pieces.index((repeat, repeat2))] == 1:
                        pygame.draw.rect(WIN, color_red_king, (repeat + 50, repeat2 + 50, 45, 45))
                    else:
                        pygame.draw.rect(WIN, color_red, (repeat + 50, repeat2 + 50, 45, 45))

                # This calculates the position of the mouse then, calculates if its touching the block the loop is on
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '1':
                        current_piece = black_pieces.index((repeat, repeat2)), (repeat, repeat2)

            # This is for making the red pieces
            elif red_pieces.__contains__((repeat, repeat2)):
                if current_piece[1] == (repeat, repeat2):
                    pygame.draw.rect(WIN, color_black_select, (repeat + 50, repeat2 + 50, 45, 45))
                else:
                    if red_kings[red_pieces.index((repeat, repeat2))] == 1:
                        pygame.draw.rect(WIN, color_black_king, (repeat + 50, repeat2 + 50, 45, 45))
                    else:
                        pygame.draw.rect(WIN, color_black, (repeat + 50, repeat2 + 50, 45, 45))

                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    if click[0] and turn == '-1':
                        current_piece = red_pieces.index((repeat, repeat2)), (repeat, repeat2)

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
                            if moved > 1:

                                # This calculates if the current piece is a king, then colors the square accordingly
                                if turn == '1':
                                    dist = current_piece[1]
                                    if dist != ():
                                        if black_kings[black_pieces.index(dist)] == 0:
                                            if dist[1]-repeat2 != abs(dist[1]-repeat2):
                                                pygame.draw.rect(WIN, (90, 90, 90), (repeat + 50, repeat2 + 50, 45, 45))
                                            else:
                                                pygame.draw.rect(WIN, (70, 70, 70), (repeat + 50, repeat2 + 50, 45, 45))

                                elif turn == '-1':
                                    dist = current_piece[1]
                                    if red_kings[red_pieces.index(dist)] == 0:
                                        if dist[1]-repeat2 == abs(dist[1]-repeat2):
                                            pygame.draw.rect(WIN, (90, 90, 90), (repeat + 50, repeat2 + 50, 45, 45))
                                        else:
                                            pygame.draw.rect(WIN, (70, 70, 70), (repeat + 50, repeat2 + 50, 45, 45))
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
    global embedded_list
    global force_end_turn
    global opposite_team_pieces
    global jumped
    global embedded_list
    global current_team
    global current_piece
    force_end_turn = 0
    # This is computing whether u can move anymore after jumping someone
    if jumped >= 5:
        for i in possible:
            embedded_list = current[1]
            if embedded_list != () and i != ():
                # This is calculating the distance between u and the possible moves,
                # so if it = 100 then that means u can go again.
                if abs(int(embedded_list[1]) - int(i[1])) == 100:
                    if turn == '1':
                        dist = current_piece[1]
                        if dist != ():
                            if black_kings[black_pieces.index(dist)] == 0:
                                if int(embedded_list[1] - int(i[1])) != 100:
                                    force_end_turn = 1
                            else:
                                force_end_turn = 1

                    elif turn == '-1':
                        dist = current_piece[1]
                        if dist != ():
                            if red_kings[red_pieces.index(dist)] == 0:
                                if int(embedded_list[1] - int(i[1])) == 100:
                                    force_end_turn = 1
                            else:
                                force_end_turn = 1

        # If it doesn't find any that = 100 then u can't go again
        if force_end_turn == 0:
            jumped = 0
            if opposite_team_pieces == black_pieces:
                opposite_team_pieces = red_pieces
                current_team = black_pieces
                pygame.display.set_caption("Black's turn")
                turn = '1'
                current_piece = [(), (), (), '-1']
            elif opposite_team_pieces == red_pieces:
                opposite_team_pieces = black_pieces
                current_team = red_pieces
                pygame.display.set_caption("Red's turn")
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
    print(jumped)
    moved += 1

    no_more_moves(possible_moves, current_piece)

    if current_piece[0:1] == [()]:
        possible_moves = [(), (), (), ()]

    for event in pygame.event.get():
        if event.type == pygame.QUIT or len(red_pieces) == 0 or len(black_pieces) == 0:
            if len(red_pieces) == 0:
                print("Black Wins!")
            elif len(black_pieces) == 0:
                print("Red Wins!")
            run = False
            break
pygame.quit()
