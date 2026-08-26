#Q1 List Analyser
num=int(input())    #no. of terms in list
og_list = input().split()   #converting string to list
og_list = [int(x) for x in og_list]    #changing string list to int list
maxNo=og_list[0]        #maximum number
minNo=og_list[0]        #minimum number
sumNo=0                 #sum of all
oddCount=0              #no. of odd nos.
evenCount=0             #no. of even nos.
rev_list=[]
if len(og_list)==num:
    for i in range(num):
        if maxNo<og_list[i]:
            maxNo = og_list[i]
        if minNo>og_list[i]:
            minNo = og_list[i]
        sumNo+=og_list[i]
        if og_list[i]%2 ==0:
            evenCount+=1
        else:
            oddCount+=1
    rev_list = og_list[::-1]            #reversing the list
    print(f" Largest: {maxNo} \n Smallest: {minNo} \n Sum: {sumNo} \n Even count: {evenCount} \n Odd count: {oddCount}")
    print(f" Reversed: {rev_list}")
else:
    print("Invalid number of inputs!")
