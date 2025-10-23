ubicacion = "C:\\Users\\ASUS\\OneDrive\\Desktop\\archivos"
#se usa para comandos de texto
nombre_archivo = "fruta.txt"
modo = "x" #modo escritura solo sobreescribe
fp =open( ubicacion+"\\"+ nombre_archivo, modo, encoding="utf-8") 
frase = input("por favor ingresa una frase: ")

numero_entero = int(input(" ingrese su peso: "))
numero_flotante = int(input("porfavor ingrese ingrese su numero de nequi: "))

fp.write("Frase: " + frase + "\n")
fp.write("numero entero: " + str(numero_entero) + "\n")
fp.write("numero flotante: " + str(numero_flotante) + "\n")

fp.close()