def conv_ls(N):
    """convert a number in a list of integers"""
    a = list(str(N))
    return list(map(lambda i: int(i), a))

def conv_nmbr(N):
    """
    convert a list of integers in a number
    """
    a = list(map(lambda i: str(i), N))
    return int("".join(a))

def add_integer(N,n):
    """
       input ----> list of integers
       output ---> list of integers with the max possible number by inserting n 
    """
    count = 0
    while count < len(N):
        if (N[count] >=0) & (N[count] <= n):
            N.insert(count, n)
            return N
            break
        if (N[count] > 5) & (N[count+1] <= 5):
            N.insert(count+1, n)
            return N
            break
        else:
            N.insert(len(N), n)
            return N
            break
        count+=1

def delete_neg(N,n):
    """delete the negative '-' sign from a number and return a list of integers
       input ---> negative number
       output ---> list of integers without '-'
    """
    a = list(str(N))
    a.remove('-')
    b = list(map(lambda i: int(i), a))
    b.insert(0,n)
    return b


def solution(N):
    """
    INSERT MAX POSSIBLE VALUE BY INSERTING A n IN A GIVEN POSITIVE/NEGATIVE NUMBER
    input ---> number positive/negative
    output ---> number positive/gative
    """
    if N >= 0:
        a = conv_ls(N)
        b = add_integer(a,5)
        c = conv_nmbr(b)
        return c
    if N < 0:
        a = delete_neg(N,5)
        b = conv_nmbr(a)
        c = -b
        return c

a = solution(91789)
print(a)