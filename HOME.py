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
        print("Eliminacion")
    elif opcion == 5:
        print("Busqueda")
    else:
        print("Opcion invalida...")

menuPrincipal()
