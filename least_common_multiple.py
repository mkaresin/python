num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

setA = set([x * num1 for x in range(1, num2+1)])
setB = set([x * num2 for x in range(1, num1+1)])

setIntersection = setA.intersection(setB)

lcm = (sorted(setIntersection)[0])

print("lcm =", lcm)
