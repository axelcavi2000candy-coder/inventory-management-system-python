
{
    "nombre": "Laptop",
    "precio": 10000,
    "categoria": "Electronica",
    "existencia": 5
}

#Creamos una lista vacia
inventario = []

#Función del menú - mostramos las opciones que el usuario puede seleccionar
def menu():
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar producto")
    print("3. Buscar producto por nombre")
    print("4. Filtrar productos")
    print("5. Salir")

# Funcion Agregar Productos
def agregar_producto(inventario):
    nombre = input("Nombre del produto: ").strip() # Pide el nombre del producto

    if nombre == "": # Verifica si esta vacío
        print("El nombre no puede estar vacío")
        return
    
    try:
        precio = float(input("Precio: "))
    except:
        print("El precio debe ser numérico") # Si falla muestra error
        return
    
    categoria = input("Categoría: ").strip()

    try:
        existencia = int(input("Existencia: ")) # Pide la categoría
    except:
        print("La existencia debe ser un número entero")
        return
    
    producto = { # Crea el diccionario
        "nombre": nombre,
        "precio": precio,               # # Guarsamos los datos del producto
        "categoria": categoria,
        "existencia": existencia
    }

    inventario.append(producto)  # Agrega el producto a la lista
    print("Producto agregado correctamente") 

# Función Mostrar Productos
def mostrar_productos(inventario):
    if not inventario: # Verificamos si la lista esta vacía
        print("No hay productos en el inventrio")
        return
    
    for producto in inventario:
        print(producto)

#Función Buscar por Nombre
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre a buscar: ").lower() # Pide el nombre del producto

    encontrados = [p for p in inventario if p["nombre"].lower() == nombre] # Recorre todos los productos, si el nombre coincide lo guarda

    if encontrados: # Verifica si encuentra algo
        for p in encontrados: # Muestra resultados
            print(p)
    else:
        print("Producto no encontrado")

#Función Filtrar
def filtrar_productos(inventario):
    print("1. Filtrar por categoría")
    print("2. Filtrar por precio menor a X")

    opcion = input("Elige una opción: ") # Pide una opción

    if opcion == "1":
        categoria = input("Categoría: ").lower()
        filtrados = [p for p in inventario if p["categoria"].lower() == categoria] # Filtra los productos que coinciden

    elif opcion == "2":
        try:
            precio = float(input("Precio máximo: "))
            filtrados = [p for p in inventario if p["precio"] <= precio] # Guarda los productos con precio menor o igual
        except:
            print("Precio inválido")
            return
    else:
        print("Opción inválida")
        return

    if filtrados:
        for p in filtrados:
            print(p)
    else:
        print("No hay resultados")


#Función Principal
def main():
    inventario = [] # Crea la lista principal

    while True: # Ciclo infinito hasta salir
        menu() # Mostramos el menu
        opcion = input("Seleccione una opción: ")

        if opcion == "1": 
            agregar_producto(inventario) # LLama función para agregar
        elif opcion == "2":
            mostrar_productos(inventario) # Llama función para mostrar
        elif opcion == "3":
            buscar_producto(inventario) # Llama función para buscar
        elif opcion == "4":
            filtrar_productos(inventario) # Llama función para filtrar
        elif opcion == "5":
            print("Saliendo...")
            break # Termina el ciclo
        else:
            print("Opción inválida")

main() #Llamamos a todo el programa