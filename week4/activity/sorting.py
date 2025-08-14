from galaxy import Galaxy

def my_mutating_sort(items):
    gax = len(items)
    for i in range(gax):
        for j in range(gax - i - 1):
            if items[j] > items[j + 1]:
               items[j], items[j + 1] = items[j + 1], items[j]

    return items

def my_immutable_sort(items):
    new_items = items[:]
    my_mutating_sort(new_items)
    return new_items

def galaxy_sorting_method(galaxies):
    return my_immutable_sort(galaxies)
