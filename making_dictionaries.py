name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar","papoy"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1,arr2):
    new_dict ={}
    for item1, item2 in zip(arr1,arr2):
        new_dict[item1] = item2
    print new_dict

# Hacker challenge
def make_dict_hack(arr1,arr2):
    new_dict ={}
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            i = 0
            while i < len(arr1):
                new_dict[arr1[i]] = ''
                i+=1
            j=0
            while j < len(arr2):
                new_dict[arr1[j]] = arr2[j]
                j+=1
            print new_dict
        elif len(arr1) < len(arr2):
            i = 0
            while i < len(arr2):
                new_dict[arr2[i]] = ''
                i+=1
            j=0
            while j < len(arr1):
                new_dict[arr2[j]] = arr1[j]
                j+=1
            print new_dict
    else:
        for item1, item2 in zip(arr1,arr2):
            new_dict[item1] = item2
        print new_dict


# make_dict(name,favorite_animal)
make_dict_hack(name,favorite_animal)
