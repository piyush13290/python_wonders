
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



if __name__=='__main__':
    example = PyList(['a','b','c','d'], size=3)


    