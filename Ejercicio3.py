# Ejercicio 3
# Escriba un programa que pida al usuario que ingrese una contraseña y que continúe 
# pidiéndola hasta que se ingrese correctamente. Al final debe imprimir un mensaje de éxito.
# Usar un bucle while.

def verificar_contrasena():
    contrasena_correcta = "python123"
    entrada = input("Ingrese su contraseña: ")

    while entrada != contrasena_correcta:
        print("Contraseña incorrecta. Intente de nuevo.")
        entrada = input("Ingrese la contraseña: ")
        
    print(f"¡Contraseña correcta!")

def main():
    verificar_contrasena()

if __name__ == "__main__":
    main()
