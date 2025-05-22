# Escribir una función que calcule el área de un círculo
# y otra que calcule el volumen de un cilindro usando la primera función.

def calcular_circulo(radio):
    area = 3.14 * radio ** 2
    return area

def calcular_cilindro(radio, altura):
    base = calcular_circulo(radio)
    volumen = base * altura
    return volumen

# Bloque principal con menú interactivo
if __name__ == "__main__":
    print("Elija una opción:")
    print("1. Calcule el área de un círculo")
    print("2. Calcule el volumen de un cilindro")
    opcion = input("Ingrese 1 o 2: ")

    if opcion == "1":
        radio = int(input("Ingrese el radio del círculo: "))
        area = calcular_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    elif opcion == "2":
        radio = int(input("Ingrese el radio de la base del cilindro: "))
        altura = int(input("Ingrese la altura del cilindro: "))
        volumen = calcular_cilindro(radio, altura)
        print(f"El volumen del cilindro es: {volumen:.2f}")
    else:
        print("Opción inválida")
