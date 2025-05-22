# EJEMPLO DE DATOS DE ESTACIONES (reemplaza esto con las reales si las tienes):
# Para cada línea, definimos una lista de estaciones ordenadas alfabéticamente
# para poder usar la búsqueda binaria.
# Notar que la "Id de estación" es su índice en la lista (empezando en 0).
lineas = {
    1: ["16 de Septiembre", "Agua Azul", "Auditorio", "Colón", "Oblatos", "San Juan de Dios"],
    2: ["Atlas", "Belenes", "Colón", "Hidalgo", "Juárez", "Refugio"],
    3: ["Arcos", "Gran Terraza", "La Calma", "Minerva", "Patria", "Zapopan Centro"],
    4: ["Américas", "Colón", "Minerva", "Plaza del Sol", "San Juan de Dios", "Vallarta"],
    5: ["Ávila Camacho", "Belisario", "Federalismo", "Garibaldi", "Refugio", "Zapopan Norte"],
    # Puedes agregar más líneas...
}

# ---------------------------------------------------------------------------------------
# Búsqueda Binaria (la usamos dentro de cada línea, que debe estar ORDENADA alfabéticamente)
# ---------------------------------------------------------------------------------------
def busqueda_binaria(lista, elemento):
    """Retorna el índice si 'elemento' está en 'lista' (ordenada). Si no, retorna -1."""
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

# ---------------------------------------------------------------------------------------
# Búsqueda Secuencial por líneas
# (Vamos línea por línea y dentro de cada línea hacemos binaria.)
# ---------------------------------------------------------------------------------------
def buscar_estacion(estacion_buscada):
    """
    Recorre cada línea (IdL) y hace búsqueda binaria de la estacion_buscada.
    Retorna una lista de tuplas (linea, indice_en_linea) donde se encontró la estación.
    """
    resultados = []
    for numero_linea, estaciones in lineas.items():
        # Hacemos la búsqueda binaria en la lista de estaciones
        indice = busqueda_binaria(estaciones, estacion_buscada)
        if indice != -1:
            # Si se encontró, agregamos a resultados (linea, índice)
            resultados.append((numero_linea, indice))
    return resultados

# ---------------------------------------------------------------------------------------
# EJEMPLO DE FLUJO PRINCIPAL
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Pedimos al usuario el nombre de la estación que busca
    estacion = input("¿Qué estación quieres buscar? ")

    # Buscamos en todas las líneas
    encontrados = buscar_estacion(estacion)

    if len(encontrados) == 0:
        # Si no se encontró en ningún lado
        print(f"{estacion} no existe")
    else:
        # Se encontró varias veces
        print(f"{estacion} se encuentra {len(encontrados)} veces")
        for (linea, idx) in encontrados:
            print(f"Línea: {linea}, Id de Estación: {idx}")