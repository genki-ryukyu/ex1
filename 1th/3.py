w = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'


w1 = w.split()

l = len(w1)
i = 0

list = []




while i<=l-1:
    m = len(w1[i])
    n = str(m)
    list.append(n)
    i += 1


print(list)