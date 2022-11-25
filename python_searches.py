def linear_search(search_item, items):
    """Return boolean for if search_item in items"""
    pass

def linear_search_for_index(search_item, items):
    """Return int index of search_item in items, or -1 for not there"""
    pass

def binary_search(search_item, items):
    """Return boolean for if search_item in sorted list items"""
    #set start and end position for sub-array item could be in
    start_index = 0
    end_index = len(items) - 1
    
    #loop as long as subarray is not empty
    while start_index <= end_index:
        #mid_index is int average of start_index and end_index
        mid_index = (start_index + end_index) // 2
        #set current_item to the item in the middle
        current_item = items[mid_index]
        #if current item is what we're looking for return True
        if current_item == search_item:
            return True
        #otherwise update the start_index or end_index depending on 
        #which section of the array can be discarded.
        elif current_item > search_item:
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1
    #...only return False when you are sure that the search_item is not in items
    return False

print(binary_search(4, [1,3,4,5,5,48,450]))

