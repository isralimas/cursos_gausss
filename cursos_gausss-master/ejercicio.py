suma = 0
entrada = '0'
while not str(entrada)=='salir':
	suma = suma + int(entrada)
	print '>>> ', suma
	entrada = raw_input()