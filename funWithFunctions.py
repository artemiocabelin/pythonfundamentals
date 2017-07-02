def odd_even():
    for num in range(1,2001):
        if num % 2 != 0:
            print "Number is ",num,". This is an odd number."
        else:
            print "Number is ",num,". This is an even number."
        
def multiply(someList,val):
    for num in range(len(someList)):
        someList[num] *= val
    print someList
    return someList

# odd_even()
x = multiply([2,4,5],3)

def layered_multiple(a): 
    newArr = []
    for num in a:
        newIndex = []
        for i in range(1,num+1):
            newIndex.append(1)
        newArr.append(newIndex)
    print newArr

layered_multiple(x)