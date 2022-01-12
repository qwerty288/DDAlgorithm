from DDAlgorithm import dd_algorithm
import matplotlib.pyplot as plt
import math


n = int(input("Enter n: "))
theta = float(input("Enter theta: "))
infectedNo = round(math.pow(n, theta))
iltb = (max(theta, 1 - theta) * math.pow(n, theta) * math.log(n)) / math.pow(math.log(2), 2)
print("Information Theoretic Lower Bound: " + str(iltb))
lowerBound = int(input("Enter lower bound for m: "))
upperBound = int(input("Enter upper bound for m: "))
step = int(input("Enter step for m: "))

x = []

tempX = lowerBound
while tempX < upperBound:
    x.append(tempX)
    tempX = tempX + step

y = []
x2 = [iltb, iltb]
y2 = [0, 100]

print("Running Algorithm...")

for m in x:
    # Repeat each value 5 times
    yValue = 0
    for i in range(5):
        yValue = yValue + round(100 * (len(dd_algorithm(n, theta, m)) / infectedNo))
    print(m)
    yValue = yValue / 5
    y.append(yValue)

plt.plot(x, y, label=" ")
plt.plot(x2, y2, label="  ")
plt.xlabel("Number of tests")
plt.ylabel("% of found individuals")
plt.title("Graph for n = " + str(n) + " and theta = " + str(theta))
plt.show()

