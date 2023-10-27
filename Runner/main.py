import pygame
import cv2
import dlib
import numpy as np
import random

pygame.init()

#Deteccion de Cara en dlib
detector = dlib.get_frontal_face_detector()
# Predictor de puntos faciales
predictor = dlib.shape_predictor("Files/shape_predictor_68_face_landmarks.dat")
#Captura de video en CV
cap = cv2.VideoCapture(0)

# Constantes
white = (255, 255, 255)
black = (0,0,0)
green = (0,255,0)
fps = 60
speed_sprite = 2 #Velocidad de la Animacion del Jugador
speed_back_sprite = 3 #Velocidad de la Animacion del Pasillo
speed_box_sprite = 40 #Velocidad de la Animacion de la Caja

# Variables del Juego
angle = 0   #Angulo de la Cabeza del Jugador
iteration = 0 # Iteraciones Actuales
score = 0 #Puntaje del Jugador
player_x = 750 #Posicion Inicial del Jugador en X
player_y = 600 #Posicion Incial del Jugador en Y
current_sprite = 0 #Fotograma Actual del Jugador
current_back_sprite = 0 #Fotograma Actual del Pasillo
current_box_sprite = 0 #Fotograma Actual del Obstaculo
movement_box = -30 #Movimiento del Obstaculo

box_y = [-30, 150, 330, 540, 750, 900] #Distancia en la cambia el Obstaculo
box_x = [700, 800, 900]

num_aleatorio = random.randint(1, 3)


timer = pygame.time.Clock()

#Ajustes Ventana
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Infinite Runner')
background = black

# Obtiene las dimensiones de la pantalla
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h

#Obtiene una lista de los fotogramas del jugador
sprite_sheet = pygame.image.load('assets/BerrendoSprite.png').convert_alpha()
back_sprite_sheet = pygame.image.load('assets/PasilloSprite.png').convert_alpha()
box_sprite_sheet = pygame.image.load('assets/BoxSprite.png').convert_alpha()
sprite_list = []
back_sprite_list = []
box_sprite_list = []

for i in range(4):
    rect1 = pygame.Rect((i * 300, 0), (300, 430))
    sprite_list.append(rect1)

for i in range(9):
    rect2 = pygame.Rect((i * 1920, 0), (1920, 1080))
    back_sprite_list.append(rect2)

for i in range(6):
    rect3 = pygame.Rect((i*250,0),(250,220))
    box_sprite_list.append(rect3)

box1= None
box2 = None
box3 = None

running = True
while running:

    # Reconocimiento Facial
    _, img = cap.read()
    faces = detector(img)

    timer.tick(fps)
    screen.fill(background)

    # (y,x,w,h)
    screen.blit(back_sprite_sheet,(0,0),back_sprite_list[current_back_sprite])

    if num_aleatorio == 1:
        #screen.blit(box_sprite_sheet,(box_x[0],movement_box),box_sprite_list[current_box_sprite])
        box1 = pygame.Rect(box_x[0], movement_box, box_sprite_list[current_box_sprite].width,box_sprite_list[current_box_sprite].height)
        screen.blit(box_sprite_sheet, box1, box_sprite_list[current_box_sprite])
    if num_aleatorio == 2:
        screen.blit(box_sprite_sheet, (box_x[1], movement_box), box_sprite_list[current_box_sprite])
        #box2 = pygame.Rect(box_x[1], movement_box, box_sprite_list[current_box_sprite].width,box_sprite_list[current_box_sprite].height)
        #screen.blit(box_sprite_sheet, box2, box_sprite_list[current_box_sprite])
    if num_aleatorio == 3:
        screen.blit(box_sprite_sheet, (box_x[2], movement_box), box_sprite_list[current_box_sprite])
        #box3 = pygame.Rect(box_x[2], movement_box, box_sprite_list[current_box_sprite].width,box_sprite_list[current_box_sprite].height)
        #screen.blit(box_sprite_sheet, box1, box_sprite_list[current_box_sprite])

    #screen.blit(sprite_sheet, (player_x, player_y), sprite_list[current_sprite])

    player = pygame.Rect(player_x, player_y, sprite_list[current_sprite].width,sprite_list[current_sprite].height)
    screen.blit(sprite_sheet, player, sprite_list[current_sprite])


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

    # ----------------------------------------------------------------------

    if iteration % speed_sprite == 0:
        current_sprite = (current_sprite + 1) % 4

    if iteration % speed_back_sprite == 0:
        current_back_sprite = (current_back_sprite + 1) % 9

    # box_y = [-30, 150, 330, 540, 750, 900]
    if iteration % 2 == 0:
        movement_box += speed_box_sprite
        box_x[0] -= 8
        box_x[2] += 8

        if movement_box > box_y[0]  and movement_box < box_y[1]:
            current_box_sprite = 0

        if movement_box > box_y[1] and movement_box < box_y[2]:
            current_box_sprite = 1

        if movement_box > box_y[2] and movement_box < box_y[3]:
            current_box_sprite = 2

        if movement_box > box_y[3]  and movement_box < box_y[4]:
            current_box_sprite = 3

        if  movement_box > box_y[4]  and movement_box < box_y[5]:
            current_box_sprite = 3
            movement_box += 30

        if movement_box > 970:
            movement_box = -60
            box_x[0] = 700
            box_x[2] = 900
            current_box_sprite = 0
            num_aleatorio = random.randint(1, 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if angle > -10 and angle < 10:
        player_x = 780

    if angle > 10:
        player_x = 540

    if angle < -10:
        player_x = 1010

    iteration += 1

    pygame.display.flip()
pygame.quit()