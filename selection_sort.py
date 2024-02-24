# Lab - 1:Selection sort (DAA)
# 24.02.24 - Sat (fri)
# M Hemasri - AIE22028

import time
def selection_sort(array):
    print("*****  Selection Sort *****")
    for i in range(0,len(array)-1,1):
        min=i
        for j in range(i+1,len(array),1):
            if array[j]<array[min]:
                min=j
        if min!=i:
            temp=array[i]
            array[i]=array[min]
            array[min]=temp
    return array



inlist=[]
size=int(input("Enter the size of the array: "))
for i in range(0,size,1):
    ele=int(input("Enter the element: "))
    inlist.append(ele)
start=time.time()    
result=selection_sort(inlist)
end=time.time()
print(result)
print("Execution time : ",end-start)
