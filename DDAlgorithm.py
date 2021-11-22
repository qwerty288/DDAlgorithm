import math
import random
import time

# Input : n, theta, m
# Output : set of marked individuals

random.seed(1)

def dd_algorithm(n, theta, m):
    # Initialize variables
    positiveTests = set()
    infectedNo = round(math.pow(n, theta))
    delta = round((m * math.log(2)) / infectedNo)
    markedIndividuals = set()
    testToIndividuals = {}
    # Generate bipartite graph matching each individual to delta tests
    for individual in range(infectedNo):
        # Pick delta tests to match
        matchedTests = random.sample(range(n, n + m), delta)
        for test in matchedTests:
            # Create mapping
            if test not in testToIndividuals:
                testToIndividuals[test] = set()
            testToIndividuals[test].add(individual)
            # Any test connected to this range of individuals is positive
            positiveTests.add(test)
    # No more positive tests can be created at this point
    for individual in range(infectedNo, n):
        # Pick delta tests to match
        matchedTests = random.sample(range(n, n + m), delta)
        for test in matchedTests:
            # Create mapping
            if test in positiveTests:
                # If the individual is mapped to a negative test, then it will be removed anyway
                # Thus, only mappings connecting an individual to a positive test are added
                testToIndividuals[test].add(individual)


    # Find all positive tests connected to only 1 individual, and mark the individual
    for test in positiveTests:
        if len(testToIndividuals[test]) == 1:
            for individual in testToIndividuals[test]:
                markedIndividuals.add(individual)
    # Return set of marked individuals
    return markedIndividuals

# start = time.time()
print(dd_algorithm(100000, 0.8, 50000))
# end = time.time()
# print(str(end - start))

