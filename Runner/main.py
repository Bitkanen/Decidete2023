import pygame
import cv2
import dlib
import numpy as np
import random

pygame.init()

# region Captura y Deteccion de Cara con dlib
detector = dlib.get_frontal_face_detector()     # Deteccion de Cara en dlib
predictor = dlib.shape_predictor("Files/shape_predictor_68_face_landmarks.dat")     # Predictor de puntos faciales
cap = cv2.VideoCapture(0)   # Captura de video en CV
# endregion

# region Constantes
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
fps = 120
letter = pygame.font.SysFont("Arial", 60)
# endregion

# region Variables del Juego
angle = 0   # Angulo de la Cabeza del Jugador
iteration = 0   # Iteraciones Actuales
score = 0   # Puntaje del Jugador
player_x = 750  # Posicion Inicial del Jugador en X
player_y = 600  # Posicion Incial del Jugador en Y
current_player_sprite = 0  # Fotograma Actual del Jugador
current_back_sprite = 0     # Fotograma Actual del Pasillo
current_first_box_sprite = 0  # Fotograma Actual del Obstaculo
current_second_box_sprite = 0
current_heart_sprite = 0
movement_box = -30  # Movimiento del Obstaculo
box_y = [-30, 150, 330, 540, 750, 900]  # Distancia en la cambia el Obstaculo
box_x = [700, 800, 900]

speed_sprite_player = 3    # Velocidad de la Animacion del Jugador
speed_back_sprite = 3   # Velocidad de la Animacion del Pasillo
speed_box_sprite = 25   # Velocidad de la Animacion de la Caja
speed_box_x = 5

num_first_box = random.randint(1, 3)
num_second_box = random.randint(0, 0)
# endregion

# region Ajustes Ventana
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('Infinite Runner')
background = black

# Obtiene las dimensiones de la pantalla
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
# endregion

# region Fotogramas de Sprites
player_sprite_sheet = pygame.image.load('assets/BerrendoSprite.png').convert_alpha()
back_sprite_sheet = pygame.image.load('assets/PasilloSprite.png').convert_alpha()
box_sprite_sheet = pygame.image.load('assets/BoxSprite.png').convert_alpha()
heart_sprite_sheet = pygame.image.load('assets/HeartSprite.png').convert_alpha()
endTitle_sprite_sheet = pygame.image.load('assets/TitleSprite.png').convert_alpha()
player_sprite_list = []
back_sprite_list = []
box_sprite_list = []
heart_sprite_list = []

for i in range(4):
    rect1 = pygame.Rect((i * 300, 0), (300, 430))
    player_sprite_list.append(rect1)

for i in range(9):
    rect2 = pygame.Rect((i * 1920, 0), (1920, 1080))
    back_sprite_list.append(rect2)

for i in range(6):
    rect3 = pygame.Rect((i * 250, 0), (250, 220))
    box_sprite_list.append(rect3)

for i in range(4):
    rect4 = pygame.Rect((i * 315, 0), (315, 100))
    heart_sprite_list.append(rect4)

# endregion

running = True
timer = pygame.time.Clock()
pause = False

while running:

    # region Reconocimiento Facial
    _, img = cap.read()
    faces = detector(img)

    timer.tick(fps)
    screen.fill(background)

    for face in faces:
        landmarks = predictor(img, face)

        # Coordenadas para los puntos de referencia del ojo izquierdo y derecho
        left_eye = (landmarks.part(36).x, landmarks.part(36).y)
        right_eye = (landmarks.part(45).x, landmarks.part(45).y)

        # Calcular el ángulo de rotación
        dx = right_eye[0] - left_eye[0]
        dy = right_eye[1] - left_eye[1]
        angle = np.arctan(dy / dx)
        angle = angle * 180. / np.pi

    # endregion

    # region Introduccion de Objetos, fondo y personaje
    screen.blit(back_sprite_sheet, (0, 0), back_sprite_list[current_back_sprite])
    screen.blit(heart_sprite_sheet, (50, 20), heart_sprite_list[current_heart_sprite])
    text_score = letter.render(("Score: " + str(score)), True, (0, 0, 0), (200, 200, 200))
    recttext = text_score.get_rect()
    screen.blit(text_score, (1600, 30), recttext)

    # region Eleccion de Caja
    if num_first_box == 1:
        screen.blit(box_sprite_sheet, (box_x[0], movement_box), box_sprite_list[current_first_box_sprite])
    if num_first_box == 2:
        screen.blit(box_sprite_sheet, (box_x[1], movement_box), box_sprite_list[current_first_box_sprite])
    if num_first_box == 3:
        screen.blit(box_sprite_sheet, (box_x[2], movement_box), box_sprite_list[current_first_box_sprite])
    if num_second_box == 4:
        screen.blit(box_sprite_sheet,(box_x[0], movement_box), box_sprite_list[current_second_box_sprite])
    if num_second_box == 5:
        screen.blit(box_sprite_sheet, (box_x[1], movement_box), box_sprite_list[current_second_box_sprite])
    if num_second_box == 6:
        screen.blit(box_sprite_sheet, (box_x[2], movement_box), box_sprite_list[current_second_box_sprite])

    # endregion

    player = pygame.Rect(player_x, player_y, 300, 430)
    screen.blit(player_sprite_sheet, player, player_sprite_list[current_player_sprite])

    if pause:
        endTitle = pygame.Rect(630, 400, 605, 187)
        screen.blit(endTitle_sprite_sheet, endTitle)

    # endregion

    # region Velocidad de Sprites

    # region Velocidad de Jugador y Fondo
    if pause == False:

        if iteration % speed_sprite_player == 0:
            current_player_sprite = (current_player_sprite + 1) % 4

        if iteration % speed_back_sprite == 0:
            current_back_sprite = (current_back_sprite + 1) % 9

    # endregion

    # region Velocidad de Objetos
    if iteration % 2 == 0:
        movement_box += speed_box_sprite

        if num_first_box == 1:
            box_x[0] -= speed_box_x

        if num_first_box == 3:
            box_x[2] += speed_box_x


        if movement_box > box_y[0]  and movement_box < box_y[1]:
            current_first_box_sprite = 0

        if movement_box > box_y[1] and movement_box < box_y[2]:
            current_first_box_sprite = 1

        if movement_box > box_y[2] and movement_box < box_y[3]:
            current_first_box_sprite = 2

        if movement_box > box_y[3] and movement_box < box_y[4]:
            current_first_box_sprite = 3

        if movement_box > box_y[4] and movement_box < box_y[5]:
            current_first_box_sprite = 3

            if player_x == 540 and num_first_box == 1 or player_x == 1010 and num_first_box == 3 or player_x == 780 and num_first_box == 2:
                if current_heart_sprite != 3:
                    current_heart_sprite += 1

                    if current_heart_sprite == 3:
                        speed_box_sprite = 0
                        speed_box_x = 0
                        pause = True

                    else:
                        movement_box = -60
                        current_first_box_sprite = 0
                        num_first_box = random.randint(1, 3)

                        if num_first_box == 1:
                            box_x[0] = 700
                        if num_first_box == 3:
                            box_x[2] = 900

        if movement_box > 970:
            movement_box = -60
            current_first_box_sprite = 0
            num_first_box = random.randint(1, 3)

            if num_first_box == 1:
                box_x[0] = 700
            if num_first_box == 3:
                box_x[2] = 900
    # endregion

    # endregion

    # region Eventos de Key y Movimiento de cara
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                pause = False

                movement_box = -60
                current_first_box_sprite = 0
                num_first_box = random.randint(1, 3)

                if num_first_box == 1:
                    box_x[0] = 700
                if num_first_box == 3:
                    box_x[2] = 900

                speed_sprite_player = 3
                speed_back_sprite = 3
                speed_box_sprite = 25
                speed_box_x = 5
                score = 0
                iteration = 0
                current_heart_sprite = 0
                screen.fill(black)


    if pause == False:
        if angle > -10 and angle < 10:
            player_x = 780

        if angle > 10:
            player_x = 540

        if angle < -10:
            player_x = 1010
    # endregion

    if pause == False:

        iteration += 1

        if iteration % 3 == 0:
            score += 1

            if score >= 50:
                if score % 50 == 0:

                    if speed_sprite_player > 1:
                        speed_sprite_player -= 1

                    if speed_back_sprite > 1:
                        speed_back_sprite -= 1

                    speed_box_sprite += 15
                    speed_box_x += 3


    pygame.display.flip()
pygame.quit()
