from Inputs import *
from Funciones import *
import os

array_participantes = crear_array(5,"")
matriz_puntuacion = crear_matriz(5,3,0)
bandera_1 = False
bandera_2 = False
bandera_3 = False
ganador = None
desempate= ""
while True:
    print("1. Cargar participantes\n2. Cargar puntuaciones\n3. Mostrar puntuaciones\n4. Mostrar promedios " \
    "mayores a 4\n5. Mostrar promedios mayores a 7\n6. Mostrar promedios del jurado\n7. Mostrar jurado mas estricto" \
    "\n8. Buscar participante\n9. Mostrar Top 3\n10. Mostrar participantes por orden alfabetico\n11. Mostrar ganador" \
    "\n12. Desempatar\n0. Salir")
    opcion = elegir_opcion()    
    if opcion == 1 and validar_ingresos(bandera_1):
        if cargar_participantes(array_participantes) == True:
            print("Nombres cargados exitosamente")
            print("Los participantes cargados son: ")
            mostrar_nombres_participantes(array_participantes)
            bandera_1 = True
        else:
            print("No se pudo cargar los datos")
    elif opcion == 2 and validar_ingresos(bandera_2):
        if cargar_puntuacion(matriz_puntuacion) == True:
            print("Puntuaciones cargadas exitosamente!")
            bandera_2=True
        else:
            print("Error al cargar las puntuaciones")
    elif 12 >= opcion >= 3 and not validar_banderas(bandera_1, bandera_2):
        print("Antes de continuar debe cargar los datos.")
    elif opcion == 3 and validar_banderas(bandera_1, bandera_2):
        mostrar_participantes(array_participantes,matriz_puntuacion)
    elif opcion == 4 and validar_banderas(bandera_1, bandera_2):
        mostrar_promedio_superior_a(array_participantes, matriz_puntuacion,4.0)
    elif opcion == 5 and validar_banderas(bandera_1, bandera_2):
        mostrar_promedio_superior_a(array_participantes, matriz_puntuacion,7.0)
    elif opcion == 6 and validar_banderas(bandera_1, bandera_2):
        mostrar_promedio_jurados(matriz_puntuacion)
    elif opcion == 7 and validar_banderas(bandera_1, bandera_2):
        mostrar_jurado_estricto(matriz_puntuacion,0)
    elif opcion == 8 and validar_banderas(bandera_1, bandera_2):
        buscar_participante(array_participantes,matriz_puntuacion)
    elif opcion == 9 and validar_banderas(bandera_1, bandera_2):
        mostrar_top_3(matriz_puntuacion, array_participantes)
    elif opcion == 10 and validar_banderas(bandera_1, bandera_2):
        mostrar_participantes_ordenados(array_participantes, matriz_puntuacion)
    elif opcion == 11 and validar_banderas(bandera_1, bandera_2): 
        desempate = mostrar_ganador(array_participantes, matriz_puntuacion)
    elif opcion == 12 and validar_banderas(bandera_1, bandera_2): 
        ganador = mostrar_desempate(array_participantes, matriz_puntuacion, desempate, ganador)
    elif opcion == 0 and validar_banderas(bandera_1, bandera_2):
        print("Saliendo")
        break
    input("Toque Enter para continuar...")
    os.system("cls")
