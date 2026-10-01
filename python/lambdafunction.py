'''a = lambda n:n*n
print(a(5))

b = lambda a,c:a+c
print(b(2,3))

c = lambda a:a%2==0
print(c(3))

d = lambda w,e:w>e or e>w
print(d(3,4))

#recursive functions
def fact(n):
    if n ==0:
        return 1
    else:
        result=n*fact(n-1)
        return result
print(fact(5))'''

def fact(n):
    result = 1
    while n>=1:
        result = result*n
        n = n-1
        return result

def palindrome(s):
    if s==s[::-1]:
        return 'palindrome'
    else:
        result = "not a palindrome"
        return result
print(palindrome('dad'))
    