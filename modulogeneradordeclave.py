import random
import string

def password_generator(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contraseña = password_generator(longitud)
    print("Contraseña generada:", contraseña)

if __name__ == "__main__":
    main()
