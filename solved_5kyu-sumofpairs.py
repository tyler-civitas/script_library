""" 5 Kyu - sum of pairs kata.
I was having difficulty getting this kata to run within the
12000ms time constraint.
Eventually, I collaborated with another programmer to
determine that xrange was necessary for "lazy" loop evaluation.
This would prevent the entire loop from being evaluated
prior to the function return."""

def sum_pairs(ints, s):

    values_index = {} # Dictionary with the value as index, and key as the list location

    for i in xrange(len(ints)): # Runs a loop for as many items in ints
        if s - ints[i] in values_index.keys(): # If the value we are on is one of the keys in the dictionary
            for num in values_index[s - ints[i]]: # for every value that works as second number in the dictionary
                return [ints[num], ints[i]] # return the outer i as second num, inner 'num' as first num
        else:
            values_index[ints[i]] = [i] #Store the value in the dictionary with key as value and value as index
# Essentially, it's creating possible matches as indexes of each i value as it goes
# That i value will always be the first number,'num' since it was entered into
# the index first
    return None




""" Solution that didn't work due to time"""
def sum_pairs(ints, s):
    best_tuple = ()
    finals = set()

    for ind2, num2 in enumerate(tuple(ints)):
        for ind1, num1 in enumerate(tuple(ints)):
            if (num1 + num2) == s:
                finals.add(((ind1, num1), (ind2, num2)))

    if finals == set():
        return None
    else:
        best_tuple = finals.pop()

    for pair in finals:
        if (pair[0] == pair[1]) or (pair[0][0] > pair[1][0]):
            continue
        elif pair[1][0] < best_tuple[1][0]:
            best_tuple = tuple(pair)
        elif (pair[1][0] == best_tuple[1][0]) and (pair[0][0] < best_tuple[0][0]):
            best_tuple = tuple(pair)
        else:
            pass

    return [best_tuple[0][1], best_tuple[1][1]]


"""SIMPLER SOLUTION, lost to time constraints"""
def sum_pairs(ints, s):

    for ind2, num2 in enumerate(tuple(ints)):
        for num1 in set(ints[:ind2]):
            if num1 + num2 == s:
                return [num1, num2]

    return None
