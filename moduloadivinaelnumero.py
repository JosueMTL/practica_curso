import random

def adivinar_numero():
    # Generar un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    print("¡Adivina el número secreto entre 1 y 100!")

    while True:
        # Pedir al usuario que ingrese un número
        intento = int(input("Ingresa tu intento: "))
        intentos += 1

        # Comparar el número ingresado con el número secreto
        if intento < numero_secreto:
            print("El número es demasiado bajo. ¡Intenta de nuevo!")
        elif intento > numero_secreto:
            print("El número es demasiado alto. ¡Intenta de nuevo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número secreto {numero_secreto} en {intentos} intentos!")
            break

# Ejecutar la función principal
adivinar_numero()
