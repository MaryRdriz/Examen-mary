import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 1 y 50): "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Felicidades! adivinaste el número en", intentos, "intentos.")
        break
    elif intento < numero_secreto:
        print("Intenta con un numero mayor. Intenta de nuevo.")
    else:
        print("Intenta con un numero menor. Intenta de nuevo.")