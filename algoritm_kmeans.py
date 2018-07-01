# Apellido y nom: 	Acero Mamani Washington
# Codigo:			141850

# para el manejo de arrays numpy
# para seleccionar elementos aleatorios de la muentra, 
#   centroides aleatorios
# math para funciones matematicas
import numpy as np
import random
import math
import matplotlib.pyplot as plt

# si se le pasa un vector con los puntos
# retorna un vecntor con las distancias
# calcula la distancia entre 2 puntos
def calcular_distancia(punto1, punto2):
    return np.sqrt(np.sum((punto1 - punto2)**2))


# return en indice del centroide al que pertenece
# devuelve el indice del centroide mas cerca al punto
def get_indice_d_centrd_mas_cerca(punto, centroides):
    distancias = [calcular_distancia(punto, i) for i in centroides]
    # distancias = np.array([calcular_distancia(punto, i) for i in centroides])
    # return min(distancias, key=distancias.get)
    return distancias.index(min(distancias)) 


# retorna los una lista de clusters o grupos
def get_clusters(datos, indices_d_grupos):
    # clusters = np.array()
    k = max(indices_d_grupos) + 1
    m = len(indices_d_grupos)
    res = [[] for i in range(0,k)]
    for i in range(0, m):
        res[indices_d_grupos[i]].append(datos[i])
    return np.array(res)


# retorna el centroide de un conjunto de puntos
def get_centroide(puntos):
    cantidad_de_datos = len(puntos)
    x,y = 0,0
    for i in puntos:
        x += i[0]
        y += i[1]
    return [x/cantidad_de_datos, y/cantidad_de_datos]


# retorna un array con los centroides de cada grupo
def calcular_centroides(datos, indices_d_grupos):
    clusters = get_clusters(datos, indices_d_grupos)
    return np.array([get_centroide(i) for i in clusters])


# retorna un array con los indices a los que pertenece cada elemento(dato)
# todos los datos 
# array de centroides
def calcular_grupos(datos, centroides):
    # para cada uno de los datos determinar la distancia hacia los centroides    
    # returna los indices de los grupos al que c/u pertenece
    return np.array([get_indice_d_centrd_mas_cerca(i, centroides) for i in datos])


# una iteracion de kmeans quer retorna centroides y grupos
def kmeans_i(datos, centroides, grupos):
    # return una tupla de (centroides, grupos)
    return (calcular_centroides(datos, grupos),calcular_grupos(datos, centroides))
    

# lee los datos de un archivo
def read_data(fname, head = True):
    res = []
    with open(fname, "rt") as f:
        if head:
            f.readline()
        for i in f.readlines():
            dat = i.split(",")
            res.append([float(dat[0]), float(dat[1])])
            # res.append(dat)
    return np.array(res)


# selecciona valores aleatorios de data que seran centroides iniciales
def get_rand_centroids(data, k):
    return np.array([data[random.randint(0,len(data))]  for i in range(k)])



def variacion_de_centroide(c1, c2):
    # si la diferencia es de menor a 0.5 entonces ya convergio
    def dif_centroid(c1, c2):
        k = len(c1)
        diff = [calcular_distancia(c1[i],c2[i]) for i in range(k)]
        max_element = max(diff)
        # print("dist",max_element)
        if max_element < 0.01:
            return True
        else:
            return False

    return not dif_centroid(c1, c2)




# #############################################################
# para un i in range(m)
# #############################################################
# K = numero de clusters, grupos
# #############################################################
# C[i]  o g_indx_grupos[i] lista de indices a los grupos que pertenecen
#         indice del cluster al que esta asignado x[i] esta asignado a cluster

#         𝑐(𝑖)=í𝑛𝑑𝑖𝑐𝑒𝑑𝑒𝑙𝑐𝑙ú𝑠𝑡𝑒𝑟1,2,…,𝐾𝑎𝑙𝑐𝑢𝑎𝑙𝑒𝑙𝑒𝑗𝑒𝑚𝑝𝑙𝑜𝑥(𝑖)
#         𝑒𝑠𝑡á𝑎𝑐𝑡𝑢𝑎𝑙𝑚𝑒𝑛𝑡𝑒𝑎𝑠𝑖𝑔𝑛𝑎𝑑𝑜.
        
#         ---> g_indx_grupos[i]
# #############################################################
# Uk = centroide del cluster k 
#     g_centroides[k]

#     ---> g_centroides[g_indx_grupos[i]]
#     ---> g_centroides[k]
# #############################################################
# Uc[i] = ubicacion del centroide del cluster al que se 
#     asigno x[i]
#     x[i]
#
#     datos[i] ubicacion de su centroide
#     g_indx_grupos[i]
#     ---> g_datos[i]
#     ---> g_centroides[g_indx_grupos[i]]
# #############################################################
    # g_centroides[g_indx_grupos[i]]
# #############################################################

# x datos
# c array con los indices a los que pertenecen los x
#   Ci hasta Cm, m longitud de muestras, len de data
# u centroides 
#   u1 hasta uk, k centroides
def cost_function(x, c, u):
    m = len(x)
    sumatoria = 0
    for i in range(m):
        # sumatoria += (x[i] - u[c[i]])**2
        sumatoria += np.sum((x[i] - u[c[i]])**2)
    return sumatoria/m


# para un conjunto de datos data, y k grupos
# retorna los cetroides calculados
# un array con los grupos creados
# y el valor del costo para k grupos
def kmeans(data,k):
    m = len(data)
    g_old_cetroides = get_rand_centroids(data, k)
    g_new_centroides = get_rand_centroids(data, k)
    g_grupos = None
    valor_de_costo = 0
    while variacion_de_centroide(g_old_cetroides, g_new_centroides):
        g_old_cetroides = g_new_centroides
        g_grupos = calcular_grupos(data, g_new_centroides)
        g_new_centroides = calcular_centroides(data, g_grupos)
        valor_de_costo = cost_function(data, g_grupos, g_new_centroides)
    return g_new_centroides, get_clusters(data, g_grupos), valor_de_costo
    


def main():
    g_datos = read_data("xclara.csv")
    m = len(g_datos)
    k = 3
    g_old_cetroides = get_rand_centroids(g_datos, k)
    g_new_centroides = get_rand_centroids(g_datos, k)
    print("Centroides iniciales aleatorios")
    for i in g_new_centroides:
        print(i)
        
    valor_de_f_cost = 0
    g_indx_grupos = None

    # mientras el centroide varie se sigue calculando
    # old y new para verificar la variacion de centroides
    while variacion_de_centroide(g_old_cetroides, g_new_centroides):
        # print("centroides -> ",g_new_centroides)
        g_old_cetroides = g_new_centroides
        
        g_indx_grupos = calcular_grupos(g_datos, g_new_centroides)
        g_new_centroides = calcular_centroides(g_datos, g_indx_grupos)
        # funcion costo J(c,u)
        valor_de_f_cost = cost_function(g_datos, g_indx_grupos, g_new_centroides)
        print("funcion costo para esta iteracion --> ",valor_de_f_cost)

    print("Centroides al final de las iteraciones")
    for i in g_new_centroides:
        print(i)

    print("costo final --> ",valor_de_f_cost)
    # no lo mostramos porque son demasiados datos en cada grupo
    # clusters = get_clusters(g_datos, g_indx_grupos)    
    # for i in clusters:
    #     print(list(i))



def pendiente(p1,p2):
    x,y = p1[0] - p2[0], p1[1] - p2[1]
    return y/x

def main_other():
    g_datos = read_data("F:\\lab de IA\\kmeans\\xclara.csv")
    # data = g_datos.
    x = g_datos[:,0]
    y = g_datos[:,1]
    plt.scatter(x, y, marker=".")
    plt.title("Nube de puntos")
    plt.show()
    k = 3
    # centroides, clusters, costo = kmeans(g_datos,k)
    x = []
    y = []
    d = []
    numero_de_pruebas_k = 10
    for i in range(numero_de_pruebas_k):
        k = i+1
        result = kmeans(g_datos, k)
        x.append(k)
        y.append(result[2])
        d.append([k,result[2]])
        print("para un K = %d el costo es -> %f"%(k, result[2]))


    pendientes = [[pendiente(d[i],d[i+1]),d[i][0]] for i in range(len(d)-1)]
    # para cual de las pendienes es mas la diferencia
    # diffs = [[pendientes[i][0] - pendientes[i+1][0], pendientes[i+1][1]] for i in range(len(pendientes)-1)]
    diffs = [math.fabs(pendientes[i][0] - pendientes[i+1][0]) for i in range(len(pendientes)-1)]
    ind_m = diffs.index(max(diffs))
    print(pendientes)
    print(diffs)
    # print(ind_m+1)
    # print(d[ind_m+1][0])
    print("el optimo k es -> ",x[ind_m+1])
    # en cual de los ... se dobla mas el ...
    # ver pendientes para cada 2 puntos y en cual de las pendientes varia mas
    
    plt.plot(x,y)
    plt.title("Valor de K vs funcion costo")
    plt.xlabel("Numero de clusters K")
    plt.ylabel("Valor de funcion costo: J(c,u)")
    plt.grid()
    plt.show()

    # print(centroides)
    # print(costo)



# public static double angleBetweenTwoPointsWithFixedPoint(
#         double p_1X, double p_1Y, 
#         double p_2X, double p_2Y, 
#         double fix_X, double fix_Y)

#     double angle1 = Math.atan2(p_1Y - fix_Y, p_1X - fix_X);
#     double angle2 = Math.atan2(p_2Y - fix_Y, p_2X - fix_X);
#     return angle1 - angle2; 


def angulo_entre_3_puntos(p1,p2,fix):
    angulo1 = math.atan2(p1[1] - fix[1], p1[0] - fix[0])
    angulo2 = math.atan2(p2[1] - fix[1], p2[0] - fix[0])
    return math.degrees(angulo1 - angulo2)



def elbow(data):
    def pendiente(p1,p2):
        x,y = p1[0] - p2[0], p1[1] - p2[1]
        return y/x
    

# EL PROGRAMA MOSTRARA LOS CENTROIDES Y LOS K GRUPOS PARA UN K

def get_k_for_data(data):
    return None

if __name__ == "__main__":
    # main()
    main_other()



# #############################################################################
# #############################################################################
# #############################################################################
# grupo y centroide

# para cada clusters determinar el centroides

# inicialmente no tenemos grupos
# se elige k
# k centroides aleatorios
# #############################################################################
# #############################################################################
# #############################################################################
# se elige la cantidad de centroides
# se elige al azar los centroides iniciales
# #############################################################################
# #############################################################################
#     # solo tener una coleccion de los indices a los que pertenecen a cada grupo
#     #     [1,2,3,0,1,2,1,2,1,1,0,]
# #############################################################################
# #############################################################################
# #############################################################################
# #############################################################################
#     agrupar los objetos en base a distancias minimas a los centroides,
#     para cada uno de los grupos calcular los nuevos centroides OKKK
#     desplazar los centroides en base a la media de los clusters
# #############################################################################
#     agrupar los objetos en base a distancias minimas a los centroides,
#     para cada uno de los grupos calcular los nuevos centroides
#     desplazar los centroides en base a la media de los clusters
# #############################################################################
# #############################################################################
# #############################################################################
# #############################################################################
# seleccion aleatoria de k observaciones
# #############################################################################
# asignar cada observacion al punto mas cercano
# calcular_centroide de c/u de los grupos
# #############################################################################
# volver a reasignar las observaciones en funcion de los nuevos centroides
# #############################################################################
# #############################################################################


    # var global grupos algo que siempre estara cambiando, 
    #   los centroides tambien, en base a esto se calcula los centroides
    """ funcion que retorne los grupos y los centroides, se le pasa
    los datos, centroides, indices a los centroides q pertenece cada elemento
    """
    """
    tenemos grupos y centroides
        grupos:esto en forma de (datos,indices a los centroides q pertenece c/u)
        centroides:array de centroides
    """
# tenemos 
# datos_global
# centroides_global

# g_grupos
# grupos = g_grupos -> grupos contiene un array con valores q indican a que 
#                      cluster pertenece cada elemento

    # g_grupos = calcular_grupos(g_datos, g_centroides)
    # print(g_grupos)
# calcular n veces:
    # print(g_centroides)
    # print(g_grupos)
    # print(g_centroides)
#   centroides = calcular_centroides((grupos,datos))
#   grupos = calcular_grupos(datos,centroides)
######################################################################
# se alamacenan los indices de los puntos




