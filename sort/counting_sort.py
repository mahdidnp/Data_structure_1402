def counting_sort(list,size):
    max=0
    for i in list:
        if i>max:
            max=i
        
    array=[0]*(max+1)


    for i in range(size):
        for element in list:
            if element==i:
                array[i]+=1
        
        if max==i:
            break

    list.clear()
    for i in range (max+1):
        if array[i]==0:
            continue
        
        for j in range(array[i]):
            list.append(i)
    return list









unordered_list= [2,2,3,3,1,1,1,4,4]
size= len(unordered_list)
print(counting_sort(unordered_list,size))