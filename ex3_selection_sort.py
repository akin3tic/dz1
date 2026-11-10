l = [29, 10, 14, 37, 13]
print("Начальный список: ")
print(l)
print()
for j in range(len(l)):
    min=j
    for k in range(j+1,len(l)):
        if l[k]<l[min]:
            min=k
    if min != j:
        l[j],l[min]=l[min],l[j]
    print(l)
    print()
print("Отсортированный список выбором: ")
print(l)
