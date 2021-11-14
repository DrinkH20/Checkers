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
possible_moves = [0, 0, 0, 0]
ground = []
part = 0


def move(re1, re2, item):
    global turn
    global current_piece
    global possible_moves
    if turn == '1':
        white_pieces[item] = re1, re2
        current_piece = [0, 0, 0, ""]
        turn = '2'
        pygame.display.set_caption("Black's turn")
    elif turn == '2':
        black_pieces[item] = re1, re2
        current_piece = [0, 0, 0, ""]
        turn = '1'
        pygame.display.set_caption("Red's turn")
    # possible_moves = [0, 0, 0, 0]


def can_move(place, moves):
    global part
    part = 0
    if moves == '1':
        opossite = black_pieces
        print(opossite, "2")
    else:
        opossite = white_pieces
        print(opossite, "1")

    # print(part)
    if current_piece.__contains__((place[0] + 50, place[1] + 50)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    elif current_piece.__contains__((place[0] + 100, place[1] + 100)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    if current_piece.__contains__((place[0] - 50, place[1] + 50)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    elif current_piece.__contains__((place[0] - 100, place[1] + 100)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    if current_piece.__contains__((place[0] - 50, place[1] - 50)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    elif current_piece.__contains__((place[0] - 100, place[1] - 100)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    if current_piece.__contains__((int(place[0]) + 50, place[1] - 50)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)
        part += 1
    elif current_piece.__contains__((int(place[0]) + 100, place[1] - 100)):
        print(part)
        possible_moves[part] = place
        print(possible_moves)

        part += 1
    # print(current_piece, "hi")
    # print(place)
    # print(possible_moves)


# def generate_places(place):
#     global possible_moves
#     global ground
#     if ground.__contains__((place[0] + 50, place[1] + 50)):
#         possible_moves[0] = (place[0] + 50, place[1] + 50)
#
#     if ground.__contains__((place[0] - 50, place[1] + 50)):
#         possible_moves[1] = (place[0] - 50, place[1] + 50)
#
#     if ground.__contains__((place[0] - 50, place[1] - 50)):
#         possible_moves[2] = (place[0] - 50, place[1] - 50)
#
#     if ground.__contains__((int(place[0]) + 50, place[1] - 50)):
#         possible_moves[3] = (place[0] + 50, place[1] - 50)


# 1: Pawn 2: Bishop 3: Night 4: Rook 5: King 6: Queen
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
                    if click[0] and turn == '2':
                        current_piece = black_pieces.index((repeat, repeat2)), (repeat, repeat2)
                    # if click[0]:
                    #     if repeat - 50 == current_piece[1] and repeat2 + 50 == current_piece[2]:
                    #         if not white_pieces.__contains__((repeat + 50, repeat2 - 50)):
                    #             move(repeat + 50, repeat2 - 50, current_piece[0])
                    #
                    #     if repeat + 50 == current_piece[1] and repeat2 - 50 == current_piece[2]:
                    #         if not white_pieces.__contains__((repeat - 50, repeat2 + 50)):
                    #             move(repeat - 50, repeat2 + 50, current_piece[0])
                    #
                    #     if repeat + 50 == current_piece[1] and repeat2 + 50 == current_piece[2]:
                    #         if not white_pieces.__contains__((repeat - 50, repeat2 - 50)):
                    #             move(repeat - 50, repeat2 - 50, current_piece[0])
                    #
                    #     if repeat - 50 == current_piece[1] and repeat2 - 50 == current_piece[2]:
                    #         if not white_pieces.__contains__((repeat + 50, repeat2 + 50)):
                    #             move(repeat + 50, repeat2 + 50, current_piece[0])

            else:
                if (50 * round(int(mx - 25)/50)) == repeat + 50 and (50 * round(int(my - 25)/50)) == repeat2 + 50:
                    can_move((repeat, repeat2), turn)
                    pygame.draw.rect(WIN, (100, 150, 100), (repeat + 50, repeat2 + 50, 45, 45))
                    if click[0]:
                        if possible_moves.__contains__((repeat, repeat2)):
                            move(repeat, repeat2, current_piece[0])
                        # if repeat - 50 == current_piece[1] and repeat2 + 50 == current_piece[2]:
                        #     move(repeat, repeat2, current_piece[0])
                        # if repeat + 50 == current_piece[1] and repeat2 - 50 == current_piece[2]:
                        #     move(repeat, repeat2, current_piece[0])
                        # if repeat + 50 == current_piece[1] and repeat2 + 50 == current_piece[2]:
                        #     move(repeat, repeat2, current_piece[0])
                        # if repeat - 50 == current_piece[1] and repeat2 - 50 == current_piece[2]:
                        #     move(repeat, repeat2, current_piece[0])

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
            possible_moves[part] = 0


while run:
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    WIN.fill((10, 10, 10))
    mx, my = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)
    screen_draw(scrnw - 100, scrnh - 100)
    # generate_places(current_piece[1:3])
    pygame.display.update()
    ground = []

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
