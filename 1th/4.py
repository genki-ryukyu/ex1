w = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

w1 = w.split()

l = len(w1)
i = 0

list = []


while i<=l-1:
    m = w1[i]
    n = m[0]
    
    m1 = w1[i+1]
    n2 = m1[1]
    list.append(n)
    list.append(n2)
    i += 2
    


list1 = []


i = 0
while i<=l-1:
    n = 1
    n2 = 2
    list1.append(n)
    list1.append(n2)
    i += 2



i = 0

dict1 = dict(zip(list, list1))
print(dict1)
    
