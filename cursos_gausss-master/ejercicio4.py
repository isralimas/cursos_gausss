iteraciones = int(raw_input('Cuantas iteraciones ? (#) :'))
matriz = [1,1]
while iteraciones > 0:
	iteraciones = iteraciones - 1
	indice = len(matriz)
	while indice > 1:
		indice = indice - 1
		matriz[indice] = matriz[indice] + matriz[indice - 1]
	matriz.append(1)
	print matriz
