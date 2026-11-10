sl = [2,5,8,11,14,18,21,25,30] 
e = 18
l = 0
h = len(sl)-1
w2=-1
while l<=h:
    m = (l+h)//2
    if sl[m] == e:
        w2 = m
        break
    elif sl[m] < e:
        l = m+1
    else:
        h = m-1
if w2 == -1:
    print("-1") 
else:
    print("Индекс элемента: ", w2)