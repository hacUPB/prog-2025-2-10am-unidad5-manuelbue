nombre_archivo = "texto.txt"
ubicacion = "C:\\Users\\ASUS\\OneDrive\\Desktop\\archivos"
with open(nombre_archivo,"r", encoding="utf=8") as archivo:
   lista = archivo.readlines()
for c in lista:
   print(c)
