# n = int(input())
def evenodd(s):
    e = ''
    o = ''
    for i in range(len(s)):
        if i % 2 == 0:
            e += s[i]
        else:
            o += s[i]
    return e + '  ' + o


n = int(input())
for i in range(n):
    s = input()
    op = evenodd(s)
    print(op)
