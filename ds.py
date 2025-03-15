my_list = []
for i in range(10, 50, 10):
    my_list.append(i)
#my_list = [10, 20, 30, 40]

my_list.insert(1, 15)
#my_list = [10, 15, 20, 30, 40]

list_2 = [50, 60, 70]

my_list += list_2 #can also use my_list.extend(list_2)
#my_list = [10, 15, 20, 30, 40, 50, 60, 70]

my_list.pop()
#my_list = [10, 15, 20, 30, 40, 50, 60]

my_list.sort() #descending order - my_list.sort(reverse=True)

print(my_list.index(30))