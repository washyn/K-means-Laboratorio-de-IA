from algoritm_kmeans import *



datos_puntos = np.array([[2,2],
    [4,2],
    [3,3],
    [2,4],
    [5,4],
    [7,2],
    [8,3],
    [8,4]]
)

d = [[2,2],
    [4,2],
    [3,3],
    [2,4],
    [5,4],
    [7,2],
    [8,3],
    [8,4]]

# def prueba_indice_d_punto_min():
#     centroids = np.array([[4,2],[3,3],[2,4]])
#     punto = np.array([2,2])
#     print(get_index_of_centroid_mas_cerca(punto, centroids))





def prueba_distacia():
    # print(calcular_distancia(datos_puntos[0],datos_puntos[3]))
    assert(calcular_distancia(datos_puntos[0],datos_puntos[3]) == 2.0)
    # print(calcular_distancia(datos_puntos[0:3], datos_puntos[4:7]))
    # print("ok")
    # assert(calcular_distancia(datos_puntos[0],datos_puntos[3]))


# def prueba_calc_nuevos_centroiddes():
#     # print(datos_puntos[0:5,])
#     # print(calcular_centroide(datos_puntos[0:5,]))

#     # print(datos_puntos[5:,])
#     # print(calcular_centroide(datos_puntos[5:,]))

#     tmp = np.array([datos_puntos[1],datos_puntos[4]])
#     print(datos_puntos[1],datos_puntos[4])
#     print(calcular_centroides(datos_puntos))
#     print("ok")



if __name__ == '__main__':
    # prueba_indice_d_punto_min()
    # prueba_distacia()

    
    for i in range(len(d)-2):
        print(d[i],d[i+1],d[i+2])