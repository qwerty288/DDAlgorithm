from DDAlgorithm import dd_algorithm
import matplotlib.pyplot as plt
import math


n = int(input("Enter n: "))
theta = float(input("Enter theta: "))
infectedNo = round(math.pow(n, theta))
iltb = (max(theta, 1 - theta) * math.pow(n, theta) * math.log(n)) / math.pow(math.log(2), 2)
print("Information Theoretic Lower Bound: " + str(iltb))
print("Enter values for m, or type '-1' to generate graph: ")
x = []
y = []
x2 = [iltb, iltb]
y2 = [0, 100]

while 1 == 1:
    inputLine = int(input(""))
    if inputLine == -1:
        break
    else:
        x.append(inputLine)


print("Running Algorithm...")

for m in x:
    y.append(round(100 * (len(dd_algorithm(n, theta, m)) / infectedNo)))

plt.plot(x, y, label=" ")
plt.plot(x2, y2, label="  ")
plt.xlabel("Number of tests")
plt.ylabel("% of found individuals")
plt.title("Graph for n = " + str(n) + " and theta = " + str(theta))
plt.show()

