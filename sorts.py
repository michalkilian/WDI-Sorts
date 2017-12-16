import random 

def wstawianie(tablica):
    for i in range(1,len(tablica)):
        for j in range (i,0,-1):
            if tablica[j-1]>tablica[j]:
                tablica[j-1],tablica[j]=tablica[j],tablica[j-1]
            else:
                break
    return tablica
    
def wybieranie(tablica):
    for i in range(len(tablica)):
        minimalna = tablica[i]
        index = i
        for j in range(i+1,len(tablica)):
            if tablica[j]<minimalna:
                minimalna = tablica[j]
                index = j
        tablica[i],tablica[index]= tablica[index],tablica[i]
    return tablica

def bubble(tablica):
    for i in range(len(tablica)-1):
        isSorted = True
        for j in range(len(tablica)-i-1):
            if (tablica[j+1]<tablica[j]):
                isSorted = False
                tablica[j],tablica[j+1] = tablica[j+1],tablica[j]
        if isSorted == True:
            break
    return tablica

def quickSort(tablica):
    mniejsze = list()
    rowne = list()
    wieksze = list()
    
    if (len(tablica)>1):
        pivot = tablica[0]
        for i in tablica:
            if(i>pivot):
                wieksze.append(i)
            elif(i<pivot):
                mniejsze.append(i)
            else:
                rowne.append(i)
        return quickSort(mniejsze)+rowne+quickSort(wieksze)
    else:
        return tablica
    
def mergeSort(tablica):
    wynik = list()
    if(len(tablica)<2):
        return tablica
    srodek = len(tablica)//2
    tab1 = mergeSort(tablica[:srodek])
    tab2 = mergeSort(tablica[srodek:])
    i = 0
    j = 0
    while( i<len(tab1) and j<len(tab2)):
        if(tab1[i]>tab2[j]):
            wynik.append(tab2[j])
            j+=1
        else:
            wynik.append(tab1[i])
            i+=1
    wynik+=tab1[i:]
    wynik+=tab2[j:]
    return wynik

def heapSort(tablica):
    for i in range(len(tablica),-1,-1):
        heapify(tablica,len(tablica),i)
    for i in range(len(tablica)-1,0,-1):
        tablica[0],tablica[i]=tablica[i],tablica[0]
        heapify(tablica,i,0)
    return tablica
def heapify(tablica,size,root):
    largest = root
    lChild = 2*root+1
    rChild = 2*root+2
    if(lChild<size and tablica[largest]<tablica[lChild]):
        largest = lChild
    if(rChild<size and tablica[largest]<tablica[rChild]):
        largest = rChild
    if(largest!=root):
        tablica[root],tablica[largest]=tablica[largest],tablica[root]
        heapify(tablica,size,largest)

def randFill(tablica):
    for i in range(50):
       nowaLiczba = random.randint(0,300)
       tablica[i]=nowaLiczba
    

tablicaLiczb = [0]*50

randFill(tablicaLiczb)
tablicaLiczb1=tablicaLiczb.copy()
tablicaLiczb2=tablicaLiczb.copy()
tablicaLiczb3=tablicaLiczb.copy()
tablicaLiczb4=tablicaLiczb.copy()
tablicaLiczb5=tablicaLiczb.copy()
tablicaLiczb6=tablicaLiczb.copy()

print(tablicaLiczb)
print(bubble(tablicaLiczb1))
print(wybieranie(tablicaLiczb2))
print(wstawianie(tablicaLiczb3))
print(quickSort(tablicaLiczb4))
print(mergeSort(tablicaLiczb5))
print(heapSort(tablicaLiczb6))