#min_heapyfy(array,i) : bir dizinin i indeksindeki elemanı ile o elemanın sağındaki ve solundaki elamanlan büyüklük kıyaslaması yapar. Küçük olanı üste çıkartır. diziyi heap yapısına çevirir

#build_min_heapy(array) : aldığı dizinin yarısından itibaren geriye doğru kontrol edee ve bütün diziyi MinHeap düzenine sokar.

#heapsort(array) : bir heap yapısını küçükten büyüğe sıralar

#insertItemToHeap(MinHeapyArray,i) : Bir heapm in heap algoritmasına uygun bir şekilde eleman ekler.

#removeItemFrom(myheap_1) : Parametre olarak aldığı MinHeap düzenin de ki array'in son elemanını siler.


def min_heapyfy(array,i):
    left = 2*i+1
    right = 2*i+2
    length = len(array)-1
    smallest = i
    if left<=length and array[i]>array[left]:
        smallest = left
    if right<=length and array[smallest]>array[right]:
        smallest = right
    if smallest != i:
        array[i],array[smallest] = array[smallest],array[i]
        min_heapyfy(array,smallest)
def build_min_heapy(array):
    for i in reversed(range(len(array)//2)):
        min_heapyfy(array,i)

my_array_1 = [8,10,3,4,7,15,1,2,16]
min_heapyfy(my_array_1,4)
print(my_array_1)
my_array_1 = [8,10,3,4,7,15,1,2,16]
build_min_heapy(my_array_1)
print(my_array_1) 

def heapsort(array):
    array = array.copy()
    build_min_heapy(array)
    sorted_array = []
    for _ in range (len(array)):
        array[0],array[-1] = array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapyfy(array,0)
    return sorted_array

Sorted_Array = heapsort(my_array_1)
print(Sorted_Array)

def insertItemToHeap(MinHeapy_array,item):
    MinHeapy_array.append(item)
    i = len(MinHeapy_array)-1
    if i<=0:
        return    
    parent = (i-1)//2
    while parent>=0 and MinHeapy_array[parent] > MinHeapy_array[i]:
        MinHeapy_array[parent],MinHeapy_array[i] = MinHeapy_array[i],MinHeapy_array[parent]            
        i = parent
        parent = (i-1)//2

def removeItemFrom(myheap_1):
    index = len(myheap_1)
    if index<=0:
        print("heap zaten boş")
        return
    myheap_1.pop()

insertItemToHeap(my_array_1,5)
print(my_array_1)
removeItemFrom(my_array_1)
print(my_array_1)
