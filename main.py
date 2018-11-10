# Receive point
# Create display
# Create point
# Receive Operation
# Update display

from __future__ import print_function
import OpenGL
import random
from transformation import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import transformation

vertices = []
edges = []
is2D = False
is3D = False
window_name = 'cartesian'
angle = 0.0
lx = 0.0
lz = -1.0
x = 0.0
z = 5.0
currentCommand = ""

def displayObject():
	#Menampilkan object saat ini
	shape.output()

def displayCartesian2D():
	#Menampilkan sumbu x dan y
	glColor3f(0.0, 0.0, 0.0)
	glBegin(GL_LINES)
	glVertex3fv((-1,0,0))
	glVertex3fv((1,0,0))
	glEnd()
	glBegin(GL_LINES)
	glVertex3fv((0,-1,0))
	glVertex3fv((0,1,0))
	glEnd()

def displayCartesian3D():
	#Todo
	return

def input2D():
	global shape
	N = int(raw_input("Masukkan nilai N\n"))
	print("Masukkan " + str(N) + " buah titik 2 dimensi")
	for i in range(N):
		x, y = map(float, raw_input().split())
		z = 0
		arr = [x/25,y/25,z]
		vertices.insert(len(vertices), arr)
		edges.insert(len(edges),[i,(i+1)%N])
	shape = Object2D(vertices, edges)

def input3D():
	#Todo
	return

def inputDimensionChoice():
	global is2D,is3D
	x = int(input("Keluarkan 2 jika ingin 2 dimensi, dan 3 jika ingin 3D\n"))
	while(x != 2 and x != 3):
		print("Masukkan salah")
		x = int(input("Keluarkan 2 jika ingin 2 dimensi, dan 3 jika ingin 3D\n"))
	if(x == 2):
		is2D = True
	else:
		is3D = True

def keyPressed(key, x, y):
	#Todo: Writing while displaying on terminal
	global currentCommand
	if(key == "\n"):
		currentCommand = ""
		return
	elif(ord(key) == 8):
		key = "\b \b"
		currentCommand = currentCommand[:-1]
	else:
		currentCommand += key
	print(key, end='')

def openGLDisplay():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(400,400)
	glutCreateWindow(window_name)
	glutDisplayFunc(display)
	#glutReshapeFunc(changeSize)
	glutKeyboardFunc(keyPressed)
	glutMainLoop()
	return

def main():
	inputDimensionChoice()
	if(is2D):		
		input2D()
	else:
		input3D()
	openGLDisplay()

def display():
	glClearColor(1.0, 1.0, 1.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	if(is2D):
		gluLookAt(0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0,  0.0);
		displayCartesian2D()
		displayObject()
	else:
		gluLookAt(0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0,  0.0);
		displayCartesian3D()
		displayObject()
	glPopMatrix()
	glutSwapBuffers()
	return

def changeSize(w, h):
	if(h == 0):
		h = 1
	ratio = 1.0* w / h
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glViewport(0, 0, w, h)
	gluPerspective(45,ratio,1,1000)
	glMatrixMode(GL_MODELVIEW)

main()