des = range(10) # Každá 10 range = des

def A():
    print("Vypisuješ A \n")

    a = 1
    for _ in des:
        print(a)
        a += 6

def B():
    print("Vypisuješ B \n")

    b = 1
    for _ in des:
        print(b)
        b *= 5

def C():
    print("Vypisuješ C \n")

    c = 5
    for _ in des:
        print(c)
        c *= 2

def D():
    print("Vypisuješ D \n")

    d_jedna = 1
    d_dva = 1
    for _ in des:
        print(d_jedna)
        print(d_dva)
        d_jedna += 1
        d_dva += 2 

def E():
    print("Vypisuješ E \n")

    e = 1
    for n in des:
        print(e)
        e += n

def F():
    print("Vypisuješ F \n")

    f = 256
    for _ in des:
        print(f)
        f /= 2

def G():
    print("Vypisuješ G \n")

    g_letters = ord("A")
    g_numbers = 1
    for _ in des:
        print(chr(g_letters))
        print(g_numbers)
        g_letters += 2
        g_numbers *= 2

def H():
    print("Vypisuješ H \n")

    h_jedna = 1
    h_dva = 1
    print(h_jedna)
    print(h_dva)
    for _ in des:
        c = h_jedna + h_dva
        print(c)
        h_jedna = h_dva
        h_dva = c


def I():
    print("Vypisuješ I \n")

    i_a = 1
    i_b = 1
    i_c = 1
    for _ in des:
        print(i_a)
        print(i_b)
        print(i_c)
        i_a += 1
        i_b *= 2
        i_c += 2

def J():
    print("Vypisuješ J \n")

    j = 1
    for _ in des:
        print(j)
        j = (j * 2) + 1

def K():
    print("Vypisuješ K \n")

    k = 2
    for _ in des:
        print(k)
        k += 2
        print(k)
        k += 5

def L():
    print("Vypisuješ L \n")

    l = 30
    for n in range(2,10):
        print(l)
        l -= n

def M():
    print("Vypisuješ M \n")

    m = -972
    for _ in des:
        print(m)
        m = m / (-3)

def N():
    print("Vypisuješ N \n")

    n = 16
    for i in range(1, 10):
        print(n)
        n += (i * 6)

#O - Bohužel nechápu posloupnost... nejde nic )?: prostě to jebnu aby to vypadalo jak to vypadat má a má to néjakou funkćnost
def O():
    print("Vypisuješ O \n")

    o = 123
    for _ in des:
        print(o)
        o += 13 if o == 135 else 12

def P():
    print("Vypisuješ P \n")

    p_vypocet = 1
    p = 4
    print(p)
    for _ in range(1, 10):
        p += p_vypocet
        print(p)
        p_vypocet *= 2

def Q():
    print("Vypisuješ Q \n")

    q_jedna = 1
    q_dva = 2
    for _ in des:
        print(q_jedna)
        print(q_dva)
        q_jedna *= 10
        q_dva *= 10


# Běh celé aplikace. Celkem clean

for run in [
    A,B,C,D,E,F,G,H,I,J,K,K,M,N,I,O,Q
]:
    run()
    print("\n" + "-"*30 + "\n")
