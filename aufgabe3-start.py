from pathlib import Path
import random
import string


""""
Kriterien:
- Ähnliche Anfänge
- Rückwärts Wörter
"""

def read_input(filename='worte5.txt'):
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


def create_game(word_list, matrix):


    difficulty = int(input("Schwierigkeit (1,2,3):"))
    for word in word_list:
        start_row, start_column = find_word_space(word, matrix)
        write_word(start_row, start_column, word, difficulty)
    fill_empty_spaces(matrix, difficulty, word_list)



def fill_empty_spaces(matrix, difficulty, word_list):
    i = 0
    total_spaces = (dimensions[0]) * (dimensions[1])
    for idx, row in enumerate(matrix):
        for coloum in range(len(matrix[0])):
            if matrix[idx][coloum] == None and i < total_spaces:
                if difficulty == 1:
                    matrix[idx][coloum] = random.choice(list(string.ascii_uppercase))
                else:
                    matrix[idx][coloum] = random.choice(list(word_list[0]))
            elif i == total_spaces:
                return matrix
            else:
                continue
            i += 1
    return matrix



def find_word_space(word, matrix):
    max_offset = len(matrix[0]) +1 - len(word) - 1
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

def write_word(start_row, start_column, word, difficulty):

    if difficulty == 3:
        word = list(word)
        word.reverse()
        for idx, letter in enumerate(word):
            matrix[start_row][start_column] = letter
            start_column += 1
    else:
        for idx, letter in enumerate(word):
            matrix[start_row][start_column] = letter
            start_column += 1




def print_matrix(matrix):
    print("Matrix: ")
    for element in matrix:
        print(element)

if __name__ == '__main__':
    dimensions, word_list, word_count = read_input()
    matrix = make_matrix(dimensions)
    create_game(word_list, matrix)
    print_matrix(matrix)

