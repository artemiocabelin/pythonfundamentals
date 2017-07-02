word_list = ['hello','world','my','name','is','Anna']
char = 'o'

def findCharacter(wordList,char):
    
    newList = []
    i = 0
    length = len(wordList)
    while i < length:
        for letter in wordList[i]:
            if letter == char:
                newList.append(wordList[i])
        i+=1
    
    print newList


findCharacter(word_list,char)