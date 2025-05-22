#1Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
def convertidor_binario():
    input_decimal = input("Introduzca un número decimal:")
    nro_decimal = int(input_decimal)
    binario = bin(nro_decimal)
    resultado = binario[2:]
    print(f"{nro_decimal} en binario es {resultado}")
   
def convertidor_decimal():
    input_binario = input("Introduzca un número binario:")
    nro_decimal = int(input_binario, 2)
    print(f"{input_binario} en decimal es {nro_decimal}")
   
if __name__ == "__main__":
    print ("Seleccione una opción:")
    print ("1. Convertir decimal a binario")
    print ("2. Convertir binario a decimal")
    opcion = input("Opción: ")
    if opcion == "1":
        convertidor_binario()
    elif opcion == "2":
        convertidor_decimal()
    else:
        print("Opción no válida")