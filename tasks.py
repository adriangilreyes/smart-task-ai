import datetime
import json

#diccionario de tareas
tasks = {}

#id de la tarea
id_task = 0

option = 0

try:
    with open("tasks.json","r") as f:
        tasks = json.load(f) 

except(FileNotFoundError, json.JSONDecodeError):
    tasks = {}


while True:
    print('---------------')
    print('1. Añadir tarea')
    print('2. Eliminar tarea')
    print('3. Listar tareas')
    print('4. Salir')
    print('----------------') 
    option = int(input('Introduce una opción:'))

    if option == 1:
        user_name = input('Introduce un nombre:')
        id_task = id_task + 1
        name_task = input('Introduce el nombre de la tarea:')
        category_task = input('Introduce la categoría de la tarea:')
        priority_task = input('Introduce la prioridad de la tarea:')
        hour = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        tasks[id_task] = {"user_name":user_name,"id":id_task, "name_task":name_task,"category_task":category_task,"priority_task":priority_task,
        "datetime:":hour}

        with open ("tasks.json","w") as f:
            json.dump(tasks,f, indent = 4) 
    
    elif option == 2:
        id_to_delete = int(input('Introduce el id a eliminar:'))
        del tasks[id_to_delete]

    elif option == 3:
        for task in tasks.items():
            print(task)
    
    elif option == 4:
        print('Saliendo....',user_name) 
        exit()