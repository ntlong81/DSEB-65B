def STgcdr(a,b):
    if a<b:
        a,b =b,a 
    if b==0:
        s=1
        t=0
        return a, s, t
    gcd,s1,t1 = STgcdr(b, a%b)
    s = t1
    t = s1-t1*(a//b)
    return gcd,s,t
def gcd(a,b):
    if a<b:
        a,b = b,a
    while b !=0:
        r = a%b
        a = b
        b = r
    return a 
print('Our_module is imported')