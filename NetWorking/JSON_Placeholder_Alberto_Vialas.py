import requests

#Hacemos la request para los datos del usuario
def obtener_informacion_usuario(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Usuario no encontrado. Código de estado: {response.status_code}")
        return None

#Mostramso los datos del usuario obreniso
def mostrar_datos_personales(user_info):
    print(f"Nombre y apellidos: {user_info['name']}")
    print(f"Dirección completa: {user_info['address']['street']}, {user_info['address']['suite']}, {user_info['address']['city']}, {user_info['address']['zipcode']}")
    print(f"Teléfono: {user_info['phone']}")

#Mostramos las opciones de tareas
def mostrar_tareas(user_id):
    print("Seleccione una opción:")
    print("1. Tareas completadas")
    print("2. Tareas no completadas")
    opcion = input("Seleccione una opción (1/2): ")
    if opcion == '1':
        mostrar_tareas_completadas(user_id)
    elif opcion == '2':
        mostrar_tareas_no_completadas(user_id)
    else:
        print("Opción no válida")

#Hacemos la request de las tareas completadas y las mostramos
def mostrar_tareas_completadas(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed=true"
    response = requests.get(url)
    if response.status_code == 200:
        tareas = response.json()
        if tareas:
            print("Tareas completadas:")
            for tarea in tareas:
                print(f"ID: {tarea['id']} - Título: {tarea['title']}")
        else:
            print("No hay tareas completadas para este usuario")
    else:
        print("Error al obtener las tareas. Código de estado: {response.status_code}")

#Hacemos la request de las tareas no completadas y las mostramos
def mostrar_tareas_no_completadas(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed=false"
    response = requests.get(url)
    if response.status_code == 200:
        tareas = response.json()
        if tareas:
            print("Tareas no completadas:")
            for tarea in tareas:
                print(f"ID: {tarea['id']} - Título: {tarea['title']}")
        else:
            print("No hay tareas no completadas para este usuario")
    else:
        print("Error al obtener las tareas. Código de estado: {response.status_code}")

#Hacemos la request de los post, y los mostramos
def mostrar_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        if posts:
            print("Posts:")
            for post in posts:
                print(f"Título: {post['title']}")
                print(f"Contenido: {post['body']}")
                mostrar_comentarios(post['id'])
        else:
            print("No hay posts para este usuario")
    else:
        print("Error al obtener los posts. Código de estado: {response.status_code}")

#Hacemos la request de los comentarios y los mostramos
def mostrar_comentarios(post_id):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        comentarios = response.json()
        if comentarios:
            print("Comentarios:")
            for comentario in comentarios:
                print(f"Nombre: {comentario['name']}")
                print(f"Email: {comentario['email']}")
                print(f"Comentario: {comentario['body']}")
        else:
            print("No hay comentarios para este post")
    else:
        print("Error al obtener los comentarios. Código de estado: {response.status_code}")

#Iniciamos el menú
while True:
        user_id = input("Ingrese el ID de un usuario o escriba 'exit' para salir: ")
        if user_id == "exit":
            break
        user_info = obtener_informacion_usuario(user_id)
        while True:
            if user_info:
                print(f"¿Qué desea ver de {user_info['name']}?")
                print("1. Datos personales")
                print("2. Tareas pendientes")
                print("3. Posts")
                print("4. Volver a elegir ID")
                
                opcion = input("Seleccione una opción (1/2/3/4): ")
                
                if opcion == '1':
                    mostrar_datos_personales(user_info)
                elif opcion == '2':
                    mostrar_tareas(user_id)
                elif opcion == '3':
                    mostrar_posts(user_id)
                elif opcion == '4':
                    break
                else:
                    print("Opción no válida")