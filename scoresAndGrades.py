import random

def scores_and_grades():
    for num in range(10):
        a = random.randint(60,100)
        if a >= 60 and a <=69:
            print "Score:",a,"; Your grade is D"
        elif a >= 70 and a <=79:
            print "Score:",a,"; Your grade is C"
        elif a >= 80 and a <=89:
            print "Score:",a,"; Your grade is B"
        elif a >= 90 and a <=100:        
            print "Score:",a,"; Your grade is A"

scores_and_grades()