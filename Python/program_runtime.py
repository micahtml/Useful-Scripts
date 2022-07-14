import timeit

start = timeit.default_timer()

# My code goes here
total = 0
for i in range(10):
    total += i
print("Sum:" ,total)
#--------------

stop = timeit.default_timer()

print('Time: ', stop - start)  