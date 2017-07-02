list_one = [1,2,4,6,5]
list_two = [1,2,4,6,5]

# With Zip
def compareArrays(arr1,arr2):

    if len(arr1) != len(arr2):
        print "The lists are not the same"
        return

    for item1,item2 in zip(arr1,arr2):
        if item1 != item2:
            print "The lists are not the same."
            return
    print "The lists are the same"


# Without zip
def compareArraysWithoutZip(arr1,arr2):
    if len(arr1) != len(arr2):
        print "The lists are not the same"
        return

    zipArray = []
    arrLength = len(arr1)
    i = 0
    while i < arrLength:
        zipArray.append([arr1[i],arr2[i]])
        i += 1
    
    for item in zipArray:
        if item[0] != item[1]:
            print "The lists are not the same"
            return
    print "The lists are the same"
        
    
# compareArrays(list_one,list_two)
compareArraysWithoutZip(list_one,list_two)
