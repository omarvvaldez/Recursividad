def opcion1():
    print("\nPlanteamiento: Dado un numero n, obtener el factorial del mismo.")
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    x = int(input("Ingresa un numero para obtener su factorial: "))
    if x < 0:
        print("No funciona con numeros negativos.")
    else:
        print(f"\nEl factorial de {x} es: {factorial(x)}")

def opcion2():
    print("\nPlanteamiento: Dado un número n, obtener su sumatoria.")
    
    def sumatoria(n):
        if n == 0:
            return 0
        else:
            return n + sumatoria(n - 1)

    x = int(input("Ingresa un numero para obtener su sumatoria: "))
    if x < 0:
        print("No funciona con numeros negativos.")
    else:
        print(f"\nLa sumatoria de {x} es: {sumatoria(x)}")
    
def opcion3():
    print("\nPlanteamiento: Dados dos números x y n, obtener x elevado a la potencia n (utilizando multiplicaciones).")
    
    def potencia(x, n):
        if n == 0:
            return 1  # La potencia de cualquier número elevado a 0 es 1
        else:
            return x * potencia(x, n - 1)

    x = int(input("Ingresa un numero: "))
    y = int(input("Ingresa su exponente: "))

    if y < 0:
        print("No funciona con numeros negativos.")
    else:
        print(f"{x} elevado a la {y} es: {potencia(x, y)}")
    
def opcion4():
    print("\nPlanteamiento: Dados dos números m y n, obtener la multiplicación de m por n (utilizando solo sumas).")
    
    def multiplicacion(x, n):
        if n == 0:
            return 0
        else:
            return x + multiplicacion(x, n - 1)

    x = int(input("Ingresa un numero: "))
    y = int(input("Ingresa su multiplo: "))

    if y < 0:
        print("No funciona con numeros negativos.")
    else:
        print(f"{x} multiplicado por {y} es: {multiplicacion(x, y)}")
    
def opcion5():
    print("\nPlanteamiento: Dados dos números m y n, obtener la división de m entre n (considerar que m siempre será mayor que n; m,n > 0; m es múltiplo de n para garantizar la divisón entera).")
    
    def division(m, n):
        if m == 0:
            return 0
        else:
            return 1 + division(m - n, n)

    m = int(input("Ingresa un numero: "))
    n = int(input("Ingresa su divisor: "))

    if m <= 0 or n <= 0:
        print("Ambos números deben ser mayores que 0.")
    elif m % n != 0:
        print("Los números deben ser múltiplos.")
    else:
        resultado = division(m, n)
        print(f"{m} entre {n} es: {resultado}")

def opcion6():
    print("\nPlanteamiento: Dada una frase (string) determinar si es palíndromo.")
    
    def es_palindromo(frase):
        frase = frase.replace(" ", "").lower()
        
        if len(frase) <= 1:
            return True
        
        if frase[0] != frase[-1]:
            return False
        
        return es_palindromo(frase[1:-1])
    
    frase = input("Ingresa una frase: ")
    
    if es_palindromo(frase):
        print("\nLa frase es un palíndromo.")
    else:
        print("\nLa frase NO es un palíndromo.")

def opcion7():
    print("\nPlanteamiento: Dada una frase (string), invertirla.")
    
    def invertir(frase):
        if len(frase) == 0:
            return ""
        
        return frase[-1] + invertir(frase[:-1])
    
    frase = input("Ingresa una frase: ")
    print(f"\nFrase invertida: {invertir(frase)}")

def opcion8():
    print("\nPlanteamiento: Implementar, con recursividad, una función \nque haga lo mismo que un ciclo for.")
    print("para este haremos una funcion que despliegue \nuna serie de numeros dependiendo un intervalo.")
    
    def ciclo_for(inicio, fin):
        if inicio > fin:
            return
        
        print(inicio, end=" ")
        ciclo_for(inicio + 1, fin)
    
    inicio = int(input("Ingresa el inicio: "))
    fin = int(input("Ingresa el fin: "))
    ciclo_for(inicio, fin)
    print()

def opcion9():
    print("\nPlanteamiento: Dado un número n, desplegar los primeros n números\n de la serie de Fibonacci.")
    
    def fib(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fib(num - 1) + fib(num - 2)
        
    n = int(input("Ingresa la posicion a conocer en Fibonacci: "))  
    
    if n < 0:
        print("El número debe ser no negativo.")
    else:
        for i in range(n):  
            print(fib(i))  


def menu():
    while True:
        print("\n--- Funciones Recursivas ---")
        print("1. Factorial")
        print("2. Sumatoria")
        print("3. Potencia")
        print("4. Multiplicacion")
        print("5. Division")
        print("6. Palindromo")
        print("7. Invertir Frase")
        print("8. Funcion ciclo for")
        print("9. Serie Fibonacci")
        print("10. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            opcion1()
        elif opcion == '2':
            opcion2()
        elif opcion == '3':
            opcion3()
        elif opcion == '4':
            opcion4()
        elif opcion == '5':
            opcion5()
        elif opcion == '6':
            opcion6()
        elif opcion == '7':
            opcion7()
        elif opcion == '8':
            opcion8()
        elif opcion == '9':
            opcion9()
        elif opcion == '10':
            print("Saliendo del menú...")
            break
        else:
            print("No existe esa opción, intenta de nuevo.")

menu()
