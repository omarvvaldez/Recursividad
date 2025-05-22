import random
import time

# Función de ordenamiento Burbuja
# Compara elementos adyacentes y los intercambia si están fuera de orden
def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                # Intercambiamos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Función de ordenamiento por Inserción
# Toma cada elemento y lo va insertando en su lugar correcto dentro de la parte ordenada
def insercion(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        posicion = i
        # Desplazamos elementos mayores hacia la derecha
        while posicion > 0 and lista[posicion - 1] > val:
            lista[posicion] = lista[posicion - 1]
            posicion -= 1
        lista[posicion] = val

# Función de ordenamiento por Selección
# Busca el elemento mínimo en la sublista y lo coloca al inicio
def seleccion(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambio del mínimo hallado con el actual
        lista[i], lista[min_index] = lista[min_index], lista[i]

# Función de ordenamiento QuickSort
# Usa recursividad y pivote para dividir la lista en dos partes
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        izq = [x for x in lista[1:] if x < pivote]
        der = [x for x in lista[1:] if x >= pivote]
        # Ordenamos recursivamente los subgrupos
        return quicksort(izq) + [pivote] + quicksort(der)

# Función auxiliar para generar datos aleatorios con la misma semilla
# Así aseguramos que cada algoritmo reciba el mismo desorden
def generar_datos(n, semilla=123):
    random.seed(semilla)
    return [random.randint(1, 100000) for _ in range(n)]

# Tamaños que queremos comparar
tamaños = [1000, 10000, 20000]

# Encabezado de la tabla en consola
print("            1000        10000       20000")

# Algoritmo Burbuja
tiempos_burbuja = []
for tam in tamaños:
    datos = generar_datos(tam)
    inicio = time.time()
    burbuja(datos)
    fin = time.time()
    tiempos_burbuja.append(fin - inicio)

print(f"Burbuja     {tiempos_burbuja[0]:.4f}   {tiempos_burbuja[1]:.4f}   {tiempos_burbuja[2]:.4f}")

# Algoritmo Inserción
tiempos_insercion = []
for tam in tamaños:
    datos = generar_datos(tam)
    inicio = time.time()
    insercion(datos)
    fin = time.time()
    tiempos_insercion.append(fin - inicio)

print(f"Inserción   {tiempos_insercion[0]:.4f}   {tiempos_insercion[1]:.4f}   {tiempos_insercion[2]:.4f}")

# Algoritmo Selección
tiempos_seleccion = []
for tam in tamaños:
    datos = generar_datos(tam)
    inicio = time.time()
    seleccion(datos)
    fin = time.time()
    tiempos_seleccion.append(fin - inicio)

print(f"Selección   {tiempos_seleccion[0]:.4f}   {tiempos_seleccion[1]:.4f}   {tiempos_seleccion[2]:.4f}")

# Algoritmo QuickSort
tiempos_quick = []
for tam in tamaños:
    datos = generar_datos(tam)
    inicio = time.time()
    ordenada = quicksort(datos)  # Devuelve la lista ordenada
    fin = time.time()
    tiempos_quick.append(fin - inicio)

print(f"Rápido      {tiempos_quick[0]:.4f}   {tiempos_quick[1]:.4f}   {tiempos_quick[2]:.4f}")