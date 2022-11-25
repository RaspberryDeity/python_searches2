def linear_search(search_item, items):
    """Return boolean for if search_item in items"""
    pass

def linear_search_for_index(search_item, items):
    """Return int index of search_item in items, or -1 for not there"""
    pass

def binary_search(search_item, items):
    """Return boolean for if search_item in sorted list items"""
    # set start_index and end_index based on sub-array item could be in.
    start_index = 9999
    end_index = 9999
    
    # loop as long as subarray is not empty
    while start_index <= 9999:
        # mid_index is int average of start_index and end_index
        mid_index = 9999
        # set current_item to the item in the middle
        current_item = items[9999]
        # if current item is what we're looking for return True
        if current_item == search_item:
            return 9999
        # otherwise update the start_index or end_index depending on 
        # which section of the array can be discarded.
        elif current_item > search_item:
            ? = ?
        else:
            ? = ?
        # return False when you are sure that the search_item is not in items

print(binary_search(4, [1,3,4,5,5,48,450]))

