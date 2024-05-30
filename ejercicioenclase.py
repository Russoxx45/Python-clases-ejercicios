Vocales = ["a","e","i","o","u","A","E","I","O","U"]

nombre = input("Ingrese su nombre: ")
contador=0


for i in nombre:
  if i in Vocales: 
    contador+=1
if contador >= 3:
  print(nombre)
else:
  print("Su nombre no tiene mas de 3 vocales")

