#variable = 0
#while variable < 1000000:
#	print variable
#	variable = variable + 1
#	if variable == 1000:
#		break

#variables = "Hola mundo"
#
#for variable in variables:
#	print variable
#	if variable == 'm':
#		break

variables = [1,2,3,4,'hola mundo']

for variable in variables:
	print variable
	if 'a' in str(variable):
		for letra in variable:
			print letra
			