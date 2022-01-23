import unittest
from question_5 import Encoding

class TestQuestion5ii(unittest.TestCase):

    def testDecodeValidMessage(self):
        """ Test that a correctly encoded message can be decoded by the method
        decodeText.
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertEqual('BAD', encoder.decodeText('11100'))
        self.assertEqual('DAD', encoder.decodeText('0100'))
        

    def testMissingBitError(self):
        """ Test that a ValueError is raised when the message is corrupted, that 
        is some bits are misssing, and the decoding process does not stop on a 
        leaf of the decoding tree. 
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertRaises(ValueError, encoder.decodeText, '111')
        self.assertRaises(ValueError, encoder.decodeText, '00101')
        

    def testInvalidBitError(self):
        """ Test that a ValueError is raised when one of the bit in the stream 
        is incorrect, that is is not a 0 or a 1.
        """
        tree = ['', 
                'D', '',
                None, None,'A', 'B', 
                None, None, None, None, None, None, None, None]
        encoder = Encoding(tree)
        self.assertRaises(ValueError, encoder.decodeText, '0112')
        self.assertRaises(ValueError, encoder.decodeText, '2011')



if __name__ == '__main__':
    unittest.main()
