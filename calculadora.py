import operaciones
# calculadora.py

def mostrar_menu():
    print("\nCalculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo...")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print(f"Resultado: {operaciones.suma(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {operaciones.resta(num1, num2)}")
    elif opcion == "3":
        print(f"Resultado: {operaciones.multiplicacion(num1, num2)}")
    elif opcion == "4":
        print(f"Resultado: {operaciones.division(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")
