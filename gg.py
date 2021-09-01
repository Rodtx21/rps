import random

def get_int(r):
    a = input(r)

    while (True):
        if (a.isnumeric() == True):
            return int(a)
        else:
            a = input(r)

def isfloat(a):
    # Python code to convert string to list character-wise https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
    def Convert(string):
	    list1=[]
	    list1[:0]=string
	    return list1

    str(a)
    b = Convert(a)
    c = len(b)
    numbers = 0
    onlypoint = 0
    x = 0
    
    while x < c:
        if (b[x].isnumeric() == True):
            numbers += 1
        elif (b[x] == "."):
            onlypoint += 1
        elif (b[x].isnumeric() == False and b[x] != "."):
            return False
        
        x += 1
    
    if numbers == c - 1 and onlypoint == 1:
        return True
    else:
        return False

def get_string(r):
    a = input(r)

    while (True):
        if (a.isnumeric() == False and isfloat(a) == False):
            return str(a)
        else:
            a = input(r)

def modu(x):
    if x >= 0:
        return x
    else:
        y = 0 - x
        return y

def game(com_guess, tries):
    while True:
        #prompt for guess
        users_guess = get_int("Your guess:")

        #compare
        diff = modu(com_guess - users_guess)

        if diff == 0:
            print("\n\nYou guessed the number in " + str(tries) + " tries.\n\n")
            break

        if diff == 1:
            print("\n\nAlmost there!!\n\n")

        elif 2 <= diff <= 3:
            print("\n\nClose!\n\n")

        elif diff > 3:
            print("\n\nPretty far!\n\n") 

        
        tries += 1

def main():
    #prompt for user's name
    name = get_string("What's your name?"+ '\n' + '\n')

    #Great user
    print('\n\nSo ' + name + ", let's play.\n")

    #round sys
    round = 1

    #while loop
    while True:
        print('Round number ' + str(round) + '\n\n')
        tries = 1
        round += 1

        #computer makes guess
        com_guess = random.randint(1, 10)
        game(com_guess, tries)

main()