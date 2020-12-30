# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    # create list to hold string pairs

    # if string is even, endpoint is end of string
    # else, endpoint is end of string minus one pair

    # go through loop
        # keep track of index and index + 1 for the two chars
        # add the two chars to list of strings
        # index moves two spaces
    # if string is odd
        # make one more pair with last char and underscore
        # add to list of strings
    
    # return list

print(solution('abcd'))