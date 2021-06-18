import unittest
import PyList

class TestPyList(unittest.TestCase):
    '''
    class to test PyList module
    '''

    def test_gettr(self):
        mylist = PyList.PyList(['a','b','c'])
        result = mylist[1]
        self.assertEqual(result,'b')

if __name__ == '__main__':
    unittest.main()