import operator
import copy
import matplotlib.pyplot as plt
import numpy as np


def solve(first_array: list, sec_array: list) -> list:
    """
    Rearranges sec_array such that the pair wise distance is minimized
    :param first_array: flattened original image
    :param sec_array: style of second image
    :return: a rearranged sec_array
    """
    assert len(first_array) == len(sec_array), "The length of the arrays should be similar."
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


# solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 1, 7, 6, 5, 4, 3, 2, 8])
starry = plt.imread("Image/new_starry.jpg")
blaise = plt.imread("new_blaise_2.jpeg")
sunset = plt.imread("Image/sunset.jpeg")
# print(f"Starry: {starry.shape} \n"
#       f"Sunset: {sunset.shape} \n"
#       f"blaise: {blaise.shape}")
# b = copy.deepcopy(blaise)
# s = copy.deepcopy(sunset)
# st = copy.deepcopy(starry)
# b = b.flatten()
# s = s.flatten()
# st = st.flatten()
# print(b)
# print(len(b), len(s), len(st))


# plt.imshow(blaise)
# plt.show()
# new_blaise = copy.deepcopy(blaise)
# new_blaise = new_blaise.flatten()
# print(new_blaise)
# b = new_blaise.reshape(blaise.shape)
# b = np.rot90(b, k=3)
# print(b)
# plt.imshow(b)
# plt.show()

# print(type(blaise))
# b_1 = blaise.tolist()
content = blaise.flatten().tolist()
style = starry.flatten().tolist()
# print(type(b))
solve(content, style)