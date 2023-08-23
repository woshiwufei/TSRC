import copy
import random

import networkx as nx


def select_seeds(centrality, RS_, k):
    for ii in RS_:
        centrality[ii] = 0

    top = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

    SS = []
    for ii in range(k):
        SS.append(top[ii][0])

    return SS


def findSeeds(G, RS_, k, method_name=None):
    SS = []
    allNodes = list(set(G.nodes) - set(RS_))
    if method_name == "random":
        SS = random.sample(allNodes, k)
        pass
    elif method_name == "betweeness":
        SS = select_seeds(nx.centrality.betweenness_centrality(G), RS_, k)

    elif method_name == "pageRank":
        SS = select_seeds(nx.pagerank(G), RS_, k)

    elif method_name == "degree":
        SS = select_seeds(nx.centrality.degree_centrality(G), RS_, k)
    return SS


def read_data(path: str):
    """
    从path读取数据集
    """
    G = nx.DiGraph()
    with open(path) as ff:
        n, m, start, w, directed = ff.readline().split()
        node_num = int(n)
        edge_num = int(m)
        start = int(start)
        start_ = start
        w = int(w)
        directed = int(directed)
        G.add_nodes_from(range(node_num))
        if w == 0:
            for line in ff:
                n, m = line.split()
                # n, m, w = line.split()
                # G.add_edge(int(n) - 1, int(m) - 1)
                # G.add_edge(int(m) - 1, int(n) - 1)
                if n == m:
                    continue
                G.add_edge(int(n) - start, int(m) - start)
                G[int(n) - start][int(m) - start]['weight'] = 0.1
                if directed != 1:
                    G.add_edge(int(m) - start, int(n) - start)
                    G[int(m) - start][int(n) - start]['weight'] = 0.1

                    # G.remove_edge(int(n - 1), int(m - 1))
                    # G.remove_edge(int(m - 1), int(n - 1))
        else:
            for line in ff:
                n, m, w = line.split()
                if n == m:
                    continue
                G.add_edge(int(n) - start, int(m) - start)
                G[int(n) - start][int(m) - start]['weight'] = float(w)
                if directed != 1:
                    G.add_edge(int(m) - start, int(n) - start)
                    G[int(m) - start][int(n) - start]['weight'] = float(w)
        print("Graph created***")
    return G


def main_func(path, RS, k):
    # graph = nx.read_weighted_edgelist(path, create_using=nx.DiGraph(), nodetype=int)
    start_ = 0
    graph = read_data(path)
    # edges = list(graph.edges)
    # for i in range(len(edges)):
    #     graph[edges[i][0]][edges[i][1]]['weight'] = 0.1

    SS = {}

    methods = ['random', 'betweeness', 'degree', 'pageRank']
    for i in range(len(methods)):
        method = methods[i]
        SS[method] = []
        SS[method] = findSeeds(graph, RS, k, method)
    return SS
