import random

def guess_number():
    secret_number = random.randint(1, 100)
    intentos = 0
    
    print("¡Adivina el número secreto entre 1 y 100!")

    while True:
        intento = int(input("Ingresa tu intento: "))
        intentos += 1

        if intento < secret_number:
            print("El número es demasiado bajo. ¡Intenta de nuevo!")
        elif intento > secret_number:
            print("El número es demasiado alto. ¡Intenta de nuevo!")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número secreto {secret_number} en {intentos} intentos!")
            break

guess_number()
