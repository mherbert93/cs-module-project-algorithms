'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    nonzero = []
    zeros = []

    for val in arr:
        if val == 0:
            zeros.append(val)
        else:
            nonzero.append(val)

    return nonzero + zeros



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")