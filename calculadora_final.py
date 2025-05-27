import os
ciclo = True
while ciclo == True:
    try:
        opc = int(input("--CALCULADORA--\n(1)Sumar.\n(2)Restar.\n(3)Multiplica.\n(4)Dividir.\n(5)Suma de tres números\n (6)Salir: "))
        os.system("cls")

        match opc:
            case 1:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    print(f"La suma de ambos números es: {n1 + n2}")
                except ValueError:
                    print("¡El número debe ser entero!")
            case 2:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    print(f"La resta de ambos números es: {n1 - n2}")
                except ValueError:
                    print("¡El número debe ser entero!")
            case 3:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    print(f"La multiplicación de ambos números es. {n1 * n2}")
                except ValueError:
                    print("¡El número debe ser entero!")
            case 4:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    print(f"La división de ambos números es. {n1 // n2}")
                except ValueError:
                    print("¡El número debe ser entero!")
            case 5:
                try:
                    n1 = int(input("Ingrese el primer número: "))
                    n2 = int(input("Ingrese el segundo número: "))
                    n3 = int(input("Ingrese el tercer número: "))
                    print(f"La suma de ambos números es: {n1 + n2 + n3}")
                except ValueError:
                    print("¡El número debe ser entero!")
            case 6:
                print("¡Adios!")
                break
    except ValueError:
        print("ERROR")