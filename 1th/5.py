


def ngram(w, i):
    w1 = w.split()
    n = 0
    list =[]
    l = len(w1)
    while n <= l-i:
        list.append(w1[n:n+i])
        n += 1
    print("単語")
    print(list)
    
    
def wgram(w, i):
    w1 = w.replace(' ', '')
    n = 0
    list =[]
    l = len(w1)
    while n <= l-i:
        list.append(w1[n:n+i])
        n += 1
    print("文字")
    print(list)
    

    
w = 'I am an NLPer'
wgram(w, 2)
ngram(w, 2)