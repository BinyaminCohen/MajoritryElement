from collections import Counter


def majority_element(num_list):
    max_value_item = max(Counter(num_list).values())
    return [key for key, val in Counter(num_list).most_common() if val == max_value_item]


print(majority_element([3, 4, 3]))
print(majority_element([3, 4, 3, 4]))
