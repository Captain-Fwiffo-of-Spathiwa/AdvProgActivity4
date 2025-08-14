from galaxy import Galaxy

def quick_sort(galaxy_list):
    # already sorted
    if len(galaxy_list) <= 1:
        return galaxy_list

    # choose a pivot value e.g. the middle element
    pivot_value = galaxy_list[len(galaxy_list) // 2]

    # less than pivot
    smaller_than_pivot = [aGalaxy for aGalaxy in galaxy_list if aGalaxy.mass < pivot_value]

    # equal to pivot
    equal_to_pivot = []
    for aGalaxy in galaxy_list:
        if aGalaxy.mass == pivot_value:
            equal_to_pivot.append(aGalaxy)

    # greater than pivot
    greater_than_pivot = [aGalaxy for aGalaxy in galaxy_list if aGalaxy > pivot_value]
    
    # recursion
    return quick_sort(smaller_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)


# Example usage
# print(quick_sort([64, 34, 25, 12, 22, 11, 90]))
