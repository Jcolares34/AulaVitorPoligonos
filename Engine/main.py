import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import *
from LoadMesh import *
import sys

pygame.init()


# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')
cube = Cube(GL_LINE_LOOP)
mesh = LoadMesh("DiamondSword.obj", GL_LINE_LOOP)

# Camera settings
camera_position = [0, 5, -50]  # X, Y, Z
camera_speed = 1.0  # Speed of camera movement

def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # Ajuste de câmera para uma visão de cima
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()
    #glTranslate(0, 5, -50)  # Move a câmera para cima (10) e para trás (20) no eixo Z
    #glRotatef(90, 1, 0, 0)  # Gira a câmera 90 graus para que ela olhe de cima para baixo
    #glViewport(0, 0, screen.get_width(), screen.get_height())
    #glEnable(GL_DEPTH_TEST)

    # Camera initial setup
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(*camera_position)  # Apply initial camera position
    glRotatef(90, 1, 0, 0)  # Rotate to look down from above
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

def handle_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        glTranslatef(camera_speed, 0, 0)
    if keys[pygame.K_d]:
        glTranslatef(-camera_speed, 0, 0)
    if keys[pygame.K_w]:
        glTranslatef(0, -camera_speed, 0)
    if keys[pygame.K_s]:
        glTranslatef(0, camera_speed, 0)



#def initialise():
#    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
#    glColor(drawing_color)
#
#    # projection
#    glMatrixMode(GL_PROJECTION)
#    glLoadIdentity()
#    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # Ajuste do FOV e dos planos de corte
#    gluPerspective(60, (screen_width / screen_height), 30, 200)  # zNear 1 e zFar 200

    # modelview
#    glMatrixMode(GL_MODELVIEW)
#    glTranslate(0, 0, -1)
#    glLoadIdentity()
#    glViewport(0, 0, screen.get_width(), screen.get_height())
#    glEnable(GL_DEPTH_TEST)
#    glTranslate(0, 0, -2)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glRotatef(1, 10, 0, 1)
    glRotatef(1, 0, 0, 1)
    glPushMatrix()
    #cube.draw()
    mesh.draw()
    glPopMatrix()


done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        handle_input()

    display()
    pygame.display.flip()
    pygame.time.wait(5);
pygame.quit()

