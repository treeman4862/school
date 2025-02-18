#Insertion Sort

array = [12,50,23,30,27,31,49,16,29,8]

def Sort(): # fix this replace for with while for decrementing i
    sorted = array[0]
    
    for i in array:
        if sorted > array[i]:
            arr[i], arr[sorted] = arr[sorted], arr[i]
            i = i-1
        else:
            i+1

Sort()