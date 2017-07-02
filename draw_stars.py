def draw_stars(numList):
    for num in numList:
        if isinstance(num,int):
            star = ""
            for i in range(num):
                star += "*"
            print star
        elif isinstance(num,str):
            word = ""
            for letter in num:
                word += num[0]
            print word.lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
