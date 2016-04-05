fibbo = [0, 1, 1] #gotta have the first few digits
answer = [] #empty list for storing the even numbers to be summed
for number in fibbo: #iterate through every number in the fibbo list
    while fibbo[-1] <= 4000000: #ensures it stops within the bounds of the problem
        fibbo.append(fibbo[-1] + fibbo[-2]) #this grabs the last item in a list, then the second to last, adds them together
        				    #then appends it to "fibbo"
for number in fibbo: #iterates through everything in fibbo, now that it has a bunch of numbers in it
    if number % 2 == 0: #checks if numbers are even
        answer.append(number) #and if they are, appends them to answer
print sum(answer) #adds 'em all together and bam! correct answer
