tareas=[]
def menu():
    print("\nQue quieres hacer ")
    print("1.Revisar tareas")
    print("2.Agregar tareas")
    print("3.Completar tareas")
    print("4.Eliminar tareas")
    print("5.Salir")

def revisa_tareas():
       separador="\n"
       if len(tareas)==0:
            print("\nNo existen tareas por realizar")
       else:
            lista_tareas=separador.join(tareas)
            print(lista_tareas)

def agregar_tareas():
     nueva_tarea = input("\nQue deseas agregar: ")
     nueva_tarea=nueva_tarea.capitalize()
     new_tarea = f"- {nueva_tarea}"
     tareas.append(new_tarea)

def marcar_tareas():
     separador="\n"
     if len(tareas)==0:
            print("\nNo existen tareas por marcar")
     else:
            lista_tares=separador.join(tareas)
            print(lista_tares)
            tareaCompletada=int(input("\nQue tarea quieres marcar como completada?: "))
            eleccion=tareaCompletada-1
            tareas[eleccion] = tareas[eleccion] + " (Completada)"
            print(f"Tarea '{tareas[eleccion].replace(' (Completada)', '')}' marcada como completada.")
                 
def eliminar_tareas():
     separador="\n"
     if len(tareas)==0:
            print("\nNo existen tareas por eliminar")
     else:
            lista_tares=separador.join(tareas)
            print(lista_tares)
            eliminarTarea=int(input("Que tarea quieres eliminar?: "))
            eleccion=eliminarTarea-1
            tareaEliminada=tareas.pop(eleccion)

while True:
    menu()
    try:
        opcion=int(input("Eligue una opcion:"))
        if opcion==1:
             revisa_tareas()
        elif opcion==2:
             agregar_tareas()
        elif opcion==3:
             marcar_tareas()
        elif opcion==4:
             eliminar_tareas()
        elif opcion==5:
            break
    except ValueError:
         print("\nError: Por favor, introduce solo un número.")

