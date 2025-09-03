# 1. Sistema de Reservas


def sistema_reservas():
    capacidad, reservas = 5, 0
    while True:
        print("\n--- SISTEMA DE RESERVAS ---")
        print("1. Reservar asiento")
        print("2. Reiniciar")
        print("3. Salir")
        op = input("Elija: ")
        if op == "1":
            if reservas < capacidad:
                reservas += 1
                print(f"Asiento reservado. {capacidad - reservas} disponibles.")
            else:
                print("No hay asientos disponibles.")
        elif op == "2": reservas = 0
        elif op == "3": break
