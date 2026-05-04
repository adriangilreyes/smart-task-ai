import datetime

#diccionario de tareas
tasks = {}

#id de la tarea
id_task = 0

option = 0

while True:

    print('1. Añadir tarea')
    print('2. Eliminar tarea')
    print('3. Listar tareas')
    print('4. Salir')

    option = int(input('Introduce una opción:'))

    if option == 1:
        id_task = id_task + 1
        name_task = input('Introduce el nombre de la tarea:')
        category_task = input('Introduce la categoría de la tarea:')
        priority_task = input('Introduce la prioridad de la tarea:')
        hour = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        tasks[id_task] = {"id":id_task, "name_task":name_task,"category_task":category_task,"priority_task":priority_task,
        "datetime:":hour}
    
    elif option == 2:
        id_to_delete = int(input('Introduce el id a eliminar:'))
        del tasks[id_to_delete]

    elif option == 3:
        for task in tasks.items():
            print(task)
    
    elif option == 4:
        print('Saliendo....')
        exit()