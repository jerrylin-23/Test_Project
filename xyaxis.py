def problem():

    #Analysis Problem wants XY axis

    X_axis = int(input())
    Y_axis = int(input())

    if (X_axis > 0 and Y_axis > 0):
        return 1
    elif (X_axis < 0 and Y_axis > 0):
        return 2
    elif (X_axis < 0 and Y_axis < 0):
        return 3
    elif (X_axis > 0 and Y_axis < 0):
        return 4

print(problem())
