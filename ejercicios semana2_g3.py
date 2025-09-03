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

# =========================
# 2. Juego FizzBuzz

def fizzbuzz():
    while True:
        print("\n--- JUEGO FIZZBUZZ ---")
        print("1. Ejecutar")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            for i in range(1, 101):
                if i % 3 == 0 and i % 5 == 0: print("FizzBuzz")
                elif i % 3 == 0: print("Fizz")
                elif i % 5 == 0: print("Buzz")
                else: print(i)
        elif op == "2": break

# =========================
# 3. Calculadora Simple

def calculadora():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Calcular")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            a, b = float(input("Num1: ")), float(input("Num2: "))
            opn = input("Operación (+,-,*,/): ")
            if opn == "+": print(a+b)
            elif opn == "-": print(a-b)
            elif opn == "*": print(a*b)
            elif opn == "/": print("∞" if b==0 else a/b)
        elif op == "2": break

# =========================
# 4. Control de Temperatura

import time, random
def invernadero():
    while True:
        print("\n--- CONTROL TEMPERATURA ---")
        print("1. Iniciar simulación")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            for _ in range(5):
                t = random.randint(5, 35)
                if t < 10: print(f"{t}°C → Calefactor ON")
                elif t > 25: print(f"{t}°C → Ventilador ON")
                else: print(f"{t}°C → Inactivo")
                time.sleep(1)
        elif op == "2": break

# =========================
# 5. Detección de Intrusos

def intrusos():
    while True:
        print("\n--- DETECCIÓN DE INTRUSOS ---")
        print("1. Activar sistema")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            noche = True
            for _ in range(5):
                sensores = [random.choice([True, False]) for _ in range(3)]
                if sum(sensores) >= 2 and noche: print(sensores, "→ Alarma ACTIVADA")
                else: print(sensores, "→ Sin alarma")
                time.sleep(1)
        elif op == "2": break

# =========================
# 6. Control de Luces

def luces():
    while True:
        print("\n--- CONTROL DE LUCES ---")
        print("1. Simular")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            for _ in range(5):
                noche, mov = random.choice([True, False]), random.choice([True, False])
                if noche and mov: print("Noche+Mov → Luces ON")
                else: print("Luces OFF")
                time.sleep(1)
        elif op == "2": break

# =========================
# 7. Aire Acondicionado

def aire():
    while True:
        print("\n--- AIRE ACONDICIONADO ---")
        print("1. Simular")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            for _ in range(5):
                t, h = random.randint(20, 35), random.randint(30, 80)
                if (t > 28 and h > 60) or t > 30:
                    print(f"{t}°C {h}% → Aire ON")
                else: print(f"{t}°C {h}% → Aire OFF")
                time.sleep(1)
        elif op == "2": break

# =========================
# 8. Control de Acceso

def acceso():
    while True:
        print("\n--- CONTROL DE ACCESO ---")
        print("1. Simular")
        print("2. Volver")
        op = input("Elija: ")
        if op == "1":
            for _ in range(5):
                tiene_m, horario, empleado = random.choice([True, False]), random.choice([True, False]), random.choice([True, False])
                if (tiene_m and horario) or empleado: print("Acceso PERMITIDO")
                else: print("Acceso DENEGADO")
                time.sleep(1)
        elif op == "2": break

# =========================
# MENÚ PRINCIPAL

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Sistema de Reservas")
        print("2. FizzBuzz")
        print("3. Calculadora")
        print("4. Invernadero")
        print("5. Intrusos")
        print("6. Luces")
        print("7. Aire Acondicionado")
        print("8. Control de Acceso")
        print("9. Salir")
        op = input("Elija: ")
        if op == "1": sistema_reservas()
        elif op == "2": fizzbuzz()
        elif op == "3": calculadora()
        elif op == "4": invernadero()
        elif op == "5": intrusos()
        elif op == "6": luces()
        elif op == "7": aire()
        elif op == "8": acceso()
        elif op == "9": break

menu()
