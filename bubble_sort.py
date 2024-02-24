#Lab - 1 DAA
#24.02.24 - Sat(Fri)
# M Hemasri - AIE22028 (D)
import time

def bubble_sort(array):
    print("*****  Bubble sort  *****")

    for i in range(0,len(array)-1,1):
        flag=0
        for j in range(0,len(array)-1-i,1):
            if array[j]>array[j+1]:
                flag=1
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
        if flag==0:
            print("The iterations took to sort the array is: ",i+1,"iterations")
            break;

    return array

inlist=[]
size=int(input("Enter the size of the array: "))
for i in range(0,size,1):
    ele=int(input("Enter the element: "))
    inlist.append(ele)
start=time.time()    
result=bubble_sort(inlist)
end=time.time()
print(result)
print("Execution time in milliseconds : ",(end-start)*1000)
