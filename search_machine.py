def binary_search(searched, sorted_list):
    median_index = len(sorted_list) // 2
    median = sorted_list[median_index]
    if len(sorted_list) == 1:
        if median == searched:
            return True
        else:
            return False
    if searched > median:  # searched is in right half
        return binary_search(searched, sorted_list[median_index:])
    elif searched < median:  # searched is in left half
        return binary_search(searched, sorted_list[:median_index])
    else:
        return True
