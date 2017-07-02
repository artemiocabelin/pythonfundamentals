# Multiples 1
for i in range(1,1001):
    print i


# Multiples 2
for i in range(5,1000001):
    if ( i % 5 ) == 0:
        print i

# Sum List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

# Average List
print sum / len(a)