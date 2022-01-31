from DDAlgorithm import dd_algorithm
import matplotlib.pyplot as plt
import math

from DDAlgorithmSlow import dd_algorithm_slow

n = int(input("Enter n: "))
theta = float(input("Enter theta: "))
infectedNo = round(math.pow(n, theta))
iltb = (max(theta, 1 - theta) * math.pow(n, theta) * math.log(n)) / math.pow(math.log(2), 2)
print("Information Theoretic Lower Bound: " + str(iltb))
lowerBound = int(input("Enter lower bound for m: "))
upperBound = int(input("Enter upper bound for m: "))
step = int(input("Enter step for m: "))
repeat = int(input("Repeat 5 times? (type 1 for yes) "))

x = []

tempX = lowerBound
while tempX <= upperBound:
    x.append(tempX)
    tempX = tempX + step

y = []
x2 = [iltb, iltb]
y2 = [0, 100]

print("Running Algorithm...")

for m in x:
    print(m)
    # Repeat each value 5 times
    yValue = 0
    if repeat == 1:
        for i in range(5):
            yValue = yValue + (100 * (len(dd_algorithm_slow(n, theta, m, False)) / infectedNo))
        yValue = yValue / 5
    else:
        yValue = 100 * (len(dd_algorithm_slow(n, theta, m, False)) / infectedNo)
    y.append(yValue)

plt.plot(x, y, label=" ")
plt.plot(x2, y2, label="  ")
plt.xlabel("Number of tests")
plt.ylabel("% of found individuals")
plt.title("Graph for n = " + str(n) + " and theta = " + str(theta))
plt.show()

