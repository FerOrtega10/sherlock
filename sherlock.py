	
def validacion():
	"""Funcion que valida el ingreso de los datos"""
	longValida=False
	isLetra=False
	while longValida==False or isLetra==False:

		entrada = input("Ingresar cadena para verificar si es Sherlock ") # Lee la entrada de datos y la almacena en la variable texto

		if len(entrada)>=1 and len(entrada)<=100000:
			longValida=True
		if longValida==False:
			print('Longitud invalida. Escriba una cadena que contenga entre 1 y 100000 caracteres')

		lista_letras=list(entrada)
		
		while len(lista_letras)>0:
			letra=lista_letras.pop()
			if (ord(letra) >= 97) and (ord(letra) <= 122):
				isLetra=True
			else:
				print('Existen caracteres que no son letras miúsculas en la cadena. Ingrese únicamente letras minúsculas')
				longValida=False

	return(entrada)


l_texto= list(validacion()) #Convierte el string en una lista de strings cuyos elementos son cada uno de los caracteres de la cadena

caracteres= set(l_texto)#Obtengo el conjunto de los caracteres que debo analizar a partir de la lista l_texto

sherlock=False #Seteo la salida

l_ocurrencias=list() #Creo lista vacia
while len(caracteres)> 0: #El bucle guarda en la lista l_ocurrencias la cantidad de veces que aparece el caracter dado por la funcion pop aplicada al conjunto
	caracter= caracteres.pop()
	cantidad= l_texto.count(caracter)
	l_ocurrencias.append(cantidad)

cant_ocurrencias= set(l_ocurrencias)

if len(cant_ocurrencias)==1: #Si el conjunto de ocurrencias tiene mas de dos valores, significa que hay mas de dos valores distintos de ocurrencias, lo cual incumple la validez de un string sherlock
	sherlock=True

elif len(cant_ocurrencias)==2:
	mayor_ocurrencia=max(cant_ocurrencias)
	menor_ocurrencia=min(cant_ocurrencias)
	if (menor_ocurrencia==1 and l_ocurrencias.count(menor_ocurrencia)==1) or (l_ocurrencias.count(mayor_ocurrencia)==1 and (mayor_ocurrencia - menor_ocurrencia==1)):
		sherlock=True

if sherlock:
	print("SI")
else:
	print("NO")
