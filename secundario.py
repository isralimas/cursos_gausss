from pasopaso import zeros, unos, reglas
import random

xd=30
#valor1 = int(raw_input('#1 ? '))
#valor2 = int(raw_input('#2 ? '))

#llenado de matriz
def llenado_matrix():
	if random.randrange(7) == 0:
		return 1
	else:
		return 0

# matriz = [[llenado_matrix() for x in xrange(xd)] for x in xrange(xd)]
matriz = zeros(xd,xd)
matriz[0][2]=1
matriz[1][3]=1
#matriz[2][0]=1
matriz[2][1]=1
matriz[2][2]=1
matriz[2][3]=1

matriz[1][xd-5]=1
matriz[1][xd-4]=1
matriz[2][xd-5]=1
matriz[3][xd-2]=1
matriz[4][xd-3]=1
matriz[4][xd-2]=1

variable = zeros(xd,xd)
#for fila in matriz:
#	print fila

print 'quitando comas y corchetes'

for fila in matriz:
	for elemento in fila:
		if elemento == 1:
			print '@',
		else:
			print '.',
	print

for pasos in xrange(100):

	#celulas de esquina
	try:
		vecinos = matriz[0][1]+matriz[1][0]+matriz[1][1]
		variable[0][0]=reglas(vecinos,0,0,matriz)
	except:
		pass
	vecinos = matriz[0][ xd - 2 ] + matriz[1][ xd - 2 ] + matriz[1][ xd - 1 ]
	variable[0][ xd - 1 ]=reglas(vecinos,0, xd - 1 ,matriz)
	vecinos = matriz[ xd - 2 ][0] + matriz[ xd - 2 ][1] + matriz[ xd - 1 ][1]
	variable[ xd - 1 ][0]=reglas(vecinos, xd - 1 ,0,matriz)
	vecinos = matriz[ xd - 2 ][ xd - 2 ] + matriz[ xd - 2 ][ xd - 1 ] + matriz[ xd - 1 ][ xd - 2 ]
	variable[ xd - 1 ][ xd - 1 ] = reglas(vecinos, xd - 1 , xd - 1 ,matriz)

	#celulas orillas
	for pos in range( 1 , xd - 1 ) :
		vecinos= matriz[0][pos - 1] + matriz[0][pos + 1] + matriz[1][pos - 1] + matriz[1][pos] + matriz[1][pos + 1]
		variable[0][pos]=reglas(vecinos,0,pos,matriz)
	for pos in range( 1 , xd - 1 ) :
		vecinos= matriz[ xd - 1 ][pos - 1] + matriz[ xd - 1 ][pos + 1] + matriz[ xd - 2 ][pos - 1] + matriz[ xd - 2 ][pos] + matriz[ xd - 2 ][pos + 1]
		variable[ xd - 1 ][pos] = reglas(vecinos, xd - 1, pos, matriz)
	for pos in range( 1 , xd - 1 ) :
		vecinos= matriz[ pos -1 ][0] + matriz[ pos + 1 ][0] + matriz[ pos - 1 ][ 1 ] + matriz[pos][1] + matriz[ pos + 1 ][1]
		variable[ pos ][0] = reglas(vecinos, pos , 0, matriz)
	for pos in range( 1 , xd - 1 ) :
		vecinos= matriz[ pos - 1 ][ xd -1 ] + matriz[ pos + 1 ][ xd - 1 ] + matriz[ pos - 1 ][ xd - 2 ] + matriz[pos][ xd - 2 ] + matriz[pos + 1][ xd - 2 ]
		variable[pos][ xd - 1 ] = reglas(vecinos, pos, xd - 1 , matriz)
	#for posx in range(1, xd - 1 ):

	#ceelulas centrales
	for posx in range(1, xd - 1 ):
		for posy in range(1, xd - 1 ):
				vecinos = matriz[ posx - 1][ posy - 1] + matriz[posx][ posy - 1 ]+ matriz[ posx + 1 ][ posy - 1 ] + matriz[ posx - 1 ][ posy ] + matriz[ posx + 1 ][ posy ] + matriz[ posx - 1 ][ posy + 1 ] + matriz[ posx ][ posy + 1 ] + matriz[ posx + 1 ][ posy + 1 ]
				variable[posx][posy] = reglas(vecinos,posx,posy,matriz)
	#			print posx, posy, vecinos,
	#	print
	print 'siguiente paso', pasos
	for x in xrange(xd):
		for y in xrange(xd):
			matriz[x][y] = matriz[x][y] + variable[x][y]

	for fila in matriz:
		for elemento in fila:
			if elemento == 1:
				print '@',
			else:
				print '.',
		print




#print variable