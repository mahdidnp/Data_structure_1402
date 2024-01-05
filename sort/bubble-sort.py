def bubble_sort(list):

    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
              list[j],list[j+1]=list[j+1],list[j]
    return list

unordered_list=[8,9,45,78,12,2,3,6,14]
print(bubble_sort(unordered_list))