def cargar_participantes(array_participantes: list) -> bool:
    """Permite ingresar los nombres de todos los participantes.

    Args:
        array_participantes (list): Lista donde se almacenan los participantes.

    Returns:
        bool: True si se pudo hacer la carga. False si no.
    """
    if type(array_participantes) == list and len(array_participantes) > 0:
        
        for i in range(len(array_participantes)):
            while True:
                nombre = input(f"Ingrese el nombre del participante {i + 1}: ")
                valido = len(nombre) >= 3
                for letra in nombre:
                    if ord(letra) != 32 and (ord(letra) < 65 or ord(letra) > 90) and (ord(letra) < 97 or ord(letra) > 122):
                        valido = False
                        break
                if valido:
                    array_participantes[i] = nombre
                    break
                else:
                    print("El nombre debe tener al menos 3 caracteres y solo puede contener letras y espacios.")
            
        
        retorno = True
    else:
        retorno = False
        
    return retorno

def cargar_puntuacion(matriz_puntuacion: list) -> bool:
    """Permite ingresar las puntuaciones que cada jurado le dio a cada participante.

    Args:
        matriz_puntuacion (list): Matriz donde se guardan las puntuaciones.

    Returns:
        bool: True si se pudo cargar. False si no.
    """
    if type(matriz_puntuacion) == list and len(matriz_puntuacion) > 0:
        for fil in range(len(matriz_puntuacion)):
            for col in range(len(matriz_puntuacion[fil])):
                while True:
                    try:
                        puntuacion = int(input(f"Ingrese la puntuacion del jurado {col + 1} para el participante {fil + 1}: "))
                        while puntuacion > 10 or puntuacion < 1:
                            puntuacion = int(input(f"{puntuacion} no es una puntuacion valida. Reingrese su opcion (1-10): "))
                        matriz_puntuacion[fil][col] = puntuacion
                        break
                    except ValueError:
                        print("Entrada invalida. Por favor ingrese un numero entero.")
        retorno = True
    else:
        retorno = False
        
    return retorno

def elegir_opcion() -> int:
    """Permite ingresar una opcion del menu, comprobando si es un numero entero entr 0 y 12.

    Returns:
        int: Opcion elegida, una vez validada.
    """
    while True:    
        try:
            opcion = int(input("Ingrese una opción (0-12): "))
            if opcion >= 0 and opcion <= 12:
                return opcion
            else:
                    print("Opción fuera de rango. Ingrese un número entre 0 y 12.")
        except ValueError:
                print("No ingreso un numero. Ingrese un numero entre 0 y 12")
