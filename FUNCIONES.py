def listarProducto(producto):
    mensaje = "Productos"
    longitud_mensaje = len(mensaje)
    ancho_marco = 15
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")

    contador = 1
    for pro in producto:
        datos = "{0} | Producto: {2: <25} | (Precio ${3})"
        print(datos.format(contador, pro[0], pro[1], pro[2]))
        contador = contador + 1
    print(" ")

def pedirDatosRegistro():
    mensaje = "Agregar"
    longitud_mensaje = len(mensaje)
    ancho_marco = 15
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")

    #Id = input("Ingrese el ID": )
    Producto = input("Ingrese el Producto: ")
    Precio = float(input("Ingrese el Precio: "))

    producto = (Producto, Precio)
    return producto

def pedirDatosActualizacion(producto):
    mensaje = "Actualizar"
    longitud_mensaje = len(mensaje)
    ancho_marco = 15
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")
    for pro in producto:
        print(pro[1])  # Muestra el nombre del producto al usuario

    productoActualizarNombre = input("Ingrese el nombre del producto a actualizar: ")

    for pro in producto:
        if pro[1] == productoActualizarNombre:
            nuevoNombre = input("Ingrese el nuevo nombre para {}: ".format(pro[1]))
            nuevoPrecio = float(input("Ingrese el nuevo precio para {}: ".format(pro[1])))
            productoActualizar = (nuevoNombre, nuevoPrecio, pro[1])  # (NuevoNombre, NuevoPrecio, ProductoAntiguo)
            return productoActualizar

    return ""
    

def pedirDatosEliminacion(producto):

    listarProducto(producto)

    mensaje = "Eliminar"
    longitud_mensaje = len(mensaje)
    ancho_marco = 15
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")

    for pro in producto:
        print(pro[1])  # Muestra el nombre del producto al usuario

    existeProducto = False
    productoEliminar = input("Ingrese el producto a eliminar: ")
    
    for pro in producto:
        if pro[1] == productoEliminar:
            existeProducto = True
            break

    if not existeProducto:
        productoEliminar = ""
        
    return productoEliminar

def mostrarResultados(resultados):

    mensaje = "Busqueda"
    longitud_mensaje = len(mensaje)
    ancho_marco = 15
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")

    if resultados:
        print("Resultados de la búsqueda:")
        contador = 1
        for rel in resultados:
            datos = "{0} | Producto: {2: <25} | (Precio ${3})"
            print(datos.format(contador, rel[0], rel[1], rel[2]))
            contador = contador + 1
        print(" ")  # Puedes imprimir toda la información del producto o lo que necesites
    else:
        print("No se encontraron productos con ese nombre.")


    