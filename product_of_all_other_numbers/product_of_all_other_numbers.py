'''
Input: a List of integers
Returns: a List of integers
'''

from functools import reduce

def product_of_all_other_numbers(arr):

    products = []
    for i in range(len(arr)):

        product = 0
        arr_to_mult = []

        if i == 0:
            for val in arr[i+1:]:
                arr_to_mult.append(val)
            products.append(reduce(lambda x, y: x * y, arr_to_mult))
            print(products)
        else:
            first = []
            second = []

            for val in arr[0:i]:
                first.append(val)
            for val in arr[i+1:]:
                second.append(val)
            arr_to_mult = first + second
            products.append(reduce(lambda x, y: x * y, arr_to_mult))

    return products



if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
