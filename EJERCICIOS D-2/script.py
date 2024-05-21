def read_contributors(archivo):
    try:
        with open(archivo, 'r') as file:
            colaboradores = file.readlines()
        colaboradores = [colaborador.strip() for colaborador in colaboradores]
        return colaboradores
    except FileNotFoundError:
        return []

def show_collaborators(colaboradores, cantidad=2):
    for i, colaborador in enumerate(colaboradores[:cantidad]):
        print(f"{i+1}. {colaborador}")

def add_collaborators(archivo, nuevo_colaborador, max_colaboradores=15):
    colaboradores = read_contributors(archivo)
    if len(colaboradores) < max_colaboradores:
        with open(archivo, 'a') as file:
            file.write(nuevo_colaborador + '\n')
        print(f"{nuevo_colaborador} ha sido agregado.")
    else:
        print("No se puede agregar más colaboradores. Se ha alcanzado el máximo permitido.")

def main():
    archivo = 'colaboradores.txt'
    colaboradores = read_contributors(archivo)

    if not colaboradores:
        print("No se encontraron colaboradores en el archivo.")
        return

    show_collaborators(colaboradores)

    nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador (o presione Enter para omitir): ").strip()
    if nuevo_colaborador:
        add_collaborators(archivo, nuevo_colaborador)

if __name__ == "__main__":
    main()
