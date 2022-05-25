# Moving Zeros To The End

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


def move_zeros(array):
    l1 = []
    l2 = []
    for i in array:
        if i != 0 or isinstance(i, bool):
            l1.append(i)
        else:
            l2.append(i)
    array = l1+l2
    return l1+l2
