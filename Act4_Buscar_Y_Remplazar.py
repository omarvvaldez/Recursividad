def boyer_moore_horspool(texto, patron):
    """
    Implementación simple de Boyer Moore Horspool (BMH).
    Retorna una lista con las posiciones (índices) donde aparece 'patron' en 'texto'.
    """

    # Preparamos la 'tabla de desplazamiento' (last occurrence) para cada carácter
    # Esta tabla dice: si aparece un caracter c que no coincide, ¿cuántos caracteres me puedo saltar?
    # Por defecto, saltamos el largo del patron.
    m = len(patron)
    n = len(texto)

    # Si el patrón es más largo que el texto, no hay coincidencias
    if m > n:
        return []

    # Construimos la tabla con desplazamiento = m para todos.
    tabla = {chr(i): m for i in range(256)}  # para caracteres ASCII
    # Para cada caracter del patrón (excepto el último), decimos m - i - 1
    for i in range(m - 1):
        tabla[patron[i]] = m - 1 - i

    posiciones = []
    i = 0  # índice en el texto

    while i <= n - m:
        # Empezamos comparando desde el final del patrón
        j = m - 1
        while j >= 0 and texto[i + j] == patron[j]:
            j -= 1

        if j < 0:
            # Significa que todo coincidió
            posiciones.append(i)
            # Avanzamos i según la tabla del último caracter
            # o 1 si ya coincidimos
            i += tabla.get(texto[i + m - 1], m)
        else:
            # Desplazamiento según el caracter conflictivo
            c = texto[i + j]
            saltar = tabla.get(c, m)
            i += saltar

    return posiciones


if __name__ == "__main__":
    # Pedimos el texto de entrada
    print("Ingresa el texto (párrafo) donde buscaremos:")
    texto_original = input("> ")

    # Pedimos la cadena a buscar y la de reemplazo
    print("¿Qué cadena deseas buscar?")
    cadena_buscar = input("> ")

    print("¿Por cuál deseas reemplazarla?")
    cadena_reemplazar = input("> ")

    # Aplicamos BMH para encontrar todas las posiciones
    posiciones = boyer_moore_horspool(texto_original, cadena_buscar)

    if not posiciones:
        # Si no hubo coincidencias
        print(f"No se encontró la cadena '{cadena_buscar}'.")
    else:
        print(f"Se encontraron {len(posiciones)} coincidencias de '{cadena_buscar}':")

        # Para ir reemplazando, convertimos a lista (así manejamos el texto como mutable)
        # Pero para no confundirnos con los índices que cambian al reemplazar,
        # iremos construyendo el nuevo texto con trozos.
        texto_final = []
        ultima_pos = 0

        # Vamos recorriendo las posiciones en orden
        for idx, pos in enumerate(posiciones, start=1):
            print(f"{idx} coincidencia, posición {pos}, cambiar (S/N): ", end="")
            opcion = input().strip().upper()

            # Agregamos al texto_final todo lo que hay desde ultima_pos hasta pos
            texto_final.append(texto_original[ultima_pos:pos])

            if opcion == "S":
                # Si el usuario dice Sí, reemplazamos
                texto_final.append(cadena_reemplazar)
            else:
                # De lo contrario, dejamos el texto tal cual
                texto_final.append(cadena_buscar)

            # Actualizamos ultima_pos para continuar
            # Nos movemos pos + longitud del patron original
            ultima_pos = pos + len(cadena_buscar)

        # Agregamos lo que falte del final
        texto_final.append(texto_original[ultima_pos:])

        # Unimos todo en un string final
        resultado = "".join(texto_final)

        print("\n-- TEXTO RESULTANTE --\n")
        print(resultado)