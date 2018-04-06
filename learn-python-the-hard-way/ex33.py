def f(j,numbers):
    i = 0
    while ( i < j ) :
        print "At the top i is %d" %i
        numbers.append(i)
        i = i + 1
        print"Numbers now: ",numbers
        print"At the bottom i is %d" %i
   

numbers = []

j = input("> ")

f(j,numbers)

print "The numbers : "

for num in numbers :
    print num
