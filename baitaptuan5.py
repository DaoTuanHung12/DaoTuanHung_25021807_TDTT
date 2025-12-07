import math
#bai1
def max_of_two_numbers(a,b):
    if a > b:
        print(a)
    else:
        print(b)

max_of_two_numbers(20,10)

#bai 2
def swap(a,b):
      return b,a
print(type(swap(1,2)))

#bai3
def prime(num):
    if num <=2:
        return False
    for i in range(2, math.isqrt(num)+1):
        if num%i == 0:
            return False
    return True
print(prime(11))

#bai4
def perfect_number(n):
    s = 0 
    for i in range(1,math.isqrt(n)+1):
        if i**2 == n:
            s += i
        elif n%i == 0 and i**2 != n:
            s += i 
            s += n/i
    return s/n == 2
print(perfect_number(6))

#bai 5
def find(num, target):
    for i in num:
        if i == target:
            return num.index(i)
    return -1

print(find([1,2,3,4,5,6,7,8,9,0], 11))

#bai 6
def factorial(n):
 if n == 0:
     return 1
 return n*factorial(n-1)
print(factorial(5))

#bai7
def cal(a,b,c):
 match b:
    case '+':
         print(f'{(a+c):.2f}') 
    case '-':
         print(f'{(a-c):.2f}')
    case '/':
         print(f'{(a/c):.2f}')
    case '*':
         print(f'{(a*c):.2f}')

cal(5,'*',3)

#bai 8
def hamming(a,b):
 count = 0
 flag = True
 glag = True
 hama = []
 hamb = []
 while flag:
     if a%2 == 0:
         hama.append(0)
         a = a//2
     if a == 1:
         hama.append(1)
         flag = False 
     if a%2 == 1:
         hama.append(1)
         a = a//2 
 while glag:
     if b%2 == 0:
         hamb.append(0)
         b = b//2
     if b == 1:
         hamb.append(1)
         glag = False
     if b%2 == 1:
         hamb.append(1)
         b = b//2
 hama = hama[::-1]
 hamb = hamb[::-1] 
 if len(hama) < len(hamb):
     count = len(hamb) - len(hama)
     for i in range(len(hama)):
         if hama[i] != hamb[i]:
          count += 1
 else:
     count = len(hama) - len(hamb)
     for i in range(len(hamb)):
         if hama[i] != hamb[i]:
          count += 1
 return count
print(hamming(1,4))