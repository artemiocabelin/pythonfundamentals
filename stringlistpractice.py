# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')
print words.replace('day','month',1)


# Min and Max
a = [2,54,-2,7,12,98]
print min(a)
print max(a)


#First and Last
b = ["hello",2,54,-2,7,12,98,"world"]
first = b[0]
last = b[len(b)-1]
newList = [first,last]
print first
print last
print newList

# New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
arr1 = x[0:len(x)/2]
arr2 = x[(len(x)/2)-1:len(x)-1]
print arr1
print arr2
arr2[0] = arr1
print arr2