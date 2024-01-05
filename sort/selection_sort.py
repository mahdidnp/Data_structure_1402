def selection_sort(list):

    for j in range(len(list)):

        for i in range(j+1, len(list)):

            if list[j]>list[i]:
                list[j],list[i]=list[i],list[j]
                
    return list

unordered_list=[4,5,1,8,75,45,23,11]
print(selection_sort(unordered_list))