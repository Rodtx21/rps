#Made by Rodtx21
def get_int(r):
    a = input(r)

    while (True):
        if (a.isnumeric() == True):
            return int(a)
        else:
            a = input(r)

def get_float(r):
    a = input(r)

    while(True):
        if (isfloat(a) == True):
            return float(a)
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