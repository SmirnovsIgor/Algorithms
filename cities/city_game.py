import sys


def find_all_routes(graph, start, end, path=[]):
    paths = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_routes(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


if __name__ == '__main__':
    cities = []
    graph = {}
    total = {}

    try:
        with open(f'{sys.argv[1]}', 'r') as file:
            for line in file:
                cities.append(line.strip())
    except FileNotFoundError:
        print('File not found')

    for city in cities:
        edges = []
        other_cities = [oc for oc in cities if oc != city]
        for c in other_cities:
            if c[0].upper() == city[-1:].upper():
                edges.insert(1, c)
        graph.update({city: edges})

    for city in cities:
        other_cities = [oc for oc in cities if oc != city]
        for c in other_cities:
            results = find_all_routes(graph, city, c)
            for res in results:
                total.update({len(res) : res})

    result = total.get(max(total))
    print (' -> '.join(result))
    print ('True') if len(result) == len(cities) and result[-1][-1] == result[0][0].lower() else print('False')