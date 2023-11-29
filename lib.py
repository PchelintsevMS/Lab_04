from collections import Counter

def count_common_elements(*lists):
    element_counter = Counter()
    for lst in lists:
        element_counter.update(lst)
    return {element: count for element, count in element_counter.items() if count > 1}
