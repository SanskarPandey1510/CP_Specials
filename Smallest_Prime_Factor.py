# For every inter i in range(n) compute smallest prime factor of i
# Smallest_Prime_Factor(1)=1
# Smallest_Prime_Factor(2)=2
# Smallest_Prime_Factor(3)=3
# Smallest_Prime_Factor(4)=2
# Smallest_Prime_Factor(5)=5
# Smallest_Prime_Factor(6)=2
# Smallest_Prime_Factor(7)=7
# Smallest_Prime_Factor(8)=2
# Smallest_Prime_Factor(9)=3
# Smallest_Prime_Factor(10)=2
# Smallest_Prime_Factor(11)=11
# Smallest_Prime_Factor(12)=2
# Smallest_Prime_Factor(13)=13
# etc.
# The smallest prime factor of a number n is the smallest prime number that divides n.
n=10**5
spn=[i for i in range(n+1)]
# spn list contains smallest prime factor of i
# if spn[i]=i then i is prime
for i in range(2,n+1):
    if spn[i]==i:
        # i is prime
        # all the multiples of i can have i as their smallest prime factor
        # if spn[j]=j then j is prime
        # so we can assign spn[j]=i
        # if spn[j] is not prime (spn[j]!=j) then we can not assign spn[j]=i
        # because we have already assigned a smaller prime factor to j
        for j in range(i*i,n+1,i):
            if spn[j]==j:
                spn[j]=i
# Time complexity of this algorithm is O(nloglogn)


# We can get prime factorization of a number using this spn(smallest prime number) list
num=1000
factors=[]
while num>1:
    factors.append(spn[num])
    num//=spn[num]
# factors will contain all the prime factors of num
# factors=[2,5,5]
# Time complexity of this algorithm is O(logn)
