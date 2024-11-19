from OpenGL.GL import *
from Mesh import *
import pygame

class LoadMesh:
    def __init__(self, file_path, draw_type):
        self.file_path = file_path
        self.draw_type = draw_type
        self.vertices = []
        self.faces = []
        self.load_drawing()  # Chama o método para carregar o arquivo .obj

    def load_drawing(self):
        # Lê o arquivo e carrega os dados de vértices e faces
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):  # Linha de vértices
                    vertex = [float(value) for value in line[2:].split()]
                    self.vertices.append(vertex)
                elif line.startswith('f '):  # Linha de faces
                    face = []
                    for value in line[2:].split():
                        indices = value.split('/')
                        vertex_index = int(indices[0]) - 1  # Índice do vértice
                        face.append(vertex_index)
                    self.faces.append(face)

    def draw(self):
        # Desenha as faces do modelo
        glBegin(self.draw_type)
        for face in self.faces:
            for vertex_index in face:
                glVertex3fv(self.vertices[vertex_index])
        glEnd()






#class LoadMesh(Mesh):
#    def __init__(self, filename, draw_type):
#        self.vertices = []
#        self.triangles = []
#        self.filename = filename
#        self.draw_type = draw_type
#        self.load_drawing()

#def load_drawing(self):
#       with open(self.filename) as fp:
#            line = fp.readline()
#            while line:
#                if line[:2] == "v ":
#                    vx, vy, vz = [float(value) for value in line[2:].split()]
#                    self.vertices.append((vx, vy, vz))
#                if line[:2] == "f ":
#                    t1, t2, t3 = [(value) for value in line[2:].split()]
#                    self.triangles.append([int(value) for value in t1.split('/')][0] - 1)
#                    self.triangles.append([int(value) for value in t2.split('/')][0] - 1)
#                    self.triangles.append([int(value) for value in t3.split('/')][0] - 1)
#             line = fp.readline()
