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
    """
    The bipartite graph generated by the algorithm is independent to the permutation of individuals in the input
     population. For ease of implementation, this implementation considers individuals in range 0 ≤ i < a to be infected
     , and individuals in range a ≤ i < n non-infected (where a is the number of infected individuals, and n is the
     population size). 
    """
    for individual in range(n):
        # Find delta unique tests to match to each individual
        matchedTests = random.sample(range(n, n + m), delta)
        # Match the individuals to tests
        if individual < infectedNo:
            # If the individual is in the infected range, then label any connected tests as +ve
            for test in matchedTests:
                if test not in positiveTests:
                    # Only preserve test nodes which are connected to only one individual
                    positiveTestsWith1Individual[test] = individual
                elif test in positiveTestsWith1Individual:
                    positiveTestsWith1Individual.pop(test)
                positiveTests.add(test)
        else:
            """ 
            If the individual is due to be matched to a negative test then it is not added to the graph, as it 
            would've been removed anyway. If the individual is due to be matched with only +ve tests, then
            check which tests in positiveTestsWith1Individual are affected. No new tests are added to this dict,
            as no more +ve tests can be created.
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
    # Return the set of values for the positiveTestsWith1Individual dictionary
    for test in positiveTestsWith1Individual:
        markedIndividuals.add(positiveTestsWith1Individual[test])
    return markedIndividuals

