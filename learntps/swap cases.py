s = raw_input()
l = list(s)
l1 = []

f = 0
f1 = 0
for i in l:

    if i.isalpha():
        f = 1
        if i.isupper():
            f1 = 1
            l1.append(i.lower())

        else:
            l1.append(i.upper())

ss = "".join(l1)
print ss