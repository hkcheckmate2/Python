def RR(x,y):
    dec = []
    #dec = ""
    a = []
    A = {}
    A = set()
    q = x//y
    r = x%y

    A.add(r)
    a.append(r)
    r = r * 10
    dec.append(r//y)
    #dec += str(r//y)
    r = r % y
    #print(r,a,dec)

    while (r not in A):
        A.add(r)
        a.append(r)
        r = r * 10
        dec.append(r//y)
        #dec += str(r//y)
        r = r % y
        #print(r,a,dec)

    imp = a.index(r)
    l = ""
    #l = str(dec[0:imp])
    for j in range(imp,len(dec)):
        l = l + str(dec[j])
    if imp != 0:
        k = ""
        #k = str(dec[imp:])
        for i in range(0,imp):
            k = k + str(dec[i])
        print(str(q) + '.' + k + '(' + l + ')')
        #print(str(q) + '.' + l + '(' + k + ')')
    else:
        print(str(q) + '.' + '(' + l + ')')
    




