def half_represent(mat):
    final = ""
    for arr in mat:
        final += f'{arr} '
        final += " " * (9-len(arr))
    return final.rstrip()

def string_represent(mat):
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