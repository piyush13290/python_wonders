import unittest
from PyList import PyList # I should name the file and class better next time. 

class TestPyList(unittest.TestCase):
    '''
    class to test PyList module
    '''

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

    def test_makeroom(self):
        '''
        To test the PyList makeroom function is expanding the PyList
        '''
        # Check 1: PyList should call __makeroom while appending the 6th item
        mylist = PyList([1,2,3,4,5], size = 5)
        mylist.append(6)
        self.assertEqual(mylist.size, 7)

    def test_append(self):
        '''
        To test append method of the class
        ''' 
        mylist = PyList([1,2,3,4])
        # Check 1: Appending expands the PyList 
        mylist.append(5)
        self.assertEqual(str(mylist), 'PyList([1, 2, 3, 4, 5])')

        # Check 2: Appends updates the numItems correctly
        self.assertEqual(mylist.numItems, 5)

        # Check 2: Appends uses __makeroom correcrtly when needed
        mylist = PyList([1,2,3,4], size=4)
        self.assertEqual(mylist.size, 4)
        mylist.append(5)
        self.assertEqual(mylist.size,6)

    def test_insert(self):
        '''
        To test that the insert method works well
        '''
        # Check 1: While inserting in the middle of the list
        mylist = PyList([1,2,3,4,5])
        mylist.insert(2,6)
        self.assertEqual(mylist[2],6)

        # Check 2: while inserting at the end of the list 
        mylist.insert(10,7)
        self.assertEqual(mylist[6],7)

    def test_add(self):
        '''
        to test that two PyList can be added 
        '''
        mylist1 = PyList([1,2,3])
        mylist2 = PyList([4,5,6])
        mylist3 = mylist1 + mylist2

        # Check 1: mylist3 is an PyList object
        self.assertEqual(type(mylist3), type(mylist1))

        # Check 2: mylist3 has 6 elements
        self.assertEqual(mylist3.numItems, 6)

        # Check 3: mylist3's appends second list to the first 
        self.assertEqual(mylist3[0],1)
        self.assertEqual(mylist3[2],3)
        self.assertEqual(mylist3[3],4)
        self.assertEqual(mylist3[5],6)

    def test_delete(self):
        '''
        To test the deletitem method of PyList
        '''

        #  Check 1: deleting an item is no longer in the PyList
        mylist = PyList([1,2,3,4,5,6])
        del mylist[3]
        self.assertFalse(4 in mylist)

        # Check 2: The numItems in the list is updated
        self.assertEqual(mylist.numItems, 5)

        # Check 3: The last item is converted into None,
        self.assertRaises(IndexError, PyList.__getitem__, mylist, 5)


if __name__ == '__main__':
    unittest.main()
