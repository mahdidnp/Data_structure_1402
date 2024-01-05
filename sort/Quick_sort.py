def quick_sort(list, start, end):
    if start>=end:
        return
    
    boundry=partition(list, start, end)
    

    quick_sort(list, start, boundry-1)
    quick_sort(list, boundry+1, end)

    return list

    
def partition(list, start, end):
    pivot=list[end]
    boundry=start-1
    
    for i in range (start, end+1):
        if list[i]<=pivot:
            boundry+=1
            swap(list, i, boundry)
    return boundry

def swap(list, first, second):
    temp=list[first]
    list[first] = list[second]
    list[second]=temp






unordered_list=[22,13,78,23,51,56]
size=len(unordered_list)
print(quick_sort(unordered_list, start=0, end=size-1))