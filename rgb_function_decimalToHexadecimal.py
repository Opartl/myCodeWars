'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3

'''



def rgb(r, g, b):
    output = ''                     #we want output in string (for examle FFFFFF - it is string)
    
    for value in (r, g, b):                                         # in for cycle, we look on r,g,b and condition min/max defining interval 0-255
        output += hex(max(0, min(255,value)))[2:].upper().zfill(2)  #[2:] only character from third place (example - r = 255; hex(r)= 0xff and we want only ff, but upper case)
                                                                    #zfill(2) fill form to 2 character (for example r=0 , hex(r)[2:]=0; hex(r)[2:].zfill(2)=00)
    return output