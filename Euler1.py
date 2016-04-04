"""I'm attempting to find the sum of all multiples of 3 or 5 below 1000."""
euler = []
x = lambda x: filter(x in range(0,1001) if x % 3 == 0, euler)

print x(3)