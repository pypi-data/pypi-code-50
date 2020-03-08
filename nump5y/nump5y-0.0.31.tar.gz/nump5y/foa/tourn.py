Ans='''"""
"""tournament method A method of finding a specific element in some set (e.g. largest of a set of numbers), so called because it involves pairing elements and comparing them to find which one goes through to the next stage, leaving just one element at the end that has not lost."""

def largest(L):
    global paris
    if len(L) == 1:
        return L[0]
    else:
        left = largest(L[:len(L)//2])
        right = largest(L[len(L)//2:])
        pairs.append((left, right))
        return max(left, right)

def second_largest(L):
    global pairs
    biggest = largest(L)
    second_L = [min(item) for item in pairs if biggest in item]

    return biggest, largest(second_L)  



if __name__ == "__main__":
    pairs = []
    # test array
    L = [2,-2,10,5,4,3,1,2,90,-98,53,45,23,56,432]    

    if len(L) == 0:
        first, second = None, None
    elif len(L) == 1:
        first, second = L[0], None
    else:
        first, second = second_largest(L)

    print('The largest number is: ' + str(first))
    print('The 2nd largest number is: ' + str(second))


"""
'''
