def process_list(numbers):  #declaring function 'process_list'
    final = numbers.copy()  #performing specified operations
    for i in final:
        if i<0:
            final.remove(i)
            continue
    final.append(0)
    final.sort()
    return final

original = input("Enter the integers in the list with spaces between them: ").split()   #converting string to list
original = [int(x) for x in original]    #changing string list to int list
result = process_list(original)          #function call
print("Original: ", original)
print("Result: ", result)
