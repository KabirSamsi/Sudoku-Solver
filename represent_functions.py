def string_represent(mat): #Represent row of ints/arrs as a proper string
    final = ""
    for x in range(len(mat)):
        arr = mat[x]
        if len(arr) == 1:
            final += f"{arr[0]} "
        else:
            final += "  "
        if (x+1)%3 == 0:
            final += "| "
    return final.rstrip()