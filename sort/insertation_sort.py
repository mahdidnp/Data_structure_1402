def insertation_sort(list,size):

    for i in range(1,size):
        current_index=i
        previouse_index=i-1
        while previouse_index >=0 and list[current_index]<list[previouse_index]:
            list[previouse_index+1],list[previouse_index]=list[previouse_index],list[previouse_index+1]
            previouse_index-=1
    return list



unordered_list=[22,13,78,23,51,56]
size=len(unordered_list)
print(insertation_sort(unordered_list,size))


