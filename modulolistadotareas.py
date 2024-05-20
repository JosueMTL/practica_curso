def mostrar_tareas(tareas):
    if tareas:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas pendientes.")

def agregar_tarea(tareas, tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada con éxito.")

def eliminar_tarea(tareas, indice):
    if 1 <= indice <= len(tareas):
        tarea_eliminada = tareas.pop(indice - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada correctamente.")
    else:
        print("Índice de tarea inválido.")

def main():
    tareas = []
    
    while True:
        print("\n*** Administrador de Tareas ***")
        print("1. Mostrar tareas pendientes")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            tarea_nueva = input("Ingrese la nueva tarea: ")
            agregar_tarea(tareas, tarea_nueva)
        elif opcion == "3":
            mostrar_tareas(tareas)
            if tareas:
                indice_eliminar = int(input("Ingrese el número de la tarea a eliminar: "))
                eliminar_tarea(tareas, indice_eliminar)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
