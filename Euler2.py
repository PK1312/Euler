"""By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""
x = int(raw_input("What position in the sequence? "))
def fib(x):
    result = 0
    if x == 1:
        result = 1
    elif x == 0:
        result = 0
    else:
        result = fib(x-1) + fib(x-2) #Okay, just for me: this is a recursive function. Basically, what's happening here is a recursive function. It's calling itself. If you were to call, say, fib(10), it would fall through the if/elif/else chain, then
		#call fib(9) + fib(8)- then, since it can't do either of those, it calls fib(8) + fib(7) and so forth until it gets to fib(1)- which it CAN do, then work back up form there to fib(10)
    return result

print fib(x)