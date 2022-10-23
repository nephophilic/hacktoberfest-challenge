# Try to find out how many zeros a given number has at the end.

def end_zeros(num: int) -> int:
    for x in str(num)[::-1]:
        if  x != '0':
            return str(num)[::-1].find(x)
    return len(str(num))

    
print('Example:')
print(end_zeros(10))



assert end_zeros(10) == 1
assert end_zeros(10001001) == 0
assert end_zeros(1000) == 3
assert end_zeros(100) == 2
assert end_zeros(20010) == 1
assert end_zeros(100001000) == 3
assert end_zeros(101010) == 1
assert end_zeros(10001001) == 0
assert end_zeros(100010) == 1
assert end_zeros(100) == 2
assert end_zeros(20010) == 1
assert end_zeros(100001000) == 3

print("The mission is done! ")
 
# expected output :
#1
#The mission is done! 