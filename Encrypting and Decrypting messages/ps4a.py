# Problem Set 4A
# Name: MORO OWUSU AFRIYIE
# Collaborators:
# Time Spent: 10 Minutes

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    permutation_list = []
    if len(sequence) == 1:  # if it cotains onw letter it should just return that letter
        return sequence
    else:
        for i in range(len(sequence)):
            s = sequence[i]  # stores the letter with respect to the number i
            m = sequence[:i] + sequence[i + 1:]
            for a in get_permutations(m):  # recursion
                permutation_list.append(s + a)
        return permutation_list

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))



