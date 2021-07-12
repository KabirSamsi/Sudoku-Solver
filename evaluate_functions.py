from math import floor

def check_solved(grid): #Check if every single cell has only one value (meaning it is solved)
    number_possible = 0
    for row in grid:
        for cell in row:
            number_possible += len(cell)
    return (81/number_possible)

def legal_vertical(number, grid, column): #Check if number's position is legal vertically
    for row in grid:
        if len(row[column]) == 1 and row[column][0] == number:
            return False
    return True

def legal_horizontal(number, grid, row): #Check if number's position is legal horizontally
    for cell in grid[row]:
        if len(cell) == 1 and cell[0] == number:
            return False
    return True

def legal_square(number, grid, indices): #Check if number's position is legal in a square
    start = (floor(indices[0]/3)*3, floor(indices[1]/3)*3) #Tuple stores starting coordinate based on rounding index coordinate down

    for x in range(3): #Iterate through the inner grid
        for y in range(3):
            cell = grid[start[0]+x][start[1]+y] #Stores the position within the grid
            if len(cell) == 1 and cell[0] == number:
                return False
    return True

def check_unique_vertical(number, grid, column): #Checks if a given element is unique in its column
    for row in grid:
        if number in row[column]:
            return False
    return True

def check_unique_horizontal(number, grid, row): #Checks if a given element is unique in its row
    for cell in grid[row]:
        if number in cell:
            return False
    return True

def check_unique_square(number, grid, indices): #Checks if a given element is unique in its inner square
    start = (floor(indices[0]/3)*3, floor(indices[1]/3)*3)
    for x in range(3):
        for y in range(3):
            cell = grid[start[0]+x][start[1]+y]
            if number in cell:
                return False
    return True
