import itertools

class Stack:
    def __init__(self):
        self.items = []  # <-- IMPORTANTE

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

def leer_laberinto():
    n = int(input("Número de renglones (n): "))
    m = int(input("Número de columnas (m): "))

    lab = []
    entrada = None
    salida = None

    print("(1=muro, 0=pasillo, 2=entrada, 3=salida)")
    for i in range(n):
        fila = list(map(int, input(f"Fila {i}: ").split()))
        lab.append(fila)

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                entrada = (i, j)
            elif lab[i][j] == 3:
                salida = (i, j)
    return lab, entrada, salida

def resolver_con_orden(lab, entrada, salida, orden):
    if not entrada or not salida:
        return None

    stack = Stack()
    stack.push(entrada)
    visitado = set([entrada])
    ruta = []

    while not stack.empty():
        actual = stack.pop()
        ruta.append(actual)

        if actual == salida:
            return ruta

        for mov in orden:
            df, dc = mov
            nr = actual[0] + df
            nc = actual[1] + dc
            if 0 <= nr < len(lab) and 0 <= nc < len(lab[0]):
                if lab[nr][nc] != 1 and (nr, nc) not in visitado:
                    stack.push((nr, nc))
                    visitado.add((nr, nc))
                    break
    return None

def mostrar_ruta(ruta):
    if not ruta:
        print("No se encontró ruta.")
        return
    for pos in ruta:
        print(pos, end=" -> ")
    print("FIN")

def main():
    lab, entrada, salida = leer_laberinto()
    if not entrada or not salida:
        print("No se encontró la entrada (2) o la salida (3).")
        return

    # a) Orden fijo (AR, D, AB, I)
    orden_a = [(-1,0), (0,1), (1,0), (0,-1)]
    print("\n(a) Ruta con orden AR, D, AB, I:")
    ruta_a = resolver_con_orden(lab, entrada, salida, orden_a)
    mostrar_ruta(ruta_a)

    # b y c) Probar todas las permutaciones
    base = [(-1,0), (0,1), (1,0), (0,-1)]
    todas_permutaciones = list(itertools.permutations(base))
    mejor_ruta = None
    mejor_orden = None

    for perm in todas_permutaciones:
        r = resolver_con_orden(lab, entrada, salida, perm)
        if r is not None:
            if (mejor_ruta is None) or (len(r) < len(mejor_ruta)):
                mejor_ruta = r
                mejor_orden = perm

    print("\n(b) y (c) Ruta más corta (probando todas permutaciones):")
    if mejor_ruta is None:
        print("Ninguna permutación encontró ruta.")
    else:
        print("Mejor orden de búsqueda:", mejor_orden)
        print(f"Longitud de la ruta: {len(mejor_ruta)}")
        mostrar_ruta(mejor_ruta)

if __name__ == "__main__":
    main()
