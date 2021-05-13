# let;s write some recursion funcions 

def main():

    # example 1: reverxe a  list 

    def reverse_list(a_list):
        '''
        reverses a list 
        '''

        rev_list = []
        for i in a_list:
            rev_list = [i] + rev_list # this is very inefficient way  to add a list 

        return rev_list


    a  = [1,2,3]
    b = reverse_list(a)

    print(a)
    print(b)
    # this works fin

    # using recursion

    def recursive_rev_list(a_list):
        '''
        recursively reverses the list
        '''

        my_rev_list = []
        # base case: 
        if a_list == []:
            return []
        last_value = a_list[-1]

        give_me_rev_list = recursive_rev_list(a_list[0:-1])
        return [last_value] + give_me_rev_list

    c = recursive_rev_list(a)

    if b==c:
        print("Wohooo.. it seems to be working")

    
if __name__ == "__main__":
    main()