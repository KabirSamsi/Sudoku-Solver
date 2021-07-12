#Import functions and libraries
from evaluate_functions import check_solved, legal_vertical, legal_horizontal, legal_square, check_unique_vertical, check_unique_horizontal, check_unique_square
from represent_functions import string_represent
import numpy as np
import time

def sudoku_file(filename): #Open sudoku csv file and represent as matrix grid
    with open(filename) as file:
        grid = []
        for row in file:
            grid.append([]) #Add new row to end of grid
            row_representation = row.rstrip().split(',') #Represent row as array of chars
            for cell in row_representation:
                grid[-1].append([]) #Add new column to end of row
                if cell == ' ' or cell == '': #If empty row, add all numbers as possibilities
                    grid[-1][-1] = list(np.arange(1, 10))
                else: #If row has value, it is solved. Add only that value
                    grid[-1][-1] = [int(cell)]
    return grid #Return formatted grid

grid = sudoku_file("Sudokus/sudoku3.txt")
#Print out initial grid
print(f'INITIAL SUDOKU ({round(check_solved(grid)*100, 2)}% Solved)')
for x in range(len(grid)):
    row = grid[x]
    print(string_represent(row))
    if (x+1)%3 == 0:
        print ("--" * 11)
print('')

while not check_solved(grid) == 1: #Continue replacing elements until grid is completely solved
    solved = check_solved(grid)
    time.sleep(0.5) #Visual latency creator
    print(f"\nPercent Solved: {round(check_solved(grid)*100, 2)}%")

    for x in range(len(grid)):
        row = grid[x]
        print(string_represent(row))
        if (x+1)%3 == 0:
            print ("--" * 11)

    for x in range(len(grid)): #Iterate through all cells of grid
        for y in range(len(grid[x])):
            cell = grid[x][y]
            for element in cell:
                if len(cell) > 1: #Do not evaluate for elements that have already been solved, they cannot be replaced
                    if legal_vertical(element, grid, y) and legal_horizontal(element, grid, x) and legal_square(element, grid, [x, y]): #Check for legality of value
                        pass
                    else: #If value is illegal, remove it
                        cell.remove(element)
                        
                    #Check if element is unique, meaning it must be in correct position
                    if check_unique_vertical(element, grid, y) or check_unique_horizontal(element, grid, x) or check_unique_square(element, grid, [x, y]):
                        for item in cell:
                            if item != element:
                                cell.remove(item)

    if check_solved(grid) == solved:
        print("\nPuzzle is too complex for algorithm")
        break
                
#Print out solved grid
if check_solved(grid) == 1:
    print('\nSOLVED SUDOKU')
    for x in range(len(grid)):
        row = grid[x]
        print(string_represent(row))
        if (x+1)%3 == 0:
            print ("--" * 11)