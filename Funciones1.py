#Ejercicios Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
# y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calculadoradeIVA():
    cantidad_input = input("Ingrese la cantidad sin IVA: ")
    cantidad_sin_iva = float(cantidad_input)
    porcentaje_input = input("Ingrese el porcentaje de IVA o presione enter si no quiere ingresar uno: ")
    if porcentaje_input.strip() == "":
        porcentaje_iva = 21
    else:
        porcentaje_iva = float(porcentaje_input)
    total = cantidad_sin_iva * (1 + (porcentaje_iva / 100))
    return total

if __name__ == "__main__":
    resultado = calculadoradeIVA()
    print(f"El total con IVA es: {resultado:.2f}")         