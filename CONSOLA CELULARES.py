rom time import sleep

# Clase que representa un celular con sus características
class Celular:
    def __init__(self, marca, modelo, gama, funcion, precio):
        self.marca = marca       # Marca del celular
        self.modelo = modelo     # Modelo del celular
        self.gama = gama         # Gama del celular
        self.funcion = funcion   # Función o característica especial
        self.precio = precio     # Precio del celular
        
    # Método que muestra las especificaciones del celular
    def especificaciones(self):
        print("-------- ESPECIFICACIONES ---------")
        print(f"MARCA : {self.marca}")
        print(f"MODELO : {self.modelo}")
        print(f"GAMA : {self.gama}")
        print(f"FUNCIÓN : {self.funcion}")
        print(f"PRECIO : {self.precio}")
        print("-----------------------------------")


# Lista para almacenar todos los celulares
lista_de_celulares = []

# Bucle principal del menú
while True:
    print("\n--- MENU PRINCIPAL ---")
    opcion = input("1. Agregar un nuevo celular\n2. Ver todos los celulares\n3. Editar un celular\n4. Salir\n\nElige una opción: ")

    # Opción 1: Agregar celular
    if opcion == '1':
        print("\n--- AGREGAR UN NUEVO CELULAR ---")

        # Datos del nuevo celular
        marca = input("Marca del celular: ")
        modelo = input("Modelo del celular: ")
        gama = input("Gama del celular: ")
        funcion = input("Función del celular: ")
        precio = input("Precio del celular: ")

        # Crear un objeto Celular y agregarlo a la lista
        nuevo_celular = Celular(marca, modelo, gama, funcion, precio)
        lista_de_celulares.append(nuevo_celular)

        print("\nCelular agregado con éxito")
        sleep(3)
        nuevo_celular.especificaciones()

    # Opción 2: Ver celulares
    elif opcion == '2':
        sleep(3)
        print("\n--- LISTA DE CELULARES ---")

        if not lista_de_celulares:  # Si la lista está vacía
            print("No hay celulares en la lista todavía.")
        else:
            # Mostrar cada celular registrado
            for celular in lista_de_celulares:
                celular.especificaciones()

    # Opción 3: Editar un celular
    elif opcion == '3':
        print("\n--- EDITAR CELULAR ---")

        if not lista_de_celulares:
            print("No hay celulares para editar.")
            continue   # Volver al menú principal

        # Buscar por modelo
        edit_modelo = input("Escribe el modelo del celular que quieres editar: ")
        
        celular_encontrado = None

        for celular in lista_de_celulares:
            if celular.modelo == edit_modelo:
                celular_encontrado = celular
                break

        if celular_encontrado:
            print("\nIntroduce los nuevos datos (deja en blanco para no cambiar):")

            nueva_marca = input(f"Nueva marca ({celular_encontrado.marca}): ")
            if nueva_marca:
                celular_encontrado.marca = nueva_marca

            nuevo_modelo = input(f"Nuevo modelo ({celular_encontrado.modelo}): ")
            if nuevo_modelo:
                celular_encontrado.modelo = nuevo_modelo

            nueva_gama = input(f"Nueva gama ({celular_encontrado.gama}): ")
            if nueva_gama:
                celular_encontrado.gama = nueva_gama

            nuevo_precio = input(f"Nuevo precio ({celular_encontrado.precio}): ")
            if nuevo_precio:
                celular_encontrado.precio = nuevo_precio  # <-- corregido

            print("\n¡Celular actualizado!")
            celular_encontrado.especificaciones()

        else:
            print(f"Error: No se encontró el modelo '{edit_modelo}'.")

    # Opción 4: Salir
    elif opcion == '4':
        print("Adiós, el programa ha finalizado.")
        break

    # Opción inválida
    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 4.")
