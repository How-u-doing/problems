############# DO NOT DELETE THESE LINES OF CODE ######################

KEYPAD = {'0': '', '1': '', '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
          '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}

##################   WRITE YOUR CODE HERE  ###########################
import copy


def t9Words(keyPressed: str) -> set:
    """Gets all possible combinations of given keys pressed.

    Args:
        keyPressed: A string of digits, 0-9, e.g. 1397.

    Returns:
        A set containing all possible combinations of letters given the
        set of keys pressed on the phone keypad.

    Examples:
        t9Words('23')
        -> {'AD','AE','AF','BD','BE','BF','CD','CE','CF'}
        t9Words('123')  # Pressing '1' has no effect
        -> {'AD','AE','AF','BD','BE','BF','CD','CE','CF'}
    """

    # The idea is very simple, iterate the keyPressed string, skip
    # empty ones (key 0 and 1) or map them to null string ''. We
    # will get a list of mapped values/strings on certain keys (2-9).
    # Then making all the combinations gives the result, during which
    # we can employ a recursive approach.

    # get a list of strings mapped by 2-9 (excluding 0 and 1)
    strings = []
    for digit in keyPressed:
        if digit == '0' or digit == '1':
            continue
        strings.append(KEYPAD[digit])

    N = len(strings)
    if N == 0:
        return {''}
    # Columns of strings:
    # =======================================
    #  P          A           W          D
    #  Q          B           X          E
    #  R          C           Y          F
    #  S                      Z
    # =======================================
    # Now we draw some directed edges (L2R) connecting these nodes (digraph)
    # This is where we can take advantage of recursion

    combinations = set()  # note that the order matters
    i = 0
    recursively_combine(combinations, strings, i, N)
    return combinations


def recursively_combine(comb: set, strings: list, i: int, N: int):
    """Recursively adds all the combinations in list[i,N) to comb
    Args:
        comb: set of strings to be added
        strings: the list of strings
        i: the current index
        N: size of the list
    """
    if i < N:
        if len(comb) == 0:  # i == 0
            assert i == 0
            for c in strings[i]:
                comb.add(c)
        else:
            # append each letter of strings[i] to the comb set
            old_comb = copy.deepcopy(comb)
            for letter in strings[i]:
                for item in old_comb:
                    # sorta miss C++'s inplace update :)
                    if item in comb:
                        comb.remove(item)
                    comb.add(item + letter)
        recursively_combine(comb, strings, i + 1, N)


if __name__ == '__main__':
    keyPressed = '702913'  # effectively '7293', 4*3*4*3 = 144 combinations
    # keyPressed = '123'
    comb = t9Words(keyPressed)
    print(comb)
