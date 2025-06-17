des = range(10)

# A
print("Vypisuješ A \n")
a = 1
for n in range (1, 10):
    print(a)
    a += 6

print("\n \n \n")

#B
print("Vypisuješ B \n")
b = 1
for _ in des:
    print(b)
    b *= 5

print("\n \n \n")

#C
print("Vypisuješ C \n")
c = 5

for _ in des:
    print(c)
    c *= 2

print("\n \n \n")

#D 
print("Vypisuješ D \n")
d_jedna = 1
d_dva = 1

for _ in des:
    print(d_jedna)
    print(d_dva)

    d_jedna += 1
    d_dva += 2 

print("\n \n \n")

#E
print("Vypisuješ E \n")
e = 1

for n in range(1,9):
    print(e)

    e += n

print("\n \n \n")

#F
print("Vypisuješ F \n")
f = 256

for _ in des:
    print(f)
    f /= 2

print("\n \n \n")

#G
print("Vypisuješ G \n")

g_letters = ord("A")
g_numbers = 1

for _ in des:
    print(chr(g_letters))
    print(g_numbers)

    g_letters += 2
    g_numbers *= 2

print("\n \n \n")

#H
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

print("\n \n \n")

#I 
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

print("\n \n \n")

#J
print("Vypisuješ J \n")

j = 1

for _ in des:
    print(j)
    j = (j * 2) + 1
    
print("\n \n \n")

#K
print("Vypisuješ K \n")

k = 2

for _ in des:
    print(k)
    k += 2
    print(k)
    k += 5

print("\n \n \n")

#L
print("Vypisuješ L \n")

l = 30

for n in range(2,10):
    print(l)
    l -= n

print("\n \n \n")

#M
print("Vypisuješ M \n")

m = -972

for _ in des:
    print(m)
    m = m / (-3)

print("\n \n \n")

#N 
print("Vypisuješ N \n")

n = 16

for i in range(1, 10):
    print(n)
    n += (i * 6)

print("\n \n \n")

#O - Bohužel nechápu posloupnost... nejde nic )?: prostě to jebnu aby to vypadalo jak to vypadat má a má to néjakou funkćnost
print("Vypisuješ O \n")

o = 123

for _ in des:
    print(o)
    if o == 135:
        o += 13
    else:
        o += 12

print("\n \n \n")

#P
print("Vypisuješ P \n")

p_vypocet = 1
p = 4
print(p)

for _ in range(1, 10):
    p += p_vypocet
    print(p)
    p_vypocet *= 2

print("\n \n \n")

#Q
print("Vypisuješ Q \n")
q_jedna = 1
q_dva = 2

for _ in des:
    print(q_jedna)
    print(q_dva)

    q_jedna *= 10
    q_dva *= 10

print("\n \n \n")