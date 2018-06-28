# from . import *



# def prueba_distacia():
#     datos_puntos = np.array([[2,2],
#     [4,2],
#     [3,3],
#     [2,4],
#     [5,4],
#     [7,2],
#     [8,3],
#     [8,4]]
#     )

#     print(calcular_distancia(datos_puntos[0],datos_puntos[3]))









# # funcion q recibe todos los puntos y le paso centroides y me devueleve los grupos y el indice al que pertenecen
# def get_group(puntos, centroides):
#     cluster = [[] for i in centroides]
#     for i in puntos:
#         distancia = {}
#         # iteracion con los k
#         # la distancia de todos los k hacia este punto
#         for j in range(0,len(centroides)):
#             distancia[j] = calcular_distancia(i, centroides[j])
        
#         # retorna un array con el indice del minimo, el punto y el centroide al que pertenece
#         # [indice_del_minimo, punto_i, centroide_i_al que pertenece]
#         datos_para_asignar = asignar_al_cluster_n_datos(distancia, i, centroides)
#         cluster[datos_para_asignar[0]].append(datos_para_asignar[1])
#         # antes de salir del bucle se le agrega a la var q tendra los resultados
#         #     if iteracion == (cantidad_d_iteraciones - 1):
#         #         etiqueta_y_cluster.append(label)
# # """ el cluster no deberia de limpiarse porque en base a eso genero los cemtroides"""
#     return cluster




# def iterate_k_means(datos, centroides, n_iteraciones):
#     cluster = [[] for i in centroides]
#     cluster2 = [[] for i in centroides]
#     etiqueta_y_cluster = []
#     contador = 0
#     centroides_aterior = centroides
#     centroides_actual = centroides

#     while contador < n_iteraciones:

#         for i in centroides_aterior:
#             print("nuevo_centroide ",i," <-")   

#         # for i in centroides_aterior:
#         #     print("nuevo_centroide ",i," <-")
#         # DEBERIA DE ALMACENAR LOS GRUPOS
#         # DESPUES DE QUE UN GRUPO SE CREA A PARTIR DE UN CENTROIDE SE CALCULA EL NUEVO CENTROIDE
#         centroides_actual = np.array([calcular_centroide(i) for i in get_group(datos,centroides_aterior)])
#         # cluster = [[] for i in centroides]
#         centroides_aterior = centroides_actual
#         contador += 1
#     return [etiqueta_y_cluster, centroides]
# 

# c(i) indice del cluster
# uc(i) ubicacion del centroide del cluster al centroide que se asigno



# def funcion_costo(c,u,x):

    

###################################################
# def iterate_k_means(data_puntos, centroides, cantidad_d_iteraciones):
#     cluster = [[] for i in centroides]
#     cluster2 = [[] for i in centroides]
#     etiqueta_y_cluster = []
#     total_de_puntos = len(data_puntos)
#     # cantidad de centroides
#     k = len(centroides)
    
#     nuevo_centroide = centroides

#     # cantidada de iteraciones
#     for iteracion in range(0, cantidad_d_iteraciones):
        
#         for i in nuevo_centroide:
#             print("nuevo_centroide ",i," <-")
#         print()
#         # iteracion en los puntos
#         for indice_del_punto in range(0, total_de_puntos):
#             distancia = {}
#             # iteracion con los k
#             # la distancia de todos los k hacia este punto
#             for indice_de_centroide in range(0, k):
#                 distancia[indice_de_centroide] = calcular_distancia(data_puntos[indice_del_punto], nuevo_centroide[indice_de_centroide])
            
#             # retorna un array con el indice del minimo, el punto y el centroide al que pertenece
#             # [indice_del_minimo, punto_i, centroide_i_al que pertenece]
#             datos_para_asignar = asignar_al_cluster_n_datos(distancia, data_puntos[indice_del_punto], nuevo_centroide)
#             cluster[datos_para_asignar[0]].append(datos_para_asignar[1])
#             # antes de salir del bucle se le agrega a la var q tendra los resultados
#             #     if iteracion == (cantidad_d_iteraciones - 1):
#             #         etiqueta_y_cluster.append(label)
#     # """ el cluster no deberia de limpiarse porque en base a eso genero los cemtroides"""

#         nuevo_centroide = np.array([calcular_centroide(i) for i in cluster])

#         cluster = [[] for i in centroides]
#         # print(cluster)




#         # centroides[label[0]] = calcular_nuevos_centroides(label[1], centroides[label[0]])
#         # print("centroides : ",centroides)

#     return [etiqueta_y_cluster, centroides]
###################################################


# def print_resultados(result):
#     print("Resultado de agrupamiento k-Means: \n")
#     for data in result[0]:
#         print("punto: {}".format(data[1]))
#         print("asignado al grupo : {} \n".format(data[0]))
#     print("posiciones de los ultimos centroids: \n {}".format(result[1]))




# def asignar_al_cluster_n_datos(distancia, data_punto, centroides):
#     # se obtiene el indice
#     # la lista de distancias(el minino)
#     indice_del_minimo = min(distancia, key=distancia.get)
#     # retorna un array con el indice del minimo, el punto y el centroide al que pertenece
#     return [indice_del_minimo, data_punto, centroides[indice_del_minimo]]

# # recibe 
# # las distancias del punto hacia los centroides {}
# # el punto que se calculo la distancia
# # la lista de centroides
# # cluster[]
# def asignar_al_cluster_n_datos(distancia, data_punto, centroides):
#     # se obtiene el indice
#     # la lista de distancias(el minino)
#     indice_del_minimo = min(distancia, key=distancia.get)
#     # retorna un array con el indice del minimo, el punto y el centroide al que pertenece
#     return [indice_del_minimo, data_punto, centroides[indice_del_minimo]]



# # calcula el centroide entre 2 puntos
# def calcular_nuevos_centroides(grupo, centroides):
#     return np.array(grupo + centroides)/2




    # while count < cnt_iter:
    #     # funcion que retorna los centroides, para cada grupo
    #     # crea los nuevos centroides
    #     # get centroides
    #     indice_d_groups = get_index_of_elements(datos_g, centroides_g)
    #     print(indice_d_groups)
    #     # los grupos anteriores seran = a los nuevos grupos obtenidos
    #     # lo
    #     centroides_g = get_centroids(datos_g, indice_d_groups)
    #     print(centroides_g)
    
    #     count += 1
    # print()



# for i in range(5):
#     print(i)
#     # print 5 veces



import numpy as np
import math


d1 = np.array([45,8,6])
d2 = np.array([50,4,6])


d3 = d1 - d2
re = max(d3)
print(d3)
print(re)



print(d1**2)
print(np.sum(d2))
print(np.sum(d3))

# def dif_centroid(c1, c2):
#     diff = c1 - c2
#     max_element = max([ float(i) for i in diff])
#     if max_element < 0.5:
#         return True
#     else:
#         return False

