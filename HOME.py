def menuPrincipal():
    print("==== MENÚ PRINCIPAL ====")
    print("1. LISTAR PRODUCTOS")
    print("2. AGREGAR PRODUCTOS")
    print("3. ACTUALIZAR PRODUCTO")
    print("4. ELIMINAR PRODUCTO")
    print("5. BUSCAR PRODUCTO")
    print("6. SALIR")
    print("====")
    opcion = int(input("Seleccione una opcion: "))

    if opcion < 1 or opcion > 6:  
        print("Opcion incorrecta, seleccione nuevamente...")
    elif opcion == 6:  
        print("¡Gracias por usar este sistema!")
    else:
        ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    print("Ejecutar opción:", opcion)

menuPrincipal()
