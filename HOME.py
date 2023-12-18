from BD.CONEXION import DAO
import FUNCIONES

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            mensaje = "Menu Principal"
            longitud_mensaje = len(mensaje)
            espacios_izquierda = (18 - longitud_mensaje) // 2
            espacios_derecha = 20 - longitud_mensaje 
            print("╔" + "═" * (longitud_mensaje + 8) + "╗")
            print("║" + " " * espacios_izquierda + mensaje + " " * espacios_derecha + "║")
            print("╚" + "═" * (longitud_mensaje + 8) + "╝")
            print("1. LISTAR PRODUCTOS")
            print("2. AGREGAR PRODUCTOS")
            print("3. ACTUALIZAR PRODUCTO")
            print("4. ELIMINAR PRODUCTO")
            print("5. BUSCAR PRODUCTO")
            print("6. SALIR")
            print("══════════════════════")
            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 6:  
                print("Opcion incorrecta, seleccione nuevamente...")
            elif opcion == 6:  
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            producto = dao.listarProducto()
            if len(producto) > 0:
                FUNCIONES.listarProducto(producto) 
            else:
                print("No se encontraron productos...")
        except:
            print("Ocurrio un error...")
    elif opcion == 2:
        producto = FUNCIONES.pedirDatosRegistro()
        try:
            dao.registrarProducto(producto)
        except:
            print("Ocurrio un error...")
    elif opcion == 3:
        print("Actualizacion")
    elif opcion == 4:
        try:
            producto = dao.listarProducto()
            if len(producto) > 0:
                productoEliminar = FUNCIONES.pedirDatosEliminacion(producto)
                if not(productoEliminar == ""):
                    dao.eliminarProducto(productoEliminar)
                else:
                    print("Producto no encontrado... /n")
            else:
                print("No se encontraron productos...")
        except:
            print("Ocurrio un error...")
    elif opcion == 5:
        try:
            nombre_a_buscar = input("Ingrese el nombre del producto a buscar: ")
            resultados_busqueda = dao.buscarProducto(nombre_a_buscar)
            if resultados_busqueda:
                productoBuscar = FUNCIONES.mostrarResultados(resultados_busqueda)
            else:
                print("No se encontraron productos con ese nombre.")
        except Exception as busqueda_error:
            print("Ocurrió un error al buscar producto:", busqueda_error)


menuPrincipal()