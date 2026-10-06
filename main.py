from dijkstra import dijkstra
from grafo import grafo
from farmacias import pedidos

from grafo import grafo
from dijkstra import dijkstra


posicion = "S"
coste_total = 0
ruta = ["S"]


# Estado de los pedidos
pedido1_recogido = False
pedido1_entregado = False

pedido2_recogido = False
pedido2_entregado = False

pedido3_recogido = False
pedido3_entregado = False


while not (pedido1_entregado and pedido2_entregado and pedido3_entregado):

    sitios = []

    # PEDIDO 1
    # Se recoge en F y se entrega en T
    if pedido1_recogido == False:
        sitios.append("F")
    elif pedido1_entregado == False:
        sitios.append("T")


    # PEDIDO 2
    # Se recoge en F y se entrega en E
    if pedido2_recogido == False:

        if "F" not in sitios:
            sitios.append("F")

    elif pedido2_entregado == False:
        sitios.append("E")


    # PEDIDO 3
    # Se recoge en T y se entrega en D
    if pedido3_recogido == False:

        if "T" not in sitios:
            sitios.append("T")

    elif pedido3_entregado == False:
        sitios.append("D")


    # Dijkstra desde donde estamos
    distancias = dijkstra(grafo, posicion)


    # Suponemos primero que el sitio más cercano
    # es el primero de la lista
    siguiente = sitios[0]


    # Comparamos con los demás
    for sitio in sitios:

        if distancias[sitio] < distancias[siguiente]:
            siguiente = sitio


    # Sumamos el coste
    coste_total = coste_total + distancias[siguiente]

    print(posicion, "->", siguiente, "coste:", distancias[siguiente])


    # Nos movemos
    posicion = siguiente
    ruta.append(posicion)


    # RECOGER PEDIDOS

    if posicion == "F":

        if pedido1_recogido == False:
            pedido1_recogido = True
            print("Recogemos pedido 1")

        if pedido2_recogido == False:
            pedido2_recogido = True
            print("Recogemos pedido 2")


    if posicion == "T":

        if pedido3_recogido == False:
            pedido3_recogido = True
            print("Recogemos pedido 3")


    # ENTREGAR PEDIDOS

    if posicion == "T" and pedido1_recogido == True:
        if pedido1_entregado == False:
            pedido1_entregado = True
            print("Entregamos pedido 1")


    if posicion == "E" and pedido2_recogido == True:
        if pedido2_entregado == False:
            pedido2_entregado = True
            print("Entregamos pedido 2")


    if posicion == "D" and pedido3_recogido == True:
        if pedido3_entregado == False:
            pedido3_entregado = True
            print("Entregamos pedido 3")


print()
print("Ruta:", ruta)
print("Coste total:", coste_total)