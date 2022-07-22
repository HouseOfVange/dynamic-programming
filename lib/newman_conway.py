''' 
P(1) = 1
P(2) = 1
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1)) 
'''

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    # base case guard clauses
    if num < 1:
        raise ValueError('newman conway number cant be zero nums long')
    elif num == 1:
        return '1'
    elif num == 2:
        # print ('1 1')
        return '1 1'

    memo = [0,1,1]
    count = 3

    while count <= num:
        #            P(P(n - 1))        +    P (n - P(n - 1)) 
        memo.append(memo[memo[count-1]] + memo[count - memo[count-1]])
        count += 1

    NCnums = []
    for num in memo:
        NCnums.append(str(num))
    # print(NCnums[1:])
    return " ".join(NCnums[1:])
    # return NCnums[1:]

newman_conway(10)