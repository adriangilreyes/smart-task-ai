#creación de la tarea 

prioridades = ['Baja','Media','Alta']

option = 0
cat_opcion = 0
prioridad = 0
id = 0

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
        task.add(name_task)
        id = id + 1

        task = { "id":id,"titulo":name_task, "cateogría": categoria, "prioridad":prioridad}

        print('Selecciona categoría:')
        print('--------------------')
        print('1.Trabajo')
        print('--------------------')
        print('2.Estudio')
        print('--------------------')
        print('3.Personal')

        cat_opcion = int(input('Introduce una categoría:'))

        prioridad = int(input('Introduce la prioridad de la tarea:'))
        
        if prioridad in prioridades:
            if prioridad == 1:
                prioridad = 'Baja'

            elif prioridad == 2:
                prioridad = 'Media'

            elif prioridad == 3:
                prioridad = 'Alta'
            
            else:
                print('La prioridad no es válida')
        
        if cat_opcion == 1:

            categoria = 'Trabajo'
        
        elif cat_opcion == 2:
            categoria = 'Estudio'
        
        elif cat_opcion == 3:
            categoria = 'Personal'
        
        else:
            categoria = 'Sin categoria'

    elif option == 2:
        delete_task_title = input('Introduce el id a eliminar:') 

        if delete_task_title in tasks:
            del task[id]
        else:
            print('El id no existe')

    elif option == 3:
        print('Listado de tareas:')

        if len(tasks) == 0:
            print('No hay tareas')
        else:
            for task in task.items():
                print(task)

    elif option == 4: 
        print('Saliendo....')  
        exit() 
 