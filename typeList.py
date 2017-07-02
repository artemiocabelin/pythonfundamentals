def typeList(newList):
    # Test data type of each index in loop
    strCount = 0
    intCount = 0
    for item in newList:
        if isinstance(item,str):
            strCount += 1
        elif isinstance(item,int) or isinstance(item,float):
            intCount += 1
    
    # checks if mixed, all str, or all int
    strList = "String: "
    intList = 0
    if strCount > 0 and intCount > 0:
        # if mixed list it strings together all strings and adds up all ints
        for item in newList:
            if isinstance(item,str):
                strList += item + " "
            elif isinstance(item,int) or isinstance(item,float):
                intList += item
        print "The array you entered is of mixed type."
        print strList
        print "Sum: ",intList
    
    elif strCount > 0 and intCount == 0:
        # if all strings it strings the whole list
        for item in newList:
            strList += item + " "
        print "The array you entered is of string type"
        print strList

    elif strCount == 0 and intCount > 0:
        # if all ints it adds all ints.
        for item in newList:
            intList += item
        print "The array you entered is of integer type"
        print "Sum: ",intList


# example
l = ['magical','unicorns']
typeList(l)