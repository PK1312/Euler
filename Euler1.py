"""I'm attempting to find the sum of all multiples of 3 or 5 below 1000."""
solution = []

for number in range(0,1000):
    if number % 3 == 0 or number % 5 == 0:
        solution.append(number)

print sum(solution)
