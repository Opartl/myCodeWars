'''There is an array with some numbers. 
# All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.
# 
# '''



def find_uniq(arr):
    
    arr.sort()                                                  # first - we sort array -> for example we have [8,7,7,7,7] => [7,7,7,7,8]

    if(arr[0] < arr[-1] and arr[0] < arr[2]):                   # we compare first number with last  and first number with lastButOne  
        n = arr[0]                                              #so example - [7,7,7,7,8]  =>  7 < 8 and 7 < 7  (condition not met) we jump to "else"
    else:
        n = arr[len(arr)-1]                                     #this mean like n = arr[-1] (last number is n) 

                                                                #in another case is number, what we want find, is as FIRST NUMBER in sorted array, so IF condition will met and n=arr[0] - first number
    return n 