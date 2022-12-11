import operator
import copy


def solve(first_array: list, sec_array: list) -> list:
    """
    Rearranges sec_array such that the pair wise distance is minimized
    :param first_array: flattened original image
    :param sec_array: style of second image
    :return: a rearranged sec_array
    """
    new_list = []
    for element in first_array:
        distances = []
        for item in sec_array:
            diff = abs(element - item)
            distances.append((diff, item))
        distances = sorted(distances, key=operator.itemgetter(0), reverse=False)
        new_list.append(distances)

    final_list = []
    sec_array_copy = copy.deepcopy(sec_array)
    for lst in new_list:
        for _, num in lst:
            if num in sec_array_copy:
                final_list.append(num)
                sec_array_copy.remove(num)
    print(final_list)
    return final_list


solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 1, 7, 6, 5, 4, 3, 2, 8])