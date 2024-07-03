def getInput():
    """
    Prompts the user to enter multiple values in a single line.
    Splits these values and converts them into a list of integers.
    Returns the list of integers.
    """
    user_input = input("Enter multiple values separated by space: ")
    return list(map(int, user_input.split()))

def listSum(list1, list2):
    """
    Takes two lists of numbers, creates a new list containing the summation
    of corresponding values from each list, and returns the new list.
    """
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

def main():
    list1 = getInput()
    list2 = getInput()
    ret = listSum(list1, list2)
    print(f'The result values are: {ret}')

if __name__ == '__main__':
    main()
