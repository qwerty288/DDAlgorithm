import math
import random

import networkx as nx
import matplotlib.pyplot as plt

# n individuals, n^theta infected and m tests
def DDAlgorithm(n,theta, m):
    # initialize vars
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    positiveTests = set()
    positiveIdentifiedIndividuals = set()
    individualsSet = set()
    G = nx.Graph()
    # generate bipartite graph matching individuals to tests
    for x in range(n):
        individualsSet.add(x+m)
        matchedTests = random.sample(range(0, m), delta)
        for i in matchedTests:
            G.add_edge(x+m, i)
    # display generated bipartite graph
    nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, individualsSet))
    plt.show()
    # save test results
    for x in range(infectedNo):
        for i in list(G.neighbors(x+m)):
            positiveTests.add(i)
    # remove individuals connected to a negative test
    for x in range(0, m):
        if x not in positiveTests and G.has_node(x):
            for i in list(G.neighbors(x)):
                G.remove_node(i)
    # find all individuals connected to 1 positive test
    for x in range(0, m):
        if x in positiveTests:
            connectedIndividuals = list(G.neighbors(x))
            if len(connectedIndividuals) == 1:
                positiveIdentifiedIndividuals.add(connectedIndividuals[0])
    # print set of found individuals
    print(positiveIdentifiedIndividuals)

DDAlgorithm(20, 0.5, 10)






