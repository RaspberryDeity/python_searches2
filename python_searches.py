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
    # mid_index is int average of start_index and end_index        
    # set current_item to the item in the middle
    # compare current_item to search item, and return True if found
    # or update the start_index or end_index depending on 
    # which section of the array can be discarded.
    # return False when you are sure that the search_item is not in items

print(binary_search(4, [1,3,4,5,5,48,450]))

