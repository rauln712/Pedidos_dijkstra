import heapq


def dijkstra(grafo, origen):

    dist = {nodo: float("inf") for nodo in grafo}

    dist[origen] = 0

    cola = [(0, origen)]  # (distancia, nodo)

    cerrados = set()


    while cola:

        d, u = heapq.heappop(cola)

        if u in cerrados:
            continue

        cerrados.add(u)


        for v, peso in grafo[u].items():

            if d + peso < dist[v]:

                dist[v] = d + peso

                heapq.heappush(cola, (dist[v], v))


    return dist