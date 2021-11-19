from pathlib import Path
import random


""""
Kriterien:
- Diagonale Wörter
- Ähnliche Anfänge
- Rückwärts Wörter
"""

def read_input(filename='worte0.txt'):
    """ Beispieldatei einlesen
    Die Zeilen in Integer und List umwandeln und Zeilenumbrüche mit .strip() entfernen.
    Default ist das Aufgabenbeispiel parkplatz0.txt.
    """
    file = Path('beispieldaten', filename)
    with open(file, 'r') as file_in:
        dimensions = [int(num) for num in file_in.readline().strip().split()]
        word_count = file_in.readline().strip()
        word_list = [line.strip() for line in file_in.readlines()]

    print('dimensions', dimensions)
    print('word_count', word_count)
    print('word_list', word_list)

    return dimensions, word_list, word_count


def make_matrix(dimensions):

    matrix = [None] * dimensions[0]
    for idx in range(0, len(matrix)):
        matrix[idx] = [None] * dimensions[1]

    return matrix


def create_easy(word_list, matrix):
    # matrix[idx] für diagonal



    for word in word_list:
        start_row, start_column = find_word_space(word, matrix)
        write_word(start_row, start_column, word)
        for row in matrix:
            print(row)

def find_word_space(word, matrix):
    max_offset = len(matrix[0]) - len(word) - 1
    start_column = random.randint(0, max_offset)
    for idx, row in enumerate(matrix):
        if matrix[idx][start_column] == None:
            fail = False
            for column in range(start_column, len(matrix[0]) - start_column):
                if matrix[idx][column] == None:
                    continue
                else:
                    fail = True
            if not fail:
                return idx, start_column

def write_word(start_row, start_column, word):
    for idx, letter in enumerate(word):
        matrix[start_row][start_column] = letter
        start_column += 1

'''
    for idx in range(0, len(word_list)):

        word_list_0 = list(word_list[idx])
        element = matrix[0]
        z = len(element) - len(word_list_0)
        x = random.randint(1, len(matrix))
        y = random.randint(0, z)

        for idx in range(0, len(word_list_0)):

            element_1 = matrix[x-1]


            for idx in range(0, len(word_list_0) - 1):
                    if element_1[idx+y] == None:
                        pass
                    else:
                        print("a")
                        break
            for idx in range(0, len(element_1)-1):
                element_1[idx + y] = word_list_0[idx]
'''




def print_matrix(matrix):
    print("Matrix: ")
    for element in matrix:
        print(element)

if __name__ == '__main__':
    dimensions, word_list, word_count = read_input()
    matrix = make_matrix(dimensions)
    create_easy(word_list, matrix)
    print_matrix(matrix)
