import unittest
from question_5 import Encoding

class TestQuestion5i(unittest.TestCase):

    def testConstructor(self):
        """ Test that the object constructed has been assigned the correct 
        values for each attributes when values are provided in the parameters.
        It also checks that a copy of the parameter is assigned to the attribute
        and not the parameter itself.
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertListEqual(tree, encoder._encoding)
        self.assertIsNot(tree, encoder._encoding, 'It should be a copy of the parameter!')


if __name__ == '__main__':
    unittest.main()
