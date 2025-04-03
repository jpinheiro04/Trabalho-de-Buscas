DISTANCE = 0
PREVIOUS_NODE = 1
INFINITY = float("inf")

graph = {}
graph["A"] = {"B":5, "D":9, "E":2}
graph["B"] = {"A":5, "C":2}
graph["C"] = {"B":2, "D":3}
graph["D"] = {"A":9, "F":2, "C":3}
graph["E"] = {"A":2, "F":3}
graph["F"] = {"E":3, "D":2}

table = {
    "A": [0, None],
    "B": [INFINITY, None],
    "C": [INFINITY, None],
    "D": [INFINITY, None],
    "E": [INFINITY, None],
    "F": [INFINITY, None]
}

def get_shortest_distance(table, vertex):

    return table[vertex][DISTANCE]

def set_shortest_distance(table, vertex, distance):

    table [vertex][DISTANCE] = distance

def set_previous_node(table, vertex, node):

    table[vertex][PREVIOUS_NODE] = node

def get_distance(graph, first_vertex, second_vertex):

    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes):

    unvisited = list(
        set(
            table.keys()
        ).difference(visited_nodes)
    )

    min_distance = INFINITY
    vertex = None

    for node in unvisited:
        if table[node][DISTANCE] < min_distance:
            min_distance = table[node][DISTANCE]
            vertex = node
    
    return vertex

def find_shortest_path(graph: dict, table: dict, origin: str = "A"):

    visited = []
    current_node = origin
    starting_node = origin

    while True:
        adjacent_nodes = graph[current_node]

        for vertex in adjacent_nodes:
            distance_from_starting_node = get_shortest_distance(table, vertex)

            if(distance_from_starting_node == INFINITY) and (current_node == starting_node):
                total_distance = get_distance(graph, vertex, current_node)
            else:
                total_distance = get_shortest_distance(table, current_node)
                total_distance += get_distance(graph, current_node, vertex)

            if total_distance < distance_from_starting_node:
                set_shortest_distance(table, vertex, total_distance)
                set_previous_node(table, vertex, current_node)

        visited.append(current_node)

        if len(visited) == len(table.keys()):
            break
        
        current_node = get_next_node(table, visited)

    return table

def rotas(destino, solucoes):
    rota = []
    atual = destino
    while atual is not None:
        rota.append(solucoes[atual][1])
        atual = solucoes[atual][1]
    return rota[::-1]

result = find_shortest_path(graph, table, 'A')
print(result)

gps = rotas("D, table")
print(gps)