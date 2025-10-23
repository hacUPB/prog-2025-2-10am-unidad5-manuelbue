import csv


with open('C:\\Users\\ASUS\\OneDrive\\Desktop\\ejemploexcel.csv', 'r')as csvfile:
    lector = csv.reader(csvfile)
    encabezado=next(lector)
    presion = []
    for fila in lector:
        #fila[3] = fila[3].replace(',','.')
        dato = float(fila[3])
        presion.append(dato)
print(presion)
