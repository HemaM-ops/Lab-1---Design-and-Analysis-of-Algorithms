# Lab - 1:Selection sort (DAA)
# 24.02.24 - Sat (fri)
# M Hemasri - AIE22028

import time

def insertion_sort(array):
    print("*****  Insertion Sort  *****")

    for i in range(1,len(array),1):
        temp=array[i]
        j=i-1
        while j>=0 & array[j]>temp:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=temp
    return array


inlist=[]
size=int(input("Enter the size of the array: "))
for i in range(0,size,1):
    ele=int(input("Enter the element: "))
    inlist.append(ele)
start=time.time()    
result=insertion_sort(inlist)
end=time.time()
print(result)
print("Execution time in milliseconds : ",(end-start)*1000)
