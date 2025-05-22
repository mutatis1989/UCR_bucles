# Ejercicio 1: Imprima un árbol de navidad formado con * haciendo uso del while y de la multiplicacón
# de un entero por una cadena, cuyo resultado en Python es replicar la cadena.

def arbol_navidad(n):
    i = 1
    while i <= n:
        print(" " * (n - i) + "*" * (2 * i - 1))
        i += 1

def main():
    n = int(input("¿Qué tan alto quiere que sea su árbol? "))
    arbol_navidad(n)

if __name__ == "__main__":
    main()