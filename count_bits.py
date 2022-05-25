
#Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
#
#Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case




def count_bits(n):
    count = 0            #inicializace
    while(n>0):          #když n bude větší než nule proveď blok IF
        if n%2:           ## když bude  n(zbytek po dělení) 2
            count+=1      ##připočti k inicializaci 1
        n = n // 2       # jako n nyní výsledek celo číselného děleni
    return count