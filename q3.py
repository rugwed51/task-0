def is_prime(n):        #declaring the function "is_prime"
    result = False
    if n<2:
        return False
    for j in range(2, int(n/2)+1):  #iterating thru the range of numbers for prime check
        if n%j==0:
            result=False
            break
    else:
        result=True
    return result

num = int(input())
for i in range(2,num+1):    #iterating thru numbers from 2 to the number itself
    if is_prime(i):         #function call
        print(i, end=' ')
