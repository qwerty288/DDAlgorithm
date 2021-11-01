import math
import random
import networkx as nx


def dd_algorithm(n, theta, m):
    # initialize variables
    infectedNo = math.pow(n, theta)
    delta = round((m * math.log(2)) / infectedNo)
    infectedNo = round(infectedNo)
    positiveTests = set()
    positiveIdentifiedIndividuals = set()
    G = nx.Graph()
    # generate bipartite graph matching individuals to tests
    for x in range(m, m + n):
        matchedTests = random.sample(range(0, m), delta)
        for i in matchedTests:
            G.add_edge(x, i)
    # create test results (consider individuals m to m+infectedNo as infected and mark their connected tests as +ve)
    for x in range(m, m + infectedNo):
        for i in list(G.neighbors(x)):
            positiveTests.add(i)
    # remove individuals connected to a negative test from the graph
    for x in range(0, m):
        if x not in positiveTests and G.has_node(x):
            for i in list(G.neighbors(x)):
                G.remove_node(i)
    # find all positive tests connected to only 1 individual, and mark the individual
    for x in range(0, m):
        if x in positiveTests:
            connectedIndividuals = list(G.neighbors(x))
            if len(connectedIndividuals) == 1:
                positiveIdentifiedIndividuals.add(connectedIndividuals[0])
    # print length of set containing such individuals
    print(len(positiveIdentifiedIndividuals))


dd_algorithm(49, 0.5, 49)
