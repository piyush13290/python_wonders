import unittest
from PyList import PyList # I should name the file and class better next time. 

class TestPyList(unittest.TestCase):
    '''
    class to test PyList module
    '''

    def test_gettr(self):
        '''
        simple test to see if getter system is working as expected 
        '''
        mylist1 = PyList(['a','b','c'])
        self.assertEqual(mylist1[1],'b')
        # to check if it raises an Indexerror while out of range
        self.assertRaises(IndexError, PyList.__getitem__, mylist1, 4)

    def test_create_PyList(self):
        '''
        To check if the PyList is correctly created upon initialization 
        '''

        mylist = PyList([1,2,3,4,5,6,7,8], size = 3)

        self.assertEqual(mylist.numItems, 8)


if __name__ == '__main__':
    unittest.main()
