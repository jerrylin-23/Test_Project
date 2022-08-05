


#print(problem())

def problemALT():
    word = input()
    word = word.replace("H","")
    word = word.replace("O","")
    word = word.replace("I","")
    word = word.replace("Z","")
    word = word.replace("X","")
    word = word.replace("N","")

    if (len(word) == 0):
        return "YES"

    return "NO"

print(problemALT())
