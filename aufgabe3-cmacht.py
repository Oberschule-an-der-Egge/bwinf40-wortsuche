from pathlib import Path
import random
import string


""""
Kriterien:
- Ähnliche Anfänge
- Rückwärts Wörter
"""


def read_input(filename='worte3.txt'):
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
    """ Erstelle ein neues Rechteck mit benutzerdefiniertem Schwierigkeitsgrad
    """
    difficulty = int(input("Wähle Schwierigkeitsgrad (1,2 oder 3):"))
    for idx, word in enumerate(word_list):
        if idx % 2 == 1:
            word_space_down = find_word_space_down(word, matrix)
            if word_space_down:
                write_word_down(matrix, word_space_down[0], word_space_down[1], word, difficulty)
                continue
        start_row, start_column = find_word_space_right(word, matrix)
        write_word_right(matrix, start_row, start_column, word, difficulty)
    fill_empty_spaces(matrix, difficulty, word_list)


def fill_empty_spaces(matrix, difficulty, word_list):
    """ Fülle die leeren Felder mit Buchstaben
    """
    for idx, row in enumerate(matrix):
        for col, _ in enumerate(row):
            if matrix[idx][col] is None:
                word_list_letters = ''.join(word_list)
                alphabet = string.ascii_uppercase
                if difficulty == 1:
                    filler = [letter for letter in alphabet if letter not in word_list_letters]
                elif difficulty == 3:
                    filler = word_list_letters
                else:
                    filler = alphabet
                matrix[idx][col] = random.choice(filler)
                # matrix[idx][col] = '.'
    return matrix


def find_word_space_right(word, matrix):
    """ Finde eine Zeile mit genug freiem Platz für das gegebene Wort
    """
    max_offset = len(matrix[0]) - len(word)
    random_column = random.randint(0, max_offset)
    random_rows = list(range(len(matrix)))
    random.shuffle(random_rows)
    for idx in random_rows:
        count = 0
        for column in range(random_column, len(matrix[0])):
            if matrix[idx][column] is not None:
                count = 0
            else:
                count += 1
                if count == len(word):
                    start_column = column - (len(word) - 1)
                    return idx, start_column


def find_word_space_down(word, matrix):
    """ Finde eine Spalte mit genug freiem Platz für das gegebene Wort
    """
    max_offset = len(matrix) - len(word)
    random_row = random.randint(0, max_offset)
    random_cols = list(range(len(matrix[0])))
    random.shuffle(random_cols)
    for idx in random_cols:
        count = 0
        for row in range(random_row, len(matrix)):
            if matrix[row][idx] is not None:
                count = 0
            else:
                count += 1
                if count == len(word):
                    start_row = row - (len(word) - 1)
                    return start_row, idx


def write_word_right(matrix, start_row, start_column, word, difficulty):
    """ Schreibe ein Wort in die Matrix
    """
    if difficulty == 3 and random.random() > 0.5:
        word = list(word)
        word.reverse()

    for letter in word:
        matrix[start_row][start_column] = letter
        start_column += 1


def write_word_down(matrix, start_row, start_column, word, difficulty):
    """ Schreibe ein Wort von oben nach unten in die Matrix
    """
    if difficulty == 3 and random.random() > 0.5:
        word = list(word)
        word.reverse()

    for letter in word:
        matrix[start_row][start_column] = letter
        start_row += 1


def print_matrix(matrix):
    for row in matrix:
        print(row)


def run_main():
    dimensions, word_list, word_count = read_input()
    matrix = make_matrix(dimensions)
    create_game(word_list, matrix)
    print_matrix(matrix)


if __name__ == '__main__':
    run_main()

