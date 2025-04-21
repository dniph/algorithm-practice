# Add your clarifying questions here

# I will assume all the input is a valid list
# If the shift by number is > than lst, make sure the shift does not exceed the list length
# Shif all the elements to the right





lst = [1, 2, 3, 4, 5]



def rotate_list(lst, shift_by):
    n = len(lst)
    # Make sure the shift doesn't exceed the list length
    shift_by %= n  
    for _ in range(shift_by):
        # Save the last element
        last = lst[-1]
        
        # Shift all elements one position to the right
        for i in range(n - 1, 0, -1):
            lst[i] = lst[i - 1]
        
        # Place the last element at the beginning
        lst[0] = last
        
rotate_list(lst, 3)        
print(lst)  # [3, 4, 5, 1, 2]