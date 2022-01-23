import unittest
from question_2 import collide

class TestQuestion2(unittest.TestCase):

    def testEmptySet(self):
        """ Test that a shape does not collide with an empty shape (represented)
        by an empty set.
        """
        shape1 = {(0,0,0,1)}
        shape2 = set()
        self.assertFalse(collide(shape2, shape1))
        self.assertFalse(collide(shape1, shape2))
        self.assertFalse(collide(set(), set()))
        

    def testNotColliding(self):
        """ Test that the function returns False when two shapes do not intersect.
        """
        shape1 = {(2, 2, 2, 3)}
        shape2 = {(7, 1, 2, 2)}
        self.assertFalse(collide(shape2, shape1))
        self.assertFalse(collide(shape1, shape2))
 
        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5)}
        shape2 = {(5, 1, 2, 2), (5, 2, 2, 2)}
        self.assertFalse(collide(shape2, shape1))
        self.assertFalse(collide(shape1, shape2))
        
 
    def testCollides(self):
        """ Test that the function returns True when two shapes do intersect. 
        It includes the case of a shape colliding with itself.
        """
        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5), (2, 2, 2, 3)}
        self.assertTrue(collide(shape1, shape1)) # an shape collide with itself
 
        shape1 = {(2, 2, 2, 3)}
        shape2 = {(5, 2, 2, 2)}
        self.assertTrue(collide(shape2, shape1))
        self.assertTrue(collide(shape1, shape2))
 
        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5), (2, 2, 2, 3)}
        shape2 = {(7, 1, 2, 2), (5, 2, 2, 2)}
        self.assertTrue(collide(shape2, shape1))
        self.assertTrue(collide(shape1, shape2))

        
    def testInvalidSphereFormat(self):
        """ Test that the function raises a ValueError when the format of the
        sphere is invalid, that is does not contains exactly 4 floats.
        """

        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5)}
        shape2 = {(7, 1, 2, 2), (5, 2, 2)}
        self.assertRaises(ValueError, collide, shape2, shape1)

        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5)}
        shape2 = {(7, 1, 2, 2), (5, 2, 2, 3, 7)}
        self.assertRaises(ValueError, collide, shape2, shape1)
        

    def testInvalidRadius(self):
        """ Test that the function raises a ValueError when one of the
        sphere has an invalid radius, that is a radius a negative radius or a
        radius of zero.
        """
        shape1 = {(0,0,0,2), (0, 1.5, 0, 1), (0, -1, 0, 1.5)}
        shape2 = {(7, 1, 2, 2), (5, 2, 2, -5)}
        self.assertRaises(ValueError, collide, shape2, shape1)

        shape1 = {(1,1,1,2), (1, 1.5, 1, 1), (2, -1, 2, 1.5)}
        shape2 = {(7, 1, 2, 2), (5, 2, 2, 0)}
        self.assertRaises(ValueError, collide, shape2, shape1)

       
if __name__ == '__main__':
    unittest.main()

