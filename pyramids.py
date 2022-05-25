# Lyrics...

# Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a pyramid built of numbers, like this one here:

#    /3/
#   \7\ 4 
#  2 \4\ 6 
# 8 5 \9\ 3

# Here comes the task...

# Let's say that the 'slide down' is the maximum sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23

# Your task is to write a function longestSlideDown (in ruby/crystal/julia: longest_slide_down) that takes a pyramid representation as argument and returns its' largest 'slide down'. For example,

# longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) => 23

# By the way...

# My tests include some extraordinarily high pyramids so as you can guess, brute-force method is a bad idea unless you have a few centuries to waste. You must come up with something more clever than that.


def longest_slide_down(pyramid):
    if len(pyramid) == 1:                                   #for only one number in list
        return pyramid[0][0]

    last_layer = pyramid[-1]                                #last layer in pyramid in examile [8,5,9,3]
    add_layer = []                                          #inicialize new list,where we will add new layer
    for i in range(1, len(last_layer)):                             #we look for every list range
        add_layer.append(max(last_layer[i], last_layer[i-1]))       #we added max number to "add_layer" - so we create new layer


    pyramid[-2] = [a+b for a, b in zip(pyramid[-2], add_layer)]     #zip function join two lists to one list and we this function use in comprehension list

    return longest_slide_down(pyramid[:-1])                         #for every run in "for cycle" we have new layer and we recursive search the best way to up pyramids