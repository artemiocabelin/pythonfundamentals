def filterType(val):
    if isinstance(val,int):
        # Integer check
        if val >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    
    elif isinstance(val,str):
        # String check
        if len(val) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."

    elif isinstance(val,list):
        # List check
        if len(val) > 10:
            print "Big list!"
        else:
            print "Short list."

# Example
filterType(['al;sdkf',1,2,4,5])