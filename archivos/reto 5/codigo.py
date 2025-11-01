import os
import csv
import matplotlib.pyplot as plt

CSV_FILE = "ventasloteria.csv"
TXT_FILE = "ventasloteria.txt"

# ---------------- FUNCIONES PARA TXT ----------------
def contar_txt():
    with open(TXT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()
    palabras = texto.split()
    print("Palabras:", len(palabras))
    print("Caracteres con espacios:", len(texto))
    print("Caracteres sin espacios:", len(texto.replace(" ", "")))

def reemplazar_txt():
    buscar = input("Palabra a buscar: ")
    nueva = input("Palabra nueva: ")
    with open(TXT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read()
    texto = texto.replace(buscar, nueva)
    with open(TXT_FILE, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Reemplazo hecho correctamente.")

def histograma_vocales():
    with open(TXT_FILE, "r", encoding="utf-8", errors="ignore") as f:
        texto = f.read().lower()
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for c in texto:
        if c in conteo:
            conteo[c] += 1
    plt.bar(conteo.keys(), conteo.values(), color="blue")
    plt.title("Histograma de vocales")
    plt.show()

# ---------------- FUNCIONES PARA CSV ----------------
def mostrar_csv():
    with open(CSV_FILE, "r", encoding="utf-8", errors="ignore") as f:
        lector = csv.reader(f, delimiter=";")
        for i, fila in enumerate(lector):
            print(fila)
            if i == 14:
                break

def calcular_estadisticas():
    with open(CSV_FILE, "r", encoding="utf-8", errors="ignore") as f:
        lector = csv.reader(f, delimiter=";")
        encabezados = next(lector)
        for i, h in enumerate(encabezados):
            print(i, h)
        col = int(input("Número de columna: "))
        datos = []
        for fila in lector:
            if fila[col] != "":
                try:
                    datos.append(float(fila[col].replace(",", ".")))
                except:
                    pass
    if len(datos) == 0:
        print("No hay datos numéricos.")
        return
    datos.sort()
    n = len(datos)
    promedio = sum(datos) / n
    print("Cantidad:", n)
    print("Promedio:", promedio)
    print("Máximo:", max(datos))
    print("Mínimo:", min(datos))

def graficar_columna():
    with open(CSV_FILE, "r", encoding="utf-8", errors="ignore") as f:
        lector = csv.reader(f, delimiter=";")
        encabezados = next(lector)
        for i, h in enumerate(encabezados):
            print(i, h)
        col = int(input("Número de columna: "))
        datos = []
        for fila in lector:
            if fila[col] != "":
                try:
                    datos.append(float(fila[col].replace(",", ".")))
                except:
                    pass
    if len(datos) == 0:
        print("No hay datos numéricos.")
        return
    plt.scatter(range(len(datos)), datos, color="green")
    plt.title("Gráfico de dispersión")
    plt.show()
    plt.bar(range(len(datos)), datos, color="orange")
    plt.title("Gráfico de barras")
    plt.show()

# ---------------- MENÚS ----------------
def menu_txt():
    while True:
        print("\n--- Submenú TXT ---")
        print("1. Contar palabras y caracteres")
        print("2. Reemplazar palabra")
        print("3. Histograma de vocales")
        print("4. Volver")

        opcion = input("Escribe el número de la opción: ")

        if opcion == "1":
            contar_txt()
        elif opcion == "2":
            reemplazar_txt()
        elif opcion == "3":
            histograma_vocales()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_csv():
    while True:
        print("\n--- Submenú CSV ---")
        print("1. Mostrar primeras 15 filas")
        print("2. Calcular estadísticas")
        print("3. Graficar columna")
        print("4. Volver")

        opcion = input("Escribe el número de la opción: ")

        if opcion == "1":
            mostrar_csv()
        elif opcion == "2":
            calcular_estadisticas()
        elif opcion == "3":
            graficar_columna()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar archivos en carpeta")
        print("2. Procesar archivo TXT")
        print("3. Procesar archivo CSV")
        print("4. Salir")

        opcion = input("Escribe el número de la opción: ")

        if opcion == "1":
            print(os.listdir("."))
        elif opcion == "2":
            menu_txt()
        elif opcion == "3":
            menu_csv()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

main()