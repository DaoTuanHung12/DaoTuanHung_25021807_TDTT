import math
#bai 2
flag = True
while flag:
 n = int(input('nhap vao 1 so nguyen duong: '))
 if n <= 0:
    print('day khong phai la 1 so nguyen duong')
 elif n > 0:
    flag = False
if n == 1:
  print('1 khong phai so nguyen to')
else:
  for i in range(2,math.isqrt(n)+1):
    if n%i == 0:
       print(f'{n} khong phai so nguyen to')
  else:
       print(f'{n} la so nguyen to')

#bai 3
def prime(num):
   if n <= 2:
      return False
   for i in range(2, math.isqrt(num)+1):
      if num%i == 0:
         return False
   return True
      
num = int(input('nhap vao 1 so nguyen duong: '))
for i in range(math.isqrt(num)+1, num+1,-1):
   if num%i == 0 and prime(i):   
      print(i)
      break

#bai 4
def prime(num):
   if num < 2:
      return False
   for i in range(2, math.isqrt(num)+1):
      if num%i == 0:
         return False
   return True

s = 0      
num = int(input('nhap vao 1 so nguyen duong: '))
for i in range(1, num+1):
   if num%i == 0 and prime(i):   
      s = i
print(s)

#bai 5
x = int(input('nhap vao 1 so nguyen: '))
num = 0
o = 0
flag = True
while flag:
    o = int(str(x)[::-1])
    if x != o:
        x += o
        num += 1
    else:
        flag = False
        print(f'''so palindrome la: {x}
so lan cong la: {num}''')