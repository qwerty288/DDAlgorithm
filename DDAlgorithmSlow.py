import math
import random
import networkx as nx
import copy


def set_seed_slow(seed):
    random.seed(seed)


def valid_graph(G, delta, n, m):
    # Check if all edges connect an individual to a test
    for edge in G.edges:
        a = edge[0]
        b = edge[1]
        if a not in range(n) and b not in range(n, m + n) or a not in range(n, m + n) and b not in range(n):
            return False
    # Check if each individual node has degree delta
    for individual in range(n):
        if len(list(G.neighbors(individual))) != delta:
            return False
    return True


def removed_correctly(new_G, original_G, n, positiveTests):
    # Check if the correct individuals have been removed
    for individual in range(n):
        connectedToOnlyPositiveTest = True
        connectedTests = list(original_G.neighbors(individual))
        for test in connectedTests:
            if test not in positiveTests:
                connectedToOnlyPositiveTest = False
                break
        if connectedToOnlyPositiveTest and individual not in new_G:
            return False
        if not connectedToOnlyPositiveTest and individual in new_G:
            return False
    return True


def dd_algorithm_slow(n, theta, m, test):
    # Initialize variables
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    if delta == 0:
        return set()
    positiveTests = set()
    markedIndividuals = set()
    G = nx.Graph()
    # Generate bipartite graph matching individuals to tests (Complexity - O(n * delta))
    for x in range(n):
        # Match each individual to delta unique tests
        matchedTests = random.sample(range(n, m + n), delta)
        for i in matchedTests:
            G.add_edge(x, i)
    # Check if the graph has been correctly generated
    G2 = copy.deepcopy(G)
    if test and not valid_graph(G, delta, n, m):
        return False
    # Generate test results using the assumption that individuals in range(infectedNo) are infected
    # (Complexity - O(n^theta * delta))
    for x in range(infectedNo):
        for i in list(G.neighbors(x)):
            positiveTests.add(i)
    # Remove individuals connected to a negative test from the graph
    for x in range(n, m + n):
        if x not in positiveTests and G.has_node(x):
            for i in list(G.neighbors(x)):
                G.remove_node(i)
    # Check if above step has been performed correctly
    if test and not removed_correctly(copy.deepcopy(G), G2, n, positiveTests):
        return False
    # Iterate through all positive tests
    for x in positiveTests:
        # If the test is connected to only one individual, then mark this individual
        connectedIndividuals = list(G.neighbors(x))
        if len(connectedIndividuals) == 1:
            markedIndividuals.add(connectedIndividuals[0])
    # Return set of marked individuals
    return markedIndividuals



