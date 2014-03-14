def zeros(var1,var2):
	matriz = [[0 for x in xrange(var1)] for x in xrange(var2)]
	return matriz

def unos(dimx,dimy):
	matriz = [[1 for x in xrange(dimx)] for x in xrange(dimy)]
	return matriz

def reglas(sumavecino,posx,posy,matrix):
	if sumavecino < 2:
		suma = -1 * matrix[posx][posy]
	elif sumavecino > 3:
		suma = -1 * matrix[posx][posy]
#		suma = 1 - (2*matrix[posx][posy])
	elif sumavecino == 3:
		suma = 1 - matrix[posx][posy]
	else:
		suma = 0
	return suma
