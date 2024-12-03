from random import randint
index = 0
comb = 0
list = []
main_input = int(input("vvedite chislo: "))
num_list = [[randint(-10, 10) for i in range(4)] for i in range(20)]#создает список из 20 подсписок в 4 чсила от -10 до 10
for i in range(len(num_list)):#i по длине списка
    for j in range(i, len(num_list)):#j по длине списка
        list.append((num_list[i], num_list[j]))#добавляет в новвй список по индлексу i и j
        comb += 1
        if sum(num_list[i]) + sum(num_list[j]) < main_input:#если сумма < инпута
            index += 1
print(list)
print("-----------------------------")
print("kolvo combination < inputa: ", index)
print("kolvo combination", comb)