#creación de la tarea

tasks = []

option = 0

while option != 4:

    option = int(input('Introduce una opción:'))
    print('1.Agregar Tareas')
    print('2.Eliminar Tareas')
    print('3.Listar Tareas')
    print('4.Salir')

    if option == 1:
        name_task = input('Introduce el titulo de la nota:')
        tasks.append(name_task)

    if option == 2:
        delete_task_title = input('Introduce el titulo a eliminar:')
        tasks.remove(delete_task_title)

    if option == 3:
      tasks.append(name_task)
      print(tasks)

    if option == 4:
        exit()
