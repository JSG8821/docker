# Programa para generar un archivo con números del 1 al 100,000

def generar_numeros():
    with open("numeros.txt", "w") as archivo:
        for numero in range(1, 100001):
            archivo.write(f"{numero}\n")

if __name__ == "__main__":
    generar_numeros()