import unittest
from PyList import PyList # I should name the file and class better next time. 

class TestPyList(unittest.TestCase):
    '''
    class to test PyList module
    '''

    def test_makeroom(self):
        '''
        To test the PyList makeroom function is expanding the PyList
        '''
        mylist = PyList([1,2,3,4,5], size = 5)
        mylist.append(6)
        self.assertEqual(mylist.size, 7)


    def test_create_PyList(self):
        '''
        To check if the PyList is correctly created upon initialization 
        '''
        # Check 1: simple  check wto see a list is created as expected
        mylist = PyList([1,2,3])
        self.assertEqual(str(mylist), 'PyList([1, 2, 3])')

        # Check 2: To see when the longish list is created with smaller initial size 
        mylist = PyList([1,2,3,4,5,6,7,8], size = 3)
        self.assertEqual(mylist.numItems, 8)

    def test_gettr(self):
        '''
        simple test to see if getter system is working as expected 
        '''
        # Check 1 : a simple check to see index based call works as expeted
        mylist1 = PyList(['a','b','c'])
        self.assertEqual(mylist1[1],'b')

        # Check 2:  to check if it raises an Indexerror while out of range
        self.assertRaises(IndexError, PyList.__getitem__, mylist1, 4)


if __name__ == '__main__':
    unittest.main()
