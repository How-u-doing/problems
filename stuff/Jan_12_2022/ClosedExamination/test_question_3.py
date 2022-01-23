import unittest
from question_3 import t9Words

class TestQuestion3(unittest.TestCase):

    def testSingleDigit(self):
        """ Test that given a single digit, the function returns all the 
        letters associated to that digit. As the returned data structure
        is a set, the order does not matter.
        """
        self.assertEqual({'W', 'X', 'Y','Z'}, t9Words('9'))
        self.assertEqual({'M', 'N', 'O'}, t9Words('6'))
        
        
    def testTwoDigits(self):
        """ Test that given two digits, the function returns nxm pairs of 
        letters where n is the number of letters associated to the first digit
        and m is the number of letters associated to the second digit. As the 
        returned data structure is a set, the order does not matter.
        """
        self.assertEqual({'AD','AE','AF','BD','BE','BF','CD','CE','CF'},
                         t9Words('23'))
        self.assertEqual({'AP','AQ','AR','AS',
                          'BP','BQ','BR','BS',
                          'CP','CQ','CR','CS'},
                         t9Words('27'))
        

    def testComplexCombination(self):
        """ Test that given a combination of digits, including digits with no
        associated letter, the function returns the correct output ignoring
        digits with no associated letters.
        As the returned data structure is a set, the order does not matter.
        """
        self.assertEqual({''}, t9Words('1'))
        self.assertEqual({'D','E','F'}, t9Words('03'))
        self.assertEqual({'AD','AE','AF','BD','BE','BF','CD','CE','CF'},
                         t9Words('123'))
        self.assertEqual({'D','E','F'}, t9Words('03'))
        self.assertEqual({'TP','TQ','TR','TS',
                          'UP','UQ','UR','US',
                          'VP','VQ','VR','VS'},
                         t9Words('18070'))

              
if __name__ == '__main__':
    unittest.main()

