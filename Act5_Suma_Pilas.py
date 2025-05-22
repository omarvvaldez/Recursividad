
class Stack:
    def __init__(self):
        self.items = []  # ¡Definimos la lista interna!

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.empty():
            return None
        return self.items.pop()

    def empty(self):
        return (len(self.items) == 0)


def sumar_strings_con_pilas(numA, numB):
    """
    Suma dos números (strings) de longitud variable (solo la parte entera).
    No utiliza ceros para rellenar; usa pilas y si una pila se vacía, asumimos 0.
    """
    pilaA = Stack()
    pilaB = Stack()

    # Empujamos dígito por dígito a cada pila
    for d in numA:
        pilaA.push(int(d))
    for d in numB:
        pilaB.push(int(d))

    carry = 0
    resultado = []

    # Mientras haya dígitos en A o B o un carry pendiente
    while (not pilaA.empty()) or (not pilaB.empty()) or (carry != 0):
        # Si la pila está vacía, es como si fuera cero
        x = pilaA.pop()
        if x is None:
            x = 0

        y = pilaB.pop()
        if y is None:
            y = 0

        s = x + y + carry
        carry = s // 10
        resultado.append(s % 10)

    # El resultado está al revés, invertimos
    resultado.reverse()
    # Convertimos a string
    return "".join(str(d) for d in resultado)


def sumar_decimales(num1, num2):
    """
    Suma dos números con parte decimal usando la función de pilas anterior.
    Cada parte (entera y decimal) puede tener distinta longitud. Maneja carry 
    que puede venir de la parte fraccionaria y pasar a la parte entera.
    """
    # Dividimos parte entera y decimal
    if '.' in num1:
        ent1, dec1 = num1.split('.', 1)
    else:
        ent1, dec1 = num1, ""

    if '.' in num2:
        ent2, dec2 = num2.split('.', 1)
    else:
        ent2, dec2 = num2, ""

    # Suma de la parte entera
    suma_entera = sumar_strings_con_pilas(ent1, ent2)

    # Suma de la parte decimal "al revés"
    dec_rev1 = dec1[::-1]
    dec_rev2 = dec2[::-1]
    suma_dec = sumar_strings_con_pilas(dec_rev1, dec_rev2)
    # Revertimos el resultado decimal
    suma_dec = suma_dec[::-1]

    # Verificar si la suma decimal generó un dígito extra (carry)
    max_dec_len = max(len(dec1), len(dec2))
    if len(suma_dec) > max_dec_len:
        # Primer dígito de la suma decimal es un carry a la parte entera
        carry_entero = suma_dec[0]  # char
        suma_dec = suma_dec[1:]     # quitamos ese dígito
        # sumamos ese carry a la parte entera
        suma_entera = sumar_strings_con_pilas(suma_entera, carry_entero)

    # Si la parte decimal quedó vacía, solo retornamos la parte entera
    if suma_dec == "":
        return suma_entera
    else:
        return suma_entera + "." + suma_dec


if __name__ == "__main__":
    print("=== Suma de números con parte decimal usando PILAS ===")

    n1 = input("Ingresa el primer número (puede tener decimal): ")
    n2 = input("Ingresa el segundo número (puede tener decimal): ")

    resultado = sumar_decimales(n1, n2)
    print(f"La suma es: {resultado}")


