# 1. abrir el archivo y define el modo
archivo = open("text.txt","r")
# 2. leer el archivo
#for datos in archivo:
   # print(datos[0])
datos = archivo.readlines()
print(datos)
#3. cerrar el archivo
archivo.close()