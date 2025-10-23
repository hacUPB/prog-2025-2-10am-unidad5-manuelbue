import csv
encabezado = ['carro', 'motor', 'pais']
carro_1 = ['340i', 3.0, 'alemania']
carro_2 = ['mustang gt', 5.0, 'estados unidos']
with open("salida.csv", 'w', newline='') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(encabezado)  # Escribe la fila de encabezados
    escritor.writerow(carro_1)
    escritor.writerow(carro_2)
print(carro_1)