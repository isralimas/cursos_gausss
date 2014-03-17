A = 0
while True:
	print ' que operacion hacer tu quieres ? '
	operacion = raw_input()
	if operacion == "salir":
		break
	entrada = raw_input('Que valor ? "numero" ')
	if operacion == '+':
		A = A + int(entrada)
	if operacion == '-':
		A = A - int(entrada)
	if operacion == '*':
		A = A * int(entrada)
	if operacion == '/':
		A = A / int(entrada)
	print 'resultado', A
# programa para sumar