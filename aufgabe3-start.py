from pathlib import Path


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

    return


if __name__ == '__main__':
    read_input()
