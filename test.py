def problemALT ():

    games = []

    games.append(input())
    games.append(input())
    games.append(input())
    games.append(input())
    games.append(input())
    games.append(input())

    w = 0
    l = 0

    for i in range(0, len(games), 1):

        if (games[i] == "W"):
            w = w + 1
        else:
            l = l + 1

    if (w == 6 or w == 5):
        return 1
    elif (w == 4 or w == 3):
        return 2
    elif (w == 2 or w == 1):
        return 3
    else:
        return -1

print(problemALT())
