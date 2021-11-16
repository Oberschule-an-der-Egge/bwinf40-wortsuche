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
    # code funktioniert wegen der funktion nich mehr 
    for idx in range(0, len(word_list)):

        word_list_0 = list(word_list[idx])
        element = matrix[0]
        z = len(element) - len(word_list_0)
        x = random.randint(1, len(matrix))
        y = random.randint(0, z)

        for idx in range(0, len(word_list_0)):

            element_1 = matrix[x-1]

            if element_1[idx+y] == None:
                element_1[idx+y] = word_list_0[idx]
            else:
                break




def print_matrix(matrix):
    print("Matrix: ")
    for element in matrix:
        print(element)

if __name__ == '__main__':
    dimensions, word_list, word_count = read_input()
    matrix = make_matrix(dimensions)
    create_easy(matrix, word_list)
    print_matrix(matrix)
