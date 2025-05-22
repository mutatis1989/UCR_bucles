# Ejercicio 2
# Escriba un programa que reciba un número entero positivo desde el teclado e imprima
# todos los números impares desde el 1 hasta ese número (inclusive), separados por comas.

def imprimir_impares():
    numero = int(input("Ingrese un número entero positivo: "))
    
    i = 1
    while i <= numero:
        if i % 2 != 0:
            if i + 2 <= numero:
                print(i, end=", ")
            else:
                print(i)
        i += 1

def main():
    imprimir_impares()

if __name__ == "__main__":
    main()
