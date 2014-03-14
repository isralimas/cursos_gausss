iteraciones = int(raw_input('Cuantas iteraciones ? (#) :'))
entrada = raw_input('Que valor ? (# > 10) :')
while iteraciones > 0:
	iteraciones = iteraciones - 1
	entrada = str(int(entrada) + int(entrada[0]) + int(entrada[len(entrada)-1]))             
	print entrada
