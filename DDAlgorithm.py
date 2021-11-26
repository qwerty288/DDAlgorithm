import math
import random


def set_seed(seed):
    random.seed(seed)

# Implementation Complexity - O(m + (n * delta))


def dd_algorithm(n, theta, m):
    # Initialize variables
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    positiveTests = set()
    markedIndividuals = set()
    testToIndividuals = {}
    positiveTestsWith1Individual = {}
    """
    Generate bipartite graph matching the individuals to tests
    The permutation of infected and non-infected individuals is not a required input for the algorithm 
    Thus, we will consider the individuals in range(infectedNo) to be infected, for ease of implementation
    """
    # Complexity - O(n * delta)
    for individual in range(n):
        # Find delta unique tests to match to each individual
        matchedTests = random.sample(range(n, n + m), delta) # need the positive tests that only appear once
        # Match the individuals to tests
        if individual < infectedNo:
            # If the individual is in the infected range, then label any connected tests as +ve
            for test in matchedTests:
                if test not in positiveTests:
                    positiveTestsWith1Individual[test] = individual
                elif test in positiveTestsWith1Individual:
                    positiveTestsWith1Individual.pop(test)
                if test not in testToIndividuals:
                    testToIndividuals[test] = set()
                testToIndividuals[test].add(individual)
                positiveTests.add(test)
        else:
            """
            If the individual is not in the infected range, then only add the individual
            to the graph if all the assigned tests are in positiveTests
            As no individual in this range are infected, no more +ve tests can be created
            Thus, any test not in positiveTests is negative
            If an individual matching to one or more -ve tests is added, then it would have
            been removed anyway, due to being connected to -ve test(s)
            """
            add = True
            for test in matchedTests:
                if test not in positiveTests:
                    add = False
                    break
            if add:
                for test in matchedTests:
                    if test in positiveTestsWith1Individual:
                        positiveTestsWith1Individual.pop(test)
                    testToIndividuals[test].add(individual)
    # Find all positive tests connected to only 1 individual, and add the found individuals to the set
    return set(positiveTestsWith1Individual.values())




