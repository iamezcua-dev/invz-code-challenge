# * EVOLUTION GAME
#
# - In a 6 X 6 board with cells - A cell can be either DEAD or ALIVE (use 0 or 1) - At each iteration of the game,
#   a DEAD cell can become ALIVE if there are 2 or more ALIVE cells adjacent to it (horizontally or vertically).
#
#   e.g. with 3 x 3 grid:
#       0 0 1 -> 0 1 1
#       0 1 0    1 1 1
#       1 0 0    1 1 0
#
# - ALIVE cells cannot become DEAD (i.e. once ALIVE they remain ALIVE for the duration of the game)
# * Challenge:
#   1. Create an application that starts with a 6 X 6 board with 10 alive cells (randomly distributed); [OK]
#   2. Run the game and "evolving" the board                                                            [*]
#   3. Print the board at each iteration (with a short delay)                                           [PENDING]
#   4. Stop the game                                                                                    [PENDING]

from random import randint
from typing import List
import copy


class MatrixShapeException(Exception):
    pass


def evolve_matrix(matrix: list) -> list:
    a_matrix = copy.deepcopy(matrix)

    for row_index, matrix_row in enumerate(matrix):  # traverse rows
        for column_index, element in enumerate(matrix_row):  # traverse elements (or columns)
            if matrix[row_index][column_index] == 0:
                adjacents = []
                if row_index > 0:  # not in the top row.
                    adjacents.append(matrix[row_index - 1][column_index])
                if row_index < len(matrix) - 1:  # not in the bottom row.
                    adjacents.append(matrix[row_index + 1][column_index])
                if column_index > 0:  # not in the left-most column.
                    adjacents.append(matrix[row_index][column_index - 1])
                if column_index < len(matrix_row) - 1:  # not in the right-most column.
                    adjacents.append(matrix[row_index][column_index + 1])

                alive_adjacents = [cell_value for cell_value in adjacents if cell_value == 1]

                if len(alive_adjacents) >= 2:
                    a_matrix[row_index][column_index] = 1  # Alive!
    return a_matrix


def matrix_contain_deads(matrix: list) -> bool:
    for row_index, matrix_row in enumerate(matrix):  # traverse rows
        for column_index, element in enumerate(matrix_row):  # traverse elements (or columns)
            if matrix[row_index][column_index] == 0:
                return True
    return False


def solve_matrix(matrix: list) -> list:
    solution = copy.deepcopy(matrix)
    while matrix_contain_deads(solution):
        solution = evolve_matrix(solution)
        print(solution)


def initialize_matrix(rows: int, columns: int, number_of_alive_cells=10) -> List[List]:
    empty_matrix = [
        [0 for _ in range(0, columns)]  # create 1 row of `columns` columns, initialized with zero
        for _ in range(0, rows)  # create `rows` rows
    ]  # matrix initialized using zero on each cell

    if (rows * columns) > number_of_alive_cells:
        alive_cells = set()
        while len(alive_cells) < number_of_alive_cells:
            rand_row = randint(0, rows - 1)  # create a randomly-generated number from 0 to `rows` - 1
            rand_col = randint(0, columns - 1)  # create a randomly-generated number from 0 to `columns` - 1
            if (rand_row, rand_col) not in alive_cells:
                empty_matrix[rand_row][rand_col] = 1
                alive_cells.add((rand_row, rand_col))

        return empty_matrix
    else:
        raise MatrixShapeException("Number of requested alive cells is higher than the matrix size.")
