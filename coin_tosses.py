import random

def coin_tosses():
    head = 0
    tails = 0
    result = ""
    for num in range(1,5001):
        toss = random.randint(1,2)
        if toss == 1:
            head+= 1
            result = "head"
        else:
            tails += 1
            result = "tails"

        if num == 5000:
            print "Attempt # 5000 : Throwing a coin... It's a ",result,"! ... Got",head,"head(s) so far and",tails,"tail(s) so far"
            print "Ending the program, thank you!"
            return
        
        print "Attempt #",num,": Throwing a coin... It's a ",result,"! ... Got",head,"head(s) so far and ",tails," tail(s) so far"


coin_tosses()