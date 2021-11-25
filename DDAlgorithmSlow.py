import math
import random
import networkx as nx
import matplotlib.pyplot as plt


def set_seed_slow(seed):
    random.seed(seed)


def dd_algorithm_slow(n, theta, m):
    # Initialize variables
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    positiveTests = set()
    markedIndividuals = set()
    # individualsSet = set()
    G = nx.Graph()
    # Generate bipartite graph matching individuals to tests
    for x in range(n):
        # individualsSet.add(x)
        # Match each individual to delta unique tests
        matchedTests = random.sample(range(n, m + n), delta)
        for i in matchedTests:
            G.add_edge(x, i)

    # Display graph
    # nx.draw_networkx(G, pos=nx.drawing.layout.bipartite_layout(G, individualsSet))
    # plt.show()

    # Generate test results using the assumption that individuals in range(infectedNo) are infected
    for x in range(infectedNo):
        for i in list(G.neighbors(x)):
            positiveTests.add(i)
    # Remove individuals connected to a negative test from the graph
    for x in range(n, m + n):
        if x not in positiveTests and G.has_node(x):
            for i in list(G.neighbors(x)):
                G.remove_node(i)
    # Iterate through all positive tests
    for x in positiveTests:
        # If the test is connected to only one individual, then mark this individual
        connectedIndividuals = list(G.neighbors(x))
        if len(connectedIndividuals) == 1:
            markedIndividuals.add(connectedIndividuals[0])
    # Return set of marked individuals
    return markedIndividuals
