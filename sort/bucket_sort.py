import math

def bubble_sort(list):

    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
              list[j],list[j+1]=list[j+1],list[j]
    return list


def bucket_sort(list,size):

    array=[]*size

    for i in list:
        element= math.floor(i*size)
        print(i*size)
        array[element].append(i)

    for i in range(size):
        array[i]= bubble_sort(array[i])

    k = 0
    for i in range(size):
        for j in range(size):
            list[k] = array[i][j]
            k += 1
    return list

    
    
        
            
            
            


unordered_list=[0.12,0.36,0.1,0.86,0.45,0.65,0.79,0.23,0.51,0.63]

size=len(unordered_list)
print(bucket_sort(unordered_list, size))