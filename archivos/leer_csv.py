import csv


with open('C:\\Users\\ASUS\\OneDrive\\Desktop\\ejemploexcel.csv', 'r')as csvfile:
    lector = csv.reader(csvfile)
    encabezado=next(lector)
    densidad = []
    for fila in lector:
        #fila[3] = fila[3].replace(',','.')
        dato = float(fila[3])
        densidad.append(dato)
suma = sum(densidad)
print(suma)
promedio = sum(densidad) / len(densidad)
print(promedio)
print(densidad)
