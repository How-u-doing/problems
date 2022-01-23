import math
import unittest
from question_1 import centreOfMass

class TestQuestion1(unittest.TestCase):
    
    ###########################################################################
    # This is a convenience function to asser that two tuples of float are equal
    # This is not a test from the test series, it is a function used within the 
    # tests.
    def assertTupleAlmostEqual(self, tuple1, tuple2):
        """A tuple-of-float-specific equality assertion. Needed as the == 
        operator on float does not always return the expected result due to
        the internal representation of float in Python.
        The function uses math.isclose() instead of == to compare two floats.

        Args:
            tuple1: The first tuple to compare.
            tuple2: The second tuple to compare.
        """
        if (not (isinstance(tuple1, tuple) and isinstance(tuple2, tuple)) 
            and len(tuple1) != len(tuple2)):
            self.fail(str(tuple1) + '!=' + str(tuple2))
            
        for i in range(len(tuple1)):
            if (isinstance(tuple1[i], float) 
                and not math.isclose(tuple1[i], tuple2[i], rel_tol=0.000000001)):
                self.fail(' tuples differ: ' + str(tuple1) + '!=' + str(tuple2) 
                          + '\nFirst differing element ' + str(i) + ':\n'
                          + str(tuple1[i]) + '\n'
                          + str(tuple2[i]) + '\n'
                          )
                
                            
    ############### The tests series start here ############################
        
    def testSameUnitOfMass(self):
        """Test that the correct answer is returned for the cases, where the
        spheres have different radius but the same unit mass. 
        """
        self.assertTupleAlmostEqual((0.0,0.0,0.0), 
                                    centreOfMass({(-4, 1, 0, 1, 1),
                                                  (-4, -1, 0, 1, 1),
                                                  (1, 0, 0, 2, 1)}))
        
        self.assertTupleAlmostEqual((-7.0/36,-7.0/36,0.0), 
                                    centreOfMass({(-2, 1, 0, 1, 1),
                                                  (-4, -1, 0, 2, 1),
                                                  (1, 0, 0, 3, 1)}))
        
    def testDifferentUnitOfMass(self):
        """Test that the correct answer is returned for the general cases, that
        is spheres with different radius and different unit mass.
        """
        self.assertTupleAlmostEqual((0.0,0.0,0.0), 
                                    centreOfMass({(-1, 1, 0, 1, 1), 
                                                  (-1, -1, 0, 1, 1),
                                                  (1, 0, 0, 1, 2)}))
        
        self.assertTupleAlmostEqual((78.0/75,32.0/75,40.0/75), 
                                    centreOfMass({(0, 0, 1, 2, 2), 
                                                  (2, 0, 0, 3, 1),
                                                  (0, 1, 0, 2, 1),
                                                  (1, 1, 1, 2, 3)}))
        
    def testEmptySet(self):
        """ Test that a ValueError is raised when one of the set of spheres is
        empty.
        """
        self.assertRaises(ValueError, centreOfMass, set())
        

    def testNegativeRadius(self):
        """Test that a ValueError is raised when one of the sphere as an negative 
        radius.
        """
        self.assertRaises(ValueError, 
                          centreOfMass,
                          {(2, 1, 3, 1, 1), (1, 1, 4, 1, 4), (1, 1, 1, -3, 2)})

    def testNegativeMass(self):
        """Test that a ValueError is raised when one of the sphere as an negative 
        unit mass.
        """
        self.assertRaises(ValueError, 
                          centreOfMass,
                          {(2, 1, 3, 1, -1), (1, 1, 1, 1, 2)})

    def testZeroRadius(self):
        """Test that a ValueError is raised when one of the sphere as a radius
        of zero.
        """
        self.assertRaises(ValueError, 
                          centreOfMass,
                          {(2, 1, 3, 1, 1), (1, 1, 4, 1, 2), (1, 1, 1, 0, 2)})

    def testZeroMass(self):
        """Test that a ValueError is raised when one of the sphere as a unit 
        mass of zero.
        """
        self.assertRaises(ValueError, 
                          centreOfMass,
                          {(2, 1, 3, 1, 1), (1, 1, 4, 1, 0)})


if __name__ == '__main__':
    unittest.main()

