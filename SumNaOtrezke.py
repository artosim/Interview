"""Множество с запросами суммы на отрезке

Реализуйте структуру данных для хранения множества целых чисел, поддерживающую запросы добавления, удаления, поиска, а также
суммы на отрезке. На вход в данной задаче будет дана последовательность таких запросов. Чтобы гарантировать, что ваша
программа обрабатывает каждый запрос по мере поступления (то есть онлайн),
каждый запрос будет зависеть от результата выполнения одного из предыдущих запросов.
Если бы такой зависимости не было, задачу можно было бы решить оффлайн: сначала прочитать весь вход и
сохранить все запросы в каком-нибудь виде, а потом прочитать вход ещё раз, параллельно отвечая на запросы.

Формат входа.
Изначально множество пусто. Первая строка содержит число запросов n. Каждая из n следующих строк содержит
запрос в одном из следующих четырёх форматов:
• + i: добавить число f (i) в множество (если оно уже есть, проигнорировать запрос);
• - i: удалить число f (i) из множества (если его нет, проигнорировать запрос);
• ? i: проверить принадлежность числа f (i) множеству;
• s l r: посчитать сумму всех элементов множества, попадающих в отрезок [f (l), f (r)].
Функция f определяется следующим образом. Пусть s — результат последнего запроса суммы на отрезке (если таких запросов
ещё не было, то s = 0). Тогда
f (x) = (x + s) mod 1 000 000 001 .

Формат выхода.
Для каждого запроса типа ? i выведите «Found» или «Not found». Для каждого запроса суммы выведите сумму
всех элементов множества, попадающих в отрезок [f (l), f (r)]. Гарантируется, что во всех тестах f (l) ≤ f (r).

Sample Input:
15
? 1
+ 1
? 1
+ 2
s 1 2
+ 1000000000
? 1000000000
- 1000000000
? 1000000000
s 999999999 1000000000
- 2
? 2
- 0
+ 9
s 0 9

Sample Output:
Not found
Found
3
Found
Not found
1
Not found
10
"""

def zig(u):# Если отец u - корень, и u левый сын отца
    a = Parrents[u] #Отец
    b = Parrents[Parrents[u]] # Дед
    r = Rights[u] # Правый сын
    Parrents[u], Rights[u], Lefts[a], Parrents[a] = b, a, r, u
    if r != -1:
        Parrents[r] = a
    Summarize(a)
    Summarize(u)

def zag(u): # Если отец u - корень, и u правый сын отца
    a = Parrents[u] #Отец
    b = Parrents[Parrents[u]] # Дед
    l = Lefts[u] # левый сын
    Parrents[u], Lefts[u], Rights[a], Parrents[a] = b, a, l, u
    if l != -1:
        Parrents[l] = a
    Summarize(a)
    Summarize(u)

def zigzig(u): # u левый сын своего отца, отец u - не корень, отец u - левый сын деда u
    a = Parrents[u] # Отец
    b = Parrents[a] # Дед
    c = Parrents[b] # Прадед
    r = Rights[u] # Правый сын
    ra = Rights[a] # Правый сын отца
    if c != -1:
        if Lefts[c] == b:
            Lefts[c] = u
        elif Rights[c] == b:
            Rights[c] = u
    Parrents[u], Rights[u], Parrents[a], Lefts[a], Rights[a], Parrents[b], Lefts[b] = c, a, u, r, b, a, ra
    if r != -1:
        Parrents[r] = a
    if ra != -1:
        Parrents[ra] = b
    Summarize(b)
    Summarize(a)
    Summarize(u)
    Summarize(c)

def zigzag(u): # u левый сын своего отца, отец u - не корень, отец u - правый сын деда u
    b = Parrents[u] #Отец
    a = Parrents[b] #Дед
    c = Parrents[a] #Прадед
    l = Lefts[u] #Левый сын
    r = Rights[u] #Правый сын
    if c != -1:
        if Lefts[c] == a:
            Lefts[c] = u
        elif Rights[c] == a:
            Rights[c] = u
    Parrents[u], Lefts[u], Rights[u], Parrents[b], Lefts[b], Parrents[a], Rights[a] = c, a, b, u, r, u, l
    if l != -1:
        Parrents[l] = a
    if r != -1:
        Parrents[r] = b
    Summarize(a)
    Summarize(b)
    Summarize(u)
    Summarize(c)

def zagzag(u): # u правый сын своего отца, отец u - не корень, отец u - правый сын деда u
    a = Parrents[u] # Отец
    b = Parrents[a] # Дед
    c = Parrents[b] # Прадед
    l = Lefts[u] # Левый сын
    la = Lefts[a] # Левый сын отца
    if c != -1:
        if Lefts[c] == b:
            Lefts[c] = u
        elif Rights[c] == b:
            Rights[c] = u
    Parrents[u], Lefts[u], Parrents[a], Lefts[a], Rights[a], Parrents[b], Rights[b] = c, a, u, b, l, a, la
    if l != -1:
        Parrents[l] = a
    if la != -1:
        Parrents[la] = b
    Summarize(b)
    Summarize(a)
    Summarize(u)
    Summarize(c)

def zagzig(u): # u правый сын своего отца, отец u - не корень, отец u - левый сын деда u
    a = Parrents[u] # Отец
    b = Parrents[a] # Дед
    c = Parrents[b] # Прадед
    l = Lefts[u] #Левый сын
    r = Rights[u] # Правый сын
    if c != -1:
        if Lefts[c] == b:
            Lefts[c] = u
        elif Rights[c] == b:
            Rights[c] = u
    Parrents[u], Lefts[u], Rights[u], Parrents[a], Rights[a], Parrents[b], Lefts[b] = c, a, b, u, l, u, r
    if l != -1:
        Parrents[l] = a
    if r != -1:
        Parrents[r] = b
    Summarize(b)
    Summarize(a)
    Summarize(u)
    Summarize(c)

def Splay(u): # пока u не корень, будут производиться вращения, взависимости от положения, кто чей сын
    while Parrents[u] != -1:
        if Lefts[Parrents[u]] == u:
            if Parrents[Parrents[u]] != -1:
                if Lefts[Parrents[Parrents[u]]] == Parrents[u]:
                    zigzig(u)
                else:
                    zigzag(u)
            else:
                zig(u)
        elif Rights[Parrents[u]] == u:
            if Parrents[Parrents[u]] != -1:
                if Rights[Parrents[Parrents[u]]] == Parrents[u]:
                    zagzag(u)
                else:
                    zagzig(u)
            else:
                zag(u)
    global koren
    koren = u # u при использовании Splay всегда будет корнем

def Search(i, k): # Поиск ключа k, в дереве с корнем i
    if i == -1:
        return -1
    else:
        while True == True :
            if Keys[i] == k:
                Splay(i)
                return i
            elif (Keys[i] > k) and (Lefts[i] != -1):
                i = Lefts[i]
            elif (Keys[i] < k) and (Rights[i] != -1):
                i = Rights[i]
            else:
                Splay(i)
                return -1

def Insert(i, k): # Вставка ключа k, в дерево с корнем i
    if i == -1:
        Keys.append(k)
        Parrents.append(-1)
        Lefts.append(-1)
        Rights.append(-1)
        Sum.append(k)
        Splay(len(Keys)-1) # Добавили вершину, которая является деревом и в нем она корень
    else:
        while True == True : # Поиск места куда вставить k
            if Keys[i] == k:
                Splay(i)
                return
            elif (Keys[i] > k) and (Lefts[i] != -1):
                i = Lefts[i]
            elif (Keys[i] < k) and (Rights[i] != -1):
                i = Rights[i]
            else:
                Keys.append(k)
                new_i = len(Keys) - 1
                Parrents.append(-1)
                Lefts.append(-1)
                Rights.append(-1)
                Sum.append(k)
                if Keys[i] > k:
                    Lefts[i] = new_i
                    Parrents[new_i] = i
                else:
                    Rights[i] = new_i
                    Parrents[new_i] = i
                Splay(new_i) # В результате корнем будет new_i
                return

def Split(i, k): # Делит дерево по ключу k на два дерева. Возвращает индексы корней деревьев, если какого-либо дерева нет, возвращает -1
    if i == -1:
        v1 = -1
        v2 = -1
        return v1, v2
    else:
        Search(i, k)
        if Keys[koren] <= k:
            v1 = koren
            v2 = Rights[koren]
            if v2 != -1:
                Parrents[v2], Rights[koren] = -1, -1
            Summarize(koren)
            return v1, v2
        else:
            v1 = Lefts[koren]
            v2 = koren
            if v1 != -1:
                Parrents[v1], Lefts[koren] = -1, -1
            Summarize(koren)
            return v1, v2

def Max(v): # Поиск максимума в вершине
    while Rights[v] != -1:
        v = Rights[v]
    return v

def Merge(v1, v2): # Объединение двух деревьев, на вход подаются корни, выход: корень дерева
    u = Max(v1)
    Splay(u) #Вершина с максимальным значением в v1 будет корнем
    Rights[u] = v2
    Parrents[v2] = u
    Summarize(u)
    return u

def Remove(u): # Удаление вершины
    global koren
    Splay(u) #Корнем дерева будет вершина u
    if (Lefts[u] == -1) and (Rights[u] == -1):
        koren = -1 # Если удалим вершину без сыновей, то дерева не будет => корня не будет
    elif Lefts[u] == -1: # Если у вершины не было левого сына, то при удалении корнем будет правый сын
        Parrents[Rights[u]] = -1 # и не забываем убрать родителя у корня
        Splay(Rights[u])
    elif Rights[u] == -1: # аналогично, если не было правого сына
        Parrents[Lefts[u]] = -1
        Splay(Lefts[u])
    else: # Если оба сына были
        Merge(Lefts[u], Rights[u]) # объединим их, в результате корнем будет левый сын
    Parrents[u], Lefts[u], Rights[u] = -1, -1, -1 # убрали все связи с удаленной вершиной

def Summarize(u): # Подсчет суммы
    Sum[u] = Keys[u]
    if Lefts[u] != -1:
        Sum[u] += Sum[Lefts[u]]
    if Rights[u] != -1:
        Sum[u] += Sum[Rights[u]]
    return Sum[u]

def Sumlr(l, r): # Подсчет суммы на отрезке, делим дерево, по ключу l-1, затем правое дерево по ключу r, ответом будет поле суммы среднего дерева
    v1, v2 = Split(koren, l-1)
    if v2 == -1:
        answer = 0
        return answer
    Splay(v2)
    v2, v3 = Split(koren, r)
    if v2 == -1:
        answer = 0
    else:
        answer = Sum[v2]
    if v1 != -1:
        if v2 != -1:
            v1 = Merge(v1, v2)
        if v3 != -1:
            v1 = Merge(v1, v3)
    else:
        if (v2 != -1) and (v3 != -1):
            v2 = Merge(v2, v3)
    return answer

def f(x): # Условие задачи
    return (x + s) % 1000000001
# Наше дерево, где у элемента i есть: его ключ, индекс левого сына,
# индекс правого сына и индекс родителя и поле суммы. Parrents со значением -1 это корень
Keys = []
Parrents = []
Lefts = []
Rights = []
Sum = []

koren = -1
s = 0
n = int(input()) #Кол-во запросов
for x in range(n):
    In = list(map(str, input().split()))
    if In[0] == '+':
        Insert(koren, f(int(In[1])))
    elif In[0] == '-':
        index_to_delete = Search(koren, f(int(In[1])))
        if index_to_delete != -1:
            Remove(koren)
    elif In[0] == '?':
        index_to_find = Search(koren, f(int(In[1])))
        if index_to_find == -1:
            print('Not found')
        else:
            print('Found')
    elif In[0] == 's':
        s = Sumlr(f(int(In[1])), f(int(In[2])))
        print(s)
