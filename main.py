from typing import List

import target as target


class Node:
    def __init__(self, name: str, location: (int, int)):
        self.name = name
        self.neighbors = []
        self.neighbors_weight = dict()
        self.location = location

    def connect_nodes(self, a: __init__, weight):
        self.neighbors.append(a)
        self.neighbors_weight[a] = weight
        a.neighbors.append(self)
        a.neighbors_weight[self] = weight


def dijkstra(s: Node, graph: List[Node]):
    is_visited = dict()
    node_distances = dict()
    pq = []
    for node in graph:
        node_distances[node.name] = float("inf")
        is_visited[node.name] = False
    node_distances[s.name] = 0
    pq.append(s)
    while len(pq) != 0:
        current = pq[0]
        pq.remove(current)
        is_visited[current.name] = True
        for node in current.neighbors:
            # if node_distances[i] > node_distances[name] + name.neighbors_weight[i]:
            #     node_distances[i] = node_distances[name] + name.neighbors_weight[i]
            node_distances[node.name] = min(node_distances[current.name] + current.neighbors_weight[node],
                                            node_distances[node.name])
            if not is_visited[node.name]:
                pq.append(node)
        pq.sort(key=lambda node: node_distances[node.name])
    return node_distances


def main():
    s = Node("s", (65, 67))
    a = Node("a", (191, 76))
    b = Node("b", (64, 154))
    c = Node("c", (196, 159))
    d = Node("d", (69, 235))
    e = Node("e", (216, 256))

    s.connect_nodes(a, 2)
    s.connect_nodes(b, 4)

    a.connect_nodes(b, 1)
    a.connect_nodes(c, 7)

    b.connect_nodes(d, 3)

    c.connect_nodes(d, 2)
    c.connect_nodes(e, 1)

    d.connect_nodes(e, 5)
    distances = dijkstra(s, [s, a, b, c, d, e])
    for i in distances:
        print(i, distances[i])
    # print(dijkstra(s, e, [s, a, b, c, d, e]))


if __name__ == "__main__":
    main()
