import math
import random


def set_seed(seed):
    random.seed(seed)


def dd_algorithm(n, theta, m):
    # Initialize variables
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    positiveTests = set()
    markedIndividuals = set()
    positiveTestsWith1Individual = {}
    for individual in range(n):
        # Find delta unique tests to match to each individual
        matchedTests = random.sample(range(n, n + m), delta)
        # Match the individuals to tests
        if individual < infectedNo:
            # If the individual is in the infected range, then label any connected tests as +ve
            for test in matchedTests:
                if test not in positiveTests:
                    positiveTestsWith1Individual[test] = individual
                elif test in positiveTestsWith1Individual:
                    positiveTestsWith1Individual.pop(test)
                positiveTests.add(test)
        else:
            add = True
            for test in matchedTests:
                if test not in positiveTests:
                    add = False
                    break
            if add:
                for test in matchedTests:
                    if test in positiveTestsWith1Individual:
                        positiveTestsWith1Individual.pop(test)
    # Find all positive tests connected to only 1 individual, and add the found individuals to the set
    for test in positiveTestsWith1Individual:
        markedIndividuals.add(positiveTestsWith1Individual[test])
    return markedIndividuals


