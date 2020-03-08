INPUT
3
hrrkhceaate
OUTPUT
hackerearth
INPUT
1
ctosnet
OUTPUT
contest


n=int(input())//number input
s=input()//string input

while n:
    l2 = ""//empty string
    l3 = ""
    for i in range(len(s)):
        if i % 2 == 0://if even add to l2
            l2 += s[i]
        else://adding to l3
            l3 += s[i]
    l3 = l3[::-1]//making l3 reverse
    n=n-1
    s = l2 + l3//changing string
print(s)



