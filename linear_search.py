def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target is found at index: ", index)
    else:
        print("Target is not found in the list")


one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(one_to_ten, 2)

verify(result)
