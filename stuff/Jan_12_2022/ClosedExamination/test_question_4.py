import unittest
from question_4 import readAdjacency
from invalidfileformatexception import InvalidFileFormatException

class TestQuestion4(unittest.TestCase):

    def testValidMatrix(self):
        """ Test that the function returns the correct adjacency matrix when
        a valid file is provided.
        """
        matrix = [[0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [1, 1, 0, 1],
                  [0, 1, 0, 1]]
        self.assertEqual(matrix, readAdjacency('./data/validmatrix.csv'))

        matrix = [[1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1]]
        self.assertEqual(matrix, readAdjacency('./data/validmatrix2.csv'))


    def testMissingFile(self):
        """ Test that a FileNotFoundError is raised when the file does not 
        exist.
        """
        self.assertRaises(FileNotFoundError,  
                          readAdjacency, 
                          './data/missingfile.csv')


    def testBlankSpace(self):
        """ Test that an InvalidFileFormatException is raised when there is 
        a blank space
        instead of a value.
        """
        self.assertRaises(InvalidFileFormatException,  
                          readAdjacency, 
                          './data/blankspace.csv')


    def testInvalidValue(self):
        """ Test that an InvalidFileFormatException is raised when a value
        is other than a a 0 or a 1.
        """
        self.assertRaises(InvalidFileFormatException,  
                          readAdjacency, 
                          './data/invalidvalue.csv')


    def testTooManyRows(self):
        """ Test that an InvalidFileFormatException is raised when the file
        contains too many rows, or in other words to few columns.
        """
        self.assertRaises(InvalidFileFormatException,  
                          readAdjacency, 
                          './data/toomanyrows.csv')


    def testTooFewRows(self):
        """ Test that an InvalidFileFormatException is raised when the file
        contains too few rows, or in other words to many columns.
        """
        self.assertRaises(InvalidFileFormatException,  
                          readAdjacency, 
                          './data/toofewrows.csv')


    def testMissingValue(self):
        """ Test that an InvalidFileFormatException is raised when the file
        has rows containing a different number of elements in them.
        """
        self.assertRaises(InvalidFileFormatException,  
                          readAdjacency, 
                          './data/missingvalue.csv')


if __name__ == '__main__':
    unittest.main()

