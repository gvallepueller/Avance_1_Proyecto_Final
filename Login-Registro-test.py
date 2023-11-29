# Una empresa necesita registrar a sus trabajadores, sus clientes y por ultimo a los administradores del sistema. Los trabajadores tendrán en sus datos: nombre, apellido, profesión, puesto, dni, nombre de usuario y contraseña. Los clientes tendrán solo nombre de usuario y contraseña. El administrador tendrá nombre de usuario, contraseña y rango. 



# 1. Se usa "import json" para poder adquirir los métodos ".dumps" que permitirá converir un diccionario de Python a JSON y el método ".loads" para covertir una cadena JSON a un diccionario de Python:
import json

# ______________________________________________________________
# 2. Creamos las funciones para la carga y lectura de los datos:

def cargar_datos(): # Función para cargar datos desde el archivo JSON
    
    try: # se maneja una excepción
        with open("data.json", "r") as archivo: # se abre el archivo JSON y se indica aque está solo en lectura.
            datos = json.load(archivo)
            
    except FileNotFoundError: # La excepción es su no se encuentra el archivo JSON
        print ("No hay datos en la lista")
        datos = {"trabajadores": [], "administradores": [], "clientes": []}  # Si está vacio el archivo JSON entonces se creará un diccionario para almacenar en el JSON.
    return datos

def guardar_datos(datos):# Función para guardar datos en el archivo JSON
    with open("data.json", "w") as archivo:  # se abre el archivo JSON y se indica aque será de escritura (se guardará).
        json.dump(datos, archivo, indent=2)     
# ______________________________________________________________

# ______________________________________________________________
# 3. Creamos las una función que admite el tipo de usuario que se quiere cear, dependiendo del usuario se pedirán una serie de datos diferentes y se guardará en listas distintas:

def registrar_usuario(tipo_registro): # Función para registrar un nuevo usuario
    datos = cargar_datos() # Cargar datos existentes
    
    if tipo_registro == "clientes": # si el tipo registro es de cliente entonces pide sus requisistos de ingreso
        username = input("Ingrese el nombre de usuario: ")
        password =  input("Ingrese su contraseña: ")
        confirmar_password =  input("Confirme su contraseña: ") # se confirma la contraseña 

        if password == confirmar_password: # se comprueba que sean iguales
            datos["clientes"].append({ # se añade a la lista de datos una nueva entrada.
                "user": username,
                "contraseña": password,
            })
            guardar_datos(datos) # Ya que la lista datos tiene nuestra clave y su valor lo guardamos con la función en el archibo JSON
            print("Usuario registrado exitosamente.")
        else:
            print("Las contraseñas no coinciden. Inténtelo de nuevo.")
            
    elif tipo_registro == "administradores": # Se hace un función igual para los administradores pero con más datos para ingresar
        username = input("Ingrese el nombre de usuario del administrador: ")
        password =  input("Ingrese su contraseña del administrador: ")
        confirmar_password =  input("Confirme su contraseña: ")
        if password == confirmar_password:
            datos["administradores"].append(
            {
                "user": username,
                "contraseña": password,
                "rango_admin": input("Ingrese fanción o rengo en la empresa del administrador: ")
                }
            )
            guardar_datos(datos) 
            print("Administrador registrado exitosamente.")
        else:
            print("Las contraseñas no coinciden. Inténtelo de nuevo.")      
        
    elif tipo_registro == "trabajadores": # Se usa la misma lógica para los trabajadores
        username = input("Ingrese el nombre de usuario del trabajador: ")
        password =  input("Ingrese su contraseña del trabajador: ")
        confirmar_password =  input("Confirme su contraseña: ")
        if password == confirmar_password:
            datos["trabajadores"].append(
            {
                "nombre_trabajador": input("Ingrese el nombre del trabajador: "),
                "apellido_trabajador": input("Ingrese la contraseña del trabajador: "),
                "profesion": input("Ingrese la profesión del trabajador: "),
                "puesto": input("Ingrese la profesión del trabajador: "),
                "DNI": input("Ingrese DNI del trabajador: "),
                "user": username,
                "contraseña": password,
                }
            )
            guardar_datos(datos) 
            print("Administrador registrado exitosamente.")
        else: 
            print("Las contraseñas no coinciden. Inténtelo de nuevo.") 
            
    else:
        print("Ocurrió un error. No sé pudo registrar ninpún valor.")
# _____________________________________________________________

# ______________________________________________________________
# 4. Creamos las una función de login para los clientes y trabajadores ya que ambos pueden ingresar en el mismo login pero tendrán funciones diferentes:  
def login():
    datos = cargar_datos() # Se cargan los datos
    global tipo_usuario
    username = input("Nombre de usuario: ") # se piden los datos 
    password =  input("Contraseña: ")

    for tipo_usuario in ["clientes", "trabajadores"]:  # se hace un bucle que recorra ambas listas para verificar a qué lista pertence el usuario
        for usuario in datos[tipo_usuario]:  # Con otro bucle hacemos la comprobación del usuario en una lista individual 
            if usuario["user"] == username and usuario["contraseña"] == password:  
                print(f"Inicio de sesión exitoso como {tipo_usuario}.")
                return tipo_usuario
    else:
        print("Inicio de sesión fallido. Credenciales incorrectas.")
        return None
# _____________________________________________________________

# ______________________________________________________________
# 5. Creamos las una función de login para el administrador ya que su login está separado de los clientes y administradores. Además tendrá funciones diferentes:  
def login_administrador():
    datos = cargar_datos()  # Se cargan los datos

    username = input("Nombre de usuario: ")  # se piden los datos
    rango = input("Rango o Cargo en la compañia: ")
    password =  input("Contraseña: ")

    for administrador in datos["administradores"]: # Con un bucle hacemos la comprobación del usuario 
        if administrador["user"] == username and administrador["contraseña"] == password and administrador["rango_admin"] == rango: 
            print(f"Inicio de sesión exitoso como administrador.")
            return True # si la comprobación es correcta decimos que es verdaderamente una administrador 
    else:
        print("Inicio de sesión fallido. Credenciales incorrectas.")
        return False # sino decimos que es falso
# _____________________________________________________________
    
# ______________________________________________________________
# 6. Creamos las opciones únicas de los administradores:    
def menu_administrador():
    while True: # Creamos un bucle infinito para repetir las opciones especiales y una lista de ellas  
        print("\n********* Menú Administrador: *********")
        print("1. Registrar Trabajador")
        print("2. Registrar Cliente")
        print("3. Registrar Administrador")
        print("4. Ver lista de Trabajadores")
        print("5. Ver lista de Clientes")
        print("6. Ver lista de Administradores")
        print("7. Salir")

        opcion = input("Seleccione una opción: ") # le pedimos una variable para que pueda selecionar que hacer
        # Programamos la lógica de las opciones:
        if opcion == "1":
            registrar_usuario("trabajadores")
        elif opcion == "2":
            registrar_usuario("clientes")
        elif opcion == "3":
            registrar_usuario("administradores")
        elif opcion == "4":
            datos = cargar_datos()
            print("\nLista de Trabajadores:")
            print(json.dumps(datos["trabajadores"], indent=2))
        elif opcion == "5":
            datos = cargar_datos()
            print("\nLista de Clientes:")
            print( json.dumps(datos["clientes"], indent=2))
        elif opcion == "6":
            datos = cargar_datos()
            print("\nLista de Administradores:")
            print(json.dumps(datos["administradores"], indent=2))
        elif opcion == "7": #opción para romper el bucle 
            break # rompe el bucle
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# ______________________________________________________________
# 7. Por ultimo hacemos le menú principal:    
while True: # Nuevamente creamos un bucle infinito para repetir las opciones y mostramos una lista
    print("\n1. Registrar")
    print("2. Ingresar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")# le pedimos una variable para que pueda selecionar que hacer
    # Programamos la lógica de las opciones:
    if opcion == "0":
        if login_administrador():
            menu_administrador()
    elif opcion == "1":
        registrar_usuario("clientes")
    elif opcion == "2":
        login()
        if tipo_usuario == "clientes":
            print ("Bienvenido, querido cliente.")
        elif tipo_usuario == "trabajadores":
            print ("Hola, trabajador. ¿Listo para otro día de trabajo?")
    elif opcion == "3":
        print("Finalizando la aplicación") #opción para romper el bucle 
        break # rompe el bucle
    else:
        print("Opción no válida. Inténtelo de nuevo.")
 