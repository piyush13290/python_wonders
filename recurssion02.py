
# problem 1: find x**n recursively  

def power_fun(x, n):
    '''
    simple recursive fun to find x**n
    '''

    # base case:
    if n == 0:
        return 1

    give_me_your_work = power_fun(x, n-1)

    return x * give_me_your_work

print(power_fun(2,3))
print("this works!")

# Problem 2: factorial of an integer (classic one)

def rec_factorial(x):

    if x == 0:
        return 1

    give_me_your_part = rec_factorial(x-1)

    return x * give_me_your_part

print(rec_factorial(5))
print("this works!")

# Problem 3: finds a lenght of a string recursively, and can not use len()

def find_len(s):
    assert type(s) is str

    if not s:
        return 0
    
    give_me_yr_digits = find_len(s[1:])

    return 1 + give_me_yr_digits

print(find_len("piyush"))
print("this works as well!")


# Problem 3: 'abcdef' -> 'badcfe' swaps first two characters of the string 

def swap_2(s):
    '''
    swaps every first two characters of a string
    '''

    if len(s) == 0:
        return ''
    if len(s) == 1:
        return s

    give_me_your_part = swap_2(s[2:])

    my_swap = s[1] + s[0]

    return my_swap + give_me_your_part

print("Piyush")
print(swap_2("Piyush"))
print(swap_2("Piyus"))
print("this makses sense")

