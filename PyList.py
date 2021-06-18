
class PyList:
    '''
    A class which works like Python's list class, sequential list  
    '''
    def __init__(self, contents = [], size = 10):
        '''
        Contents = to initialize the PyList class with some existing contents
        Size = the size of the PyList to initialize the object, no need to worry if it is not known in advance, 
        it will adjust dynamically as we add more elements 
        '''
        self.items = [None] * size 
        self.numItems = 0
        self.size = size

        # now add elements if provided at the time of initialization
        for e in contents:
            self.append(e) # this method is developed below 

    def __makeroom(self):
        '''
        hidden method to resize the list when called upon
        let's expand the list size by 20% each time this method is called
        '''

        newlen = int(self.size * 1.50) 
        newlist = [None] * newlen

        for i in range(self.numItems):
            newlist[i] = self.items[i]

        self.items = newlist
        self.size = newlen

    def append(self, item):
        '''
        A function to append items in our PyList
        '''

        if self.numItems == self.size:
            self.__makeroom()

        self.items[self.numItems] = item
        self.numItems += 1
    
    def insert(self, i, newitem):
        '''
        To insert an item in the list
        i = the index to insert the new  item
        newitem = the item which needs to be inserted
        '''

        #check 1: if the size of the PyList needs to be expanded

        if self.numItems == self.size:
            self.__makeroom()

        # check 2: if the new insert would require shifting of old items

        if i < self.numItems:
            for j in range(self.numItems-1, i-1, -1):
                self.items[j+1] =  self.items[j]

            self.items[i] == newitem
            self.numItems  += 1
        else:
            self.append(newitem)

    def __getitem__(self, index):
        '''
        getter method
        '''

        if index >=0 and index < self.numItems:
            return self.items[index]

        raise IndexError("Index is out of range for PyList")

    def __add__(self,other):
        '''
        to add another PyList with this 
        Input:
            other = PyList object
        Output
            result = PyList object adding the existing list with the other list 
        '''
        if type(self) != type(other):
            raise TypeError("the object does not seems to be of PyList type, it is {} type".format(type(other)))
            print("this is still running")

        newsize = int((self.numItems + other.numItems)*1.5)
        result = PyList(size = newsize) # to make sure new PyList if of adequet size

        for i in range(self.numItems):
            result.append(i)

        for i in range(other.numItems):
            result.append(i)

        return result

    
    def __delitem__(self, index):
        '''
        to delete an item from the PyList
        '''

        if index > self.numItems-1:
            raise ValueError("Index should be lower, the list does not have item in this index")

        for i in range(index, self.numItems-1):
            self.items[i] = self.items[i+1]
        
        self.numItems -= 1 

    def __eq__(self, other):
        '''
        To check if two PyList are same or not
        '''
        #check 1 : if type is not similar 
        if type(self) != type(other):
            return False
        
        #check 2: if num of items in both lists are not similar 
        if self.numItems != other.numItems:
            return False
        
        #check 3: now checking each element of both lists, break it as soon as one of the items is not similar
        for i in range(self.items):
            if self.items[i] != other.items[i]:
                return False
        
        # check 4: okay, if you have reached so far, they must be similar lists
        return True

    def __iter__(self):
        '''
        a method to iterate over the list 
        '''
        for i in range(self.numItems):
            return self.items[i]

    def __len__(self):
        '''
        to get the length of the PyList object 
        '''
        return self.numItems

    def __contains__(self, item):
        '''
        to see if the PyList contains this item; linear search in the PyList
        '''
        for i in range(self.numItems):
            if self.items[i] == item:
                return True
        
        return False

    def __repr__(self):
        '''
        repr method to see the object more meaningfully
        '''
        s = "PyList(["
        for i in range(self.numItems):
            s += repr(self.items[i])
            if i < self.numItems-1:
                s += ", "
        s += "])"
        return s

if __name__=='__main__':
    example = PyList(['a','b','c','d'], size=3)
    example2 = PyList([1,2,3], 5)
    example




    