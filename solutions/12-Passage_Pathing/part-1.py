# Day 12 : Passage Pathing

## Part 1


from collections import defaultdict


class CaveNetwork:

    def __init__(self, network):
        self.network = network
    
    @classmethod
    def from_tuples(cls, edges):
        network = defaultdict(set)
        for n1, n2 in edges:
            network[n1].add(n2)
            network[n2].add(n1)
        return CaveNetwork(network)

    def count_routes(self, node="start", visited=None):
        visited = [] if visited is None else visited
        if node == "end":
            return 1
        if node.islower() and node in visited:
            return 0
        nodes = self.network[node]
        return sum(self.count_routes(n, visited + [node]) for n in nodes)


# load edges
edge_strings = open("edges.txt").read().split("\n")
edges = [tuple(edge.split("-")) for edge in edge_strings]

# create network
cave_network = CaveNetwork.from_tuples(edges)

# count routes
print(cave_network.count_routes())