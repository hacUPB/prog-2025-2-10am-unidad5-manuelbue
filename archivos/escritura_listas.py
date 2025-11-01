list = ["giuseppe", "por amar a ciegas", "formula", "my eyes", "happier than ever"]
ubicacion = "C:\\Users\\ASUS\\OneDrive\\Desktop\\archivos"
modo = "a"
nombre_archivo = "canciones.txt"

fp = open(ubicacion + "\\" + nombre_archivo,modo,encoding="utf-8")

for cancion in list:
    fp.write(cancion + "\n")

fp.close()
