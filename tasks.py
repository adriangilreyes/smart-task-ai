#creación de la tarea
from task import tasks

option = 0
cat_opcion = 0

while option != 4:
    #menú
    print('--------------------')
    print('1.Agregar Tareas')
    print('2.Eliminar Tareas')
    print('3.Listar Tareas') 
    print('4.Salir')
    print('--------------------')

    option = int(input('Introduce una opción:')) 
    
    if option == 1:
        name_task = input('Introduce el titulo de la tarea:')
        tasks.append(name_task)

        print('Selecciona categoría:')
        print('1.Trabajo')
        print('2.Estudio')
        print('3.Personal')

        cat_opcion = int(input('Introduce una categoría:'))

        if cat_opcion == 1:
            categoria = 'Trabajo'
        elif cat_opcion == 2:
            categoria = 'Estudio'
        elif cat_opcion == 3:
            categoria = 'Personal'
        else:
            categoria = 'Sin categoria'

        task = {
            "titulo":name_task,
            "cateogría": categoria
        }

        task.update(task) 


    elif option == 2:
        delete_task_title = input('Introduce el titulo a eliminar:')

        if delete_task_title in tasks:
            tasks.remove(delete_task_title)
        else:
            print('La tarea no existe')

    elif option == 3:
        print('Listado de tareas:')

        if len(tasks) == 0:
            print('No hay tareas')
        else:
            for task in enumerate(tasks):
                print(f'- {task}')

    elif option == 4:
        print('Saliendo....') 
        exit()
 