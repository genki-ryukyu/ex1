W0 = "paraparaparadise"
W1 = "paragraph"

def wgram(w, i):
    w1 = w.replace(' ', '')
    n = 0
    list =[]
    l = len(w1)
    while n <= l-i:
        list.append(w1[n:n+i])
        n += 1
    return list



X = set(wgram(W0,2))
print(X)
Y = set(wgram(W1,2))
print(Y)

#和集合
Z = X | Y
print(Z)

#積集合
Z1 = X & Y
print(Z1)

#差集合
Z2 = X - Z1
print(Z2)

X = list(X)
Y = list(Y)

if X.count("se")>0:
    print("Xには含まれている")
else:
    print("Xには含まれていない")
    
if Y.count("se")>0:
    print("Yには含まれている")
else:
    print("Yには含まれていない")


    


    

