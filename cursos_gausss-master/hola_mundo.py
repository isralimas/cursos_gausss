#Este es mi primer programa de python
gaus = 10
jordan = 5
escuela = gaus + jordan
print escuela
escuela = 'gaus' + "jordan"
print escuela
#escuela = 'gaus' + jordan
#print escuela
#las liineas anteriores producen un error
#en la compilacioon por diferencia entre tipos de 
# variables
jordan = "Jordan"
escuela = 'gaus' + jordan
print escuela
#sumando cadenas de texto
escuela = 'gaus' + str(gaus)
print escuela
#sumando cadenas de texto con conversion de un enetero a cadena de texto
gaus = '10'
jordan = "5"
escuela = gaus + jordan
print escuela
# CONCATENACIOON de cadenas de texto
escuela = int(escuela) + 1
print escuela
# conversioon de cadenas de texto a enteros
matriz = ['matriz']
print matriz
# corchetes para vaciio o un soolo elemento

matrix = ("matriz",'perro')
print matrix
print matrix[0]
print matrix[1]
#definiendo los elementos de matriz para la impresioon

matrox = ("matrix",'perro',10)
print matrox[2]

ejercicio = matrox[1] + str(matrox[2]) + matrox[0]
print ejercicio
#el anterior no economiza memoria
print matrox[0]
print matrox[1]
print matrox[2]
print matrox[1] + str(matrox[2]) + matrox[0]
#esta es la solucioon

#boolean data
matriz_t = True
matriz_f = False
print matriz_t
print matriz_f
matroz = 5.5
matruz = 5.0

print matroz + matruz

