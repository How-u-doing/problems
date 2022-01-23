############# DO NOT DELETE THIS LINE OF CODE ######################
from invalidfileformatexception import InvalidFileFormatException

##################  WRITE YOUR CODE HERE ###########################
import csv


def readAdjacency(filename: str):
    """Reads a csv file containing an adjacent matrix.

    Args:
        filename: The file name containing an adjacent matrix.

    Returns:
        A 2D list representation of the adjacent matrix read from the file.

    Raises:
        FileNotFoundError: Occurred when the file path given by the parameter
            ``filename`` does not exist.
        InvalidFileFormatException: Occurred when
            - the file contains values other than 0s and 1s,
            - the number of columns and lines are not the same (the matrix is not square)
    """

    file = open(filename)
    csvreader = csv.reader(file)
    rows = []
    try:
        for row in csvreader:
            row = [int(c) for c in row]  # int(c) may throw ValueError
            rows.append(row)
    except ValueError:
        raise InvalidFileFormatException("Invalid data: non-digits")
    # print(rows)  # to debug
    file.close()

    for row in rows:
        if len(row) != len(rows):
            raise InvalidFileFormatException("The matrix is NOT square")
        for x in row:
            if x != 0 and x != 1:
                raise InvalidFileFormatException("Invalid data: digit 2-9)")
    return rows


if __name__ == '__main__':
    try:
        matrix = [[0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [1, 1, 0, 1],
                  [0, 1, 0, 1]]
        m = readAdjacency('./data/validmatrix.csv')
        succ = m == matrix
        print("matrix=")
        print(matrix)
        print("matrix read = ")
        print(m)
        print("m == matrix: " + str(succ))
    except FileNotFoundError as fnf:
        print(fnf)
    except InvalidFileFormatException:
        print("Invalid file format")
