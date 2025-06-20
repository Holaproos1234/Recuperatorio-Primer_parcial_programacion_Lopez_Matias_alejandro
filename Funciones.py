from random import *

def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    """Crea un array del largo indicado, relleno con el valor elegido.

    Args:
        cantidad_elementos (int): Largo que va a tener la lista.
        valor_inicial (any): Valor inicial de los elementos de la lista.

    Returns:
        list: Lista creada con los parametros elegidos.
    """
    array = [valor_inicial] * cantidad_elementos
    return array

def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any) -> list:
    """Crea una matriz del tamaño indicado, rellena con el valor elegido.

    Args:
        cantidad_filas (int): Cantidad de filas que va a tener la matriz.
        cantidad_columnas (int): Cantidad de columnas que va a tener la matriz.
        valor_inicial (any): Valor inicial de los elementos de la matriz.

    Returns:
        list: Matriz creada con los parametros elegidos.
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

def mostrar_nombres_participantes(array_Participantes: list) -> None:
    """Muestra los nombres de todos los participantes.

    Args:
        array_Participantes (list): Lista con los nombres de los participantes.
    """
    for i in range(len(array_Participantes)):
        print(array_Participantes[i])

def buscar_largo_matriz(matriz_puntuacion: list, indice: int) -> int:
    """Busca el largo de una matriz.

    Args:
        matriz_puntuacion (list): Matriz que se va a medir.
        indice (int): Indice utilizado para medir el largo.

    Returns:
        int: Largo de la matriz medida.
    """
    largo_matriz = len(matriz_puntuacion[indice])

    return largo_matriz

def calcular_promedio(cantidad_parcial: int | float, largo_matriz: int) -> float:
    """Calcula el promedio de una matriz.

    Args:
        cantidad_parcial (int | float): Suma de los elementos de la matriz a la que se le sacara promedio.
        largo_matriz (int): Largo de la matriz a la que se le sacara el promedio.

    Returns:
        float: Promedio resultado de la cuenta. Es un decimal.
    """
    promedio = (cantidad_parcial / largo_matriz)
    
    return promedio

def sumar_columna(matriz_numerica: list, indice_col: int) -> int | float:
    """Suma una columna especifica de una matriz numerica.

    Args:
        matriz_numerica (list): Matriz de la que se sumara una columna.
        indice_col (int): Indice de la columna que se sumara.

    Returns:
        int | float: Resultado de la suma. Puede ser entero o decimal.
    """
    suma_columna = 0
    for fila in range(len(matriz_numerica[0])):
        if indice_col >= len(matriz_numerica[fila]):
            break
        if type(matriz_numerica[fila][indice_col]) == int or type(matriz_numerica[fila][indice_col]) == float :
            suma_columna += matriz_numerica[fila][indice_col]
    return suma_columna

def calcular_promedio_jurado(matriz_puntuacion: list, indice: int) -> float:
    """Calcula el promedio de puntuaciones de un jurado.

    Args:
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de los participantes.
        indice (int): Indice utilizado para determinar la cantidad de jurados.

    Returns:
        float: Promedio calculado.
    """

    puntuacion_jurado = sumar_columna(matriz_puntuacion, indice)
    cantidad_jueces = buscar_largo_matriz(matriz_puntuacion, indice)
    promedio = calcular_promedio(puntuacion_jurado, cantidad_jueces)
    return promedio
    
def encontrar_jurado_estricto(matriz_puntuacion: list, indice: int) -> list:
    """Encuentra el o los jurados con el promedio mas bajo.

    Args:
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de los participantes.
        indice (int): Indice utilizado para determinar la cantidad de jurados.

    Returns:
        list[list, float]: Una lista conteniendo dos elementos. Una lista con los indices de jurados mas estrictos,
        y un Floatante conteniendo el menor de los promedios de los jurados.
    """
    min_numero = float('inf')
    largo_matriz = buscar_largo_matriz(matriz_puntuacion, indice)
    jurados = []
    for i in range(largo_matriz):
        promedio = (calcular_promedio_jurado(matriz_puntuacion, i))


        if promedio < min_numero:
            min_numero = promedio
            jurados = [i]
        elif promedio == min_numero:
            jurados += [i]
    return [jurados, min_numero]

def redondear_dos_decimales(numero: float) -> float:
    """Redondea un float, dejando 2 decimales.

    Args:
        numero (float): Numero a redondear.

    Returns:
        float: Numero redondeado.
    """
    numero_redondeado = int(numero * 100 + 0.5) / 100
    return numero_redondeado

def mostrar_jurado_estricto(matriz_puntuacion: list, indice: int) -> bool:
    """Muestra el jurado o los jurados mas estrictos(con menor promedio).

    Args:
        matriz_puntuacion (list): Matriz donde se encuentran los puntajes dados por todos los jurados.
        indice (int): Indice utilizado para determinar la cantidad de jurados.
    Returns:
        bool: Retorna True si se mostraron jurados, false si no.
    """
    jurados, min_numero = encontrar_jurado_estricto(matriz_puntuacion, indice)
    if len(jurados) == 0:
        return False
    elif len(jurados) == 1:    
            print(f"EL JURADO MAS ESTRICTO ES EL JURADO {jurados[0]+1}: PROMEDIO {redondear_dos_decimales(min_numero)}")
            print("")
    elif len(jurados) != 1:
        print("LOS JURADOS MAS ESTRICTOS SON:")
        for i in range(len(jurados)):
            print(f"JURADO {jurados[i]+1}: PROMEDIO {redondear_dos_decimales(min_numero)}")
            print("")
    return True
    
def mostrar_promedio_jurado(matriz_puntuacion: list, indice: int) -> bool:
    """Muestra el promedio de la puntuacion dada por cada jurado.

    Args:
        matriz_puntuacion (list): Matriz donde se almacenan las puntuaciones.
        indice (int): Indice del jurado del que se buscara el promedio.

    Returns:
        bool: True si el índice es válido, False en caso contrario.
    """
    cantidad_jueces = buscar_largo_matriz(matriz_puntuacion, indice)
    if indice >= cantidad_jueces or indice < 0:
        retorno = False
    else:
        retorno = True
        puntuacion_jurado = sumar_columna(matriz_puntuacion,indice)
        cantidad_jueces = buscar_largo_matriz(matriz_puntuacion,indice)
        promedio = calcular_promedio(puntuacion_jurado,cantidad_jueces)
        print(f"Puntuacion promedio del jurado {indice+1}: {redondear_dos_decimales(promedio)}")

        
    return retorno

def mostrar_promedio_jurados(matriz_puntuacion: list) -> None:
    """Muestra por consola el promedio de cada jurado.

    Args:
        matriz_puntuacion (list): Matriz donde se almacenan las puntuaciones.
    """

    for i in range(len(matriz_puntuacion[0])):
        mostrar_promedio_jurado(matriz_puntuacion,i)
        print("")

def mostrar_participante(array_participantes: list, matriz_puntuacion: list, indice: int) -> bool:
    """Muestra por consola la info de un participante.

    Args:
        array_participantes (list): Lista con los nombres de los participantes.
        matriz_puntuacion (list): Matriz donde se almacenan las puntuaciones.
        indice (int): Indice del participante.

    Returns:
        bool: True si el participante existe. False si no.
    """
    if indice >= len(array_participantes) or indice < 0:
        retorno = False
    else:
        cantidad_total_puntuacion_participante = sumar_fila(matriz_puntuacion, indice)
        retorno = True
        cantidad_jueces = buscar_largo_matriz(matriz_puntuacion, indice)
        promedio = calcular_promedio(cantidad_total_puntuacion_participante, cantidad_jueces)
        print(f"PARTICIPANTE: {array_participantes[indice]}")
        print(f"PUNTUACION JURADO 1: {matriz_puntuacion[indice][0]}")
        print(f"PUNTUACION JURADO 2: {matriz_puntuacion[indice][1]}")
        print(f"PUNTUACION JURADO 3: {matriz_puntuacion[indice][2]}")
        print(f"PUNTUACION PROMEDIO: {redondear_dos_decimales(promedio)}")
    return retorno

def mostrar_participantes(array_participantes: list, matriz_puntuacion: list) -> None:
    """Muestra la info de todos los participantes por consola.

    Args:
        array_participantes (list): Lista con los nombres de los participantes.
        matriz_puntuacion (list): Matriz donde se almacenan las puntuaciones.
    """
    for i in range(len(array_participantes)):
        mostrar_participante(array_participantes, matriz_puntuacion, i)
        print("")

def sumar_matriz(matriz_numerica: list) -> int | float:
    """Suma todos los elementos de una matriz numerica.

    Args:
        matriz_numerica (list): Matriz formada por numeros.

    Returns:
        int | float: El resultado de la suma, puede ser un numero entero o decimales.
    """
    suma = 0
    
    for fil in range(len(matriz_numerica)):
        for col in range(len(matriz_numerica[fil])):
            if type(matriz_numerica[fil][col]) == int or type(matriz_numerica[fil][col]) == float:
                suma += matriz_numerica[fil][col]
    return suma

def sumar_fila(matriz_numerica: list, indice_fila: int) -> int | float:
    """Suma una fila especifica de una matriz numerica.

    Args:
        matriz_numerica (list): Matriz de la que se sumara una fila.
        indice_fila (int): Indice de la fila que se sumara.

    Returns:
        int | float: El resultado de la suma, puede ser un numero entero o decimales.
    """
    suma_fila = 0
    
    for col in range(len(matriz_numerica[0])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila

def mostrar_promedio_superior_a(array_participantes: list, matriz_puntuacion: list, mayor_a: float) ->bool:
    """Muestra los participantes con un promedio superior a cierto numero.

    Args:
        array_participantes (list): Lista que contiene a los participantes.
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de cada participante.
        mayor_a (float): Numero que se debe superar para mostrar.

    Returns:
        bool: True si algun participante tiene promedio mayor a "mayor_a". False si no.
    """
    retorno = False
    for i in range(len(array_participantes)):
        cantidad_total_puntuacion_participante = sumar_fila(matriz_puntuacion, i)
        cantidad_jueces = buscar_largo_matriz(matriz_puntuacion, i)
        promedio = calcular_promedio(cantidad_total_puntuacion_participante, cantidad_jueces)
        
        if promedio > mayor_a:
            mostrar_participante(array_participantes, matriz_puntuacion, i)
            print("")
            retorno = True
    if retorno == False:
            print(f"Ningun participante tuvo un promedio mayor a {mayor_a}")
    return retorno

def buscar_participante(array_participantes: list, matriz_puntuacion: list) -> bool:
    """Busca un participante y su info dentro del array.

    Args:
        array_participantes (list): Lista que contiene a los participantes.
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de los participantes.

    Returns:
        bool: True si el nombre fue encontrado. False si no.
    """
    while True:
            
            participante = input("Ingrese el nombre del participante a buscar: ")
            indice = buscar_por_nombre(array_participantes, participante)
            if indice == -1:
                print("Ese participante no existe.")
                return False
            else:
                mostrar_participante(array_participantes, matriz_puntuacion, indice)
                return True

def buscar_por_nombre(array_participantes: list, participante: str) -> int:
    """Busca un elemento dentro de una lista, y devuelve su indice.

    Args:
        array_participantes (list): Lista donde se encuentran los participantes.
        participante (str): Nombre a buscar en el array.

    Returns:
        int: Indice donde se encuentra el elemento.
    """
    for i in range(len(array_participantes)):
            if array_participantes[i] == participante:
                return i
    return -1

def validar_banderas(bandera_1: bool, bandera_2: bool) -> bool:
    """Valida si las dos banderas son verdaderas.

    Args:
        bandera_1 (bool): Primera bandera.
        bandera_2 (bool): Segunda bandera.

    Returns:
        bool: Regresa True si ambas banderas son verdaderas. Regresa False en cualquier otro caso.
    """
    if bandera_1 and bandera_2:
        retorno = True
    else:
        retorno = False
    return retorno               

def intercambiar_elementos(array: list, izq: int, der: int) -> None:
    """Intercambia dos elementos en una lista.

    Args:
        array (list): Array que contiene los elementos a intercambiar.
        izq (int): Indice del elemento a la izquierda. Primer elemento a intercambiar.
        der (int): Indice del elemento a la derecha. Segundo elemento a intercambiar.
    """
    auxiliar = array[izq]
    array[izq] = array[der]
    array[der] = auxiliar

def ordenar_mayor_menor_con_indices(valores: list, indices: list) -> None:
    """Ordena los elementos de una lista, de mayor a menor, y manteniendo cada elemento con su indice original.

    Args:
        valores (list): Lista de los elementos a ordenar.
        indices (list): Lista de los indices originales de los elementos a ordenar. Se reorganiza manteniendo
        cada indice correspondiente al valor en "valores".
    """
    for izq in range(len(valores) - 1):
        for der in range(izq + 1, len(valores)):
            if valores[izq] < valores[der]:
                intercambiar_elementos(valores, izq, der)
                intercambiar_elementos(indices, izq, der)

def buscar_por_indice(array_participantes: list, indice: int) -> str | None:
    """Busca un elemento en una lista mediante su indice.

    Args:
        array_participantes (list): Lista con los nombres de los participantes.
        indice (int): Indice a buscar en la lista.

    Returns:
        str | None: Retorna None si no encuentra el elemento. Retorna el elemento si lo encuentra.
    """
    if 0 <= indice < len(array_participantes):
        return array_participantes[indice]

def encontrar_top_3(matriz_puntuacion: list) -> list[list[int, float]]:
    """Encuentra el top 3 de los participantes con mayor promedio.

    Args:
        matriz_puntuacion (list): Matriz que contiene todas las puntuaciones de los participantes.

    Returns:
        list[list[int, float]]: Una lista de listas. Contiene listas con dos elementos.
        Uno siendo el indice del participante(int) y el otro su promedio(float)
    """
    num_participantes = len(matriz_puntuacion)
    num_columnas = 0
    if num_participantes > 0:
        num_columnas = len(matriz_puntuacion[0])

    promedios = []
    indices = []
    i = 0
    while i < num_participantes:
        suma = 0
        j = 0
        while j < num_columnas:
            suma += matriz_puntuacion[i][j]
            j += 1
        promedio = calcular_promedio(suma, num_columnas)
        promedios += [promedio]
        indices += [i]
        i += 1

    ordenar_mayor_menor_con_indices(promedios, indices)

    top3 = []
    k = 0
    while k < 3 and k < len(promedios):
        top3 += [[indices[k], promedios[k]]]
        k += 1

    return top3

def mostrar_top_3(matriz_puntuacion: list, array_participantes: list) -> None:
    """Muestra el top 3 de los participantes con mayor promedio.

    Args:
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de todos los participantes.
        array_participantes (list): Array que posee los nombres de todos los participantes.
    """
    i = 0
    top3 = encontrar_top_3(matriz_puntuacion)
    while i < len(top3):
        participante = top3[i][0]
        promedio = top3[i][1]
        nombre_participante = buscar_por_indice(array_participantes, participante)
        print(f"Top {i+1}: Participante {nombre_participante} con promedio {redondear_dos_decimales(promedio)}")
        i += 1

def ordenar_menor_mayor_con_indices(valores: list, indices: list) -> None:
    """Ordena los elementos de una lista, de menor a mayor, y manteniendo cada elemento con su indice original.

    Args:
        valores (list): Lista de los elementos a ordenar.
        indices (list): Lista de los indices originales de los elementos a ordenar. Se reorganiza manteniendo
        cada indice correspondiente al valor en "valores".
    """
    for izq in range(len(valores) - 1):
        for der in range(izq + 1, len(valores)):
            if valores[izq] > valores[der]:
                intercambiar_elementos(valores, izq, der)
                intercambiar_elementos(indices, izq, der)

def ordena_alfabeticamente(array_participantes: list) -> list:
    """Ordena en orden alfabetico los elementos de una lista, manteniendo sus indices originales.

    Args:
        array_participantes (list): Lista que contiene los nombres de todos los participantes.

    Returns:
        list: Lista con los indices de los nombres en orden aflabetico.
    """
    nombres = []
    indices = []
    i = 0
    while i < len(array_participantes):
        nombres += [array_participantes[i]]
        indices += [i]
        i += 1

    ordenar_menor_mayor_con_indices(nombres, indices)

    return indices

def mostrar_participantes_ordenados(array_participantes: list, matriz_puntuaciones: list) -> None:
    """Muestra a los participantes y su info en orden alfabetico.

    Args:
        array_participantes (list): Lista con los nombres de todos los participantes.
        matriz_puntuaciones (list): Matriz con todas las puntuaciones de los participantes.
    """
    indices = ordena_alfabeticamente(array_participantes)
    for i in range(len(indices)):
        indice = indices[i]
        mostrar_participante(array_participantes, matriz_puntuaciones, indice)
        print("")

def encontrar_ganador(matriz_puntuacion: list) -> list:
    """Encuentra el o los participantes con el promedio mas alto.

    Args:
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de los participantes.

    Returns:
        list: Una lista con los indices del o de los ganadores.
    """
    max_numero = float('-inf')
    largo_matriz = len(matriz_puntuacion)
    participantes = []
    for i in range(largo_matriz):
        puntuacion_participantes = sumar_fila(matriz_puntuacion, i)
        promedio = (calcular_promedio(puntuacion_participantes, largo_matriz))


        if promedio > max_numero:
            max_numero = promedio
            participantes = [i]
        elif promedio == max_numero:
            participantes += [i]
    return participantes

def mostrar_ganador(array_participantes: list, matriz_puntuacion: list) -> str:
    """Muestra al ganador o ganadores. En caso de haber mas de uno, avisa que hay que desempatar.

    Args:
        array_participantes (list): Lista que contiene los nombres de todos los participantes.
        matriz_puntuacion (list): Matriz que contiene las puntuaciones de todos los jurados para cada participantes. 

    Returns:
        str: "Si" si hay que desempatar. "No" si no hay que desempatar. Se usa para validar la funcion Desempatar
    """
    indice_ganador = encontrar_ganador(matriz_puntuacion)
    if len(indice_ganador) == 1:
        print("El ganador es:")
        indice = indice_ganador[0]
        mostrar_participante(array_participantes, matriz_puntuacion, indice)
        desempate = "No"
    elif len(indice_ganador) > 1:
        print("Los ganadores son:")
        desempate = "Si"
        for i in range(len(indice_ganador)):
            indice = indice_ganador[i]
            mostrar_participante(array_participantes, matriz_puntuacion, indice)
            print("")
        print("Hay que desempatar")
    return desempate

def desempatar(desempate: str, cantidad_ganadores: int, ganador: int = None) -> int:
    """Comprueba si hay que desempatar, y en caso afirmativo genera un numero al azar.

    Args:
        desempate (str): "Si" si hay que desempatar. "No" si no hay que desempatar.
        cantidad_ganadores (int): Cantidad de ganadores. Se usa para saber el rango en el que hay que 
        generar un numero al azar.

    Returns:
        int: Numero generado al azar, entro 1 y el rango necesario.
    """
    if desempate == "No":
        print("No hay que desempatar")
    elif desempate == "Si":    
        ganador = randint(1, cantidad_ganadores)
    else:
        print("Primero compruebe el ganador")
    return ganador

def mostrar_desempate(array_participantes, matriz_puntuacion, desempate, ganador: int = None) -> bool:

    ganadores = encontrar_ganador(matriz_puntuacion)
    if ganador == None:
        ganador = desempatar(desempate, len(ganadores))
        if ganador == None:
            return None
        i = ganadores[ganador-1]
        mostrar_participante(array_participantes, matriz_puntuacion, i)
    elif ganador != None:
        print(f"Ya se desempato. El resultado fue:\n")
        i = ganadores[ganador-1]
        mostrar_participante(array_participantes, matriz_puntuacion, i)
    return ganador

def validar_ingresos(bandera: bool) -> bool:
    """Valida si las dos banderas son verdaderas.

    Args:
        bandera_1 (bool): Primera bandera.
        bandera_2 (bool): Segunda bandera.

    Returns:
        bool: Regresa True si ambas banderas son verdaderas. Regresa False en cualquier otro caso.
    """
    if not bandera:
        retorno = True
    else:
        print("Ya se ingresaron estos datos")
        retorno = False
    return retorno   
