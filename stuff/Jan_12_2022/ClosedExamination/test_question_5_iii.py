import unittest
from question_5 import Encoding

class TestQuestion5iii(unittest.TestCase):

    def testEncodeValidMessage(self):
        """ Test that a valid plain text is encoded correctly by the method
        encodeText.
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertEqual('11100', encoder.encodeText('BAD'))
        self.assertEqual('0100', encoder.encodeText('DAD'))
        self.assertEqual('111011100', encoder.encodeText('BABAD'))
        
        tree = ['', 
                '', '',
                'D', 'Y','A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertEqual('111000', encoder.encodeText('BAD'))
        self.assertEqual('001000', encoder.encodeText('DAD'))
        self.assertEqual('0010000001', encoder.encodeText('DADDY'))
        
        
    def testErrorInvalidMessage(self):
        """ Test that a ValueError is raised when a symbol/letter in the message 
        to be encoded is not a symbol/letter from the encoding tree.
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertRaises(ValueError, encoder.encodeText,'DADS') # S not in tree.
        


if __name__ == '__main__':
    unittest.main()
