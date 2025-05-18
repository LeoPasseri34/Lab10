import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, year):
        self._nodes = DAO.getNodes(year)
        self._idMap = {}
        for node in self._nodes:
            self._idMap[node.CCode] = node

        self._graph.clear()
        confini = DAO.getEdges(self._idMap, year)
        self._graph.add_nodes_from(self._nodes)
        for c in confini:
            self._graph.add_edge(c.c1, c.c2)


    def getNodes(self):
        return list(self._graph.nodes)

    def infoCompConnessa(self):
        return nx.number_connected_components(self._graph)

    def getNumConfini(self, v):
        return len(list(self._graph.neighbors(v)))

    def getRaggiungibili(self, n):
        a = self.getRaggiungibiliDFS(n)
        print(f"{len(a)}")
        return a

    def getRaggiungibiliDFS(self, n):
        tree = nx.dfs_tree(self._graph, n)
        a = list(tree.nodes)
        a.remove(n)
        return a


