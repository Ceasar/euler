
def linked_list(length):
    nodes = [Node(None)]
    for i in range(length - 1):
        end = Node([nodes[-1]])
        nodes.append(end)
    return nodes

def link(a, b):
    map(lambda x, y: x['neighbors'].append(y), a, b)
    return b

def matrix(height, width):
    graph = [linked_list(height) for w in range(width)]
    reduce(link, graph)
    return graph

class Node(dict):
    def __init__(self, neighbors=None):
        if neighbors is None:
            neighbors = []
        super(Node, self).__init__({'neighbors': neighbors})

class Graph(set):
    def __init__(self, nodes):
        super(Graph, self).__init__(nodes)
