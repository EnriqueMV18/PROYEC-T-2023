def listarProducto(producto):
    mensaje = "Productos"
    longitud_mensaje = len(mensaje)

    # Tamaño del marco
    ancho_marco = 15  # Puedes ajustar este valor según el tamaño deseado

    # Calcula los espacios para centrar el mensaje
    espacios_total = ancho_marco - longitud_mensaje
    espacios_izquierda = espacios_total // 2
    espacios_derecha = espacios_total - espacios_izquierda

    # Imprime el marco con el mensaje centrado
    print("╔" + "═" * ancho_marco + "╗")
    print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
    print("╚" + "═" * ancho_marco + "╝")

    contador = 1
    for pro in producto:
        datos = "{0} | Producto: {2: <25} | (Precio ${3})"
        print(datos.format(contador, pro[0], pro[1], pro[2]))
        contador = contador + 1
    print(" ")