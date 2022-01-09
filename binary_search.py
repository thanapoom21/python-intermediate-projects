def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index, target):
    if index is not None:
        print(target, " is found at index: ", index)
    else:
        print(target, " is not found in the list")


one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(one_to_ten, 12)

verify(result, 12)

existed_result = binary_search(one_to_ten, 2)

verify(existed_result, 2)
