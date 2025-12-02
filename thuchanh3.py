#bai3
#a,b,c = map(float, input('nhap vao do dai 3 canh: ').split())
#if a+b>c and a+c>b and b+c>a:
#    print('day la 1 tam giac')
#else:
#    print('day khong phai 1 tam giac')

#bai1
#a,b = map(float, input('nhap vao chieu rong, chieu dai lan luot:').split())
#print(f'''dien tich hcn la: {(a*b}
#chu vi hcn la: {(a+b)*2}''')

#bai2
#import math
#r = float(input('nhap ban kinh hinh tron: '))
#print(f'''chu vi hinh tron la: {2*math.pi*r:.2f}
#dien tich hinh tron la: {(r**2)*math.pi:.2f}''')

#bai4
#a,b = map(float, input('nhap 2 gia tri a va b lan luot cho pt ax+b=0: ').split())
#print(f'nghiem cua phuong trinh la: x = {-b/a:.2f}')

#bai5
#import math
#a,b,c = map(float, input('nhap lan luot a,b,c cho pt ax**2+bx+c=0: ').split())
#d = b**2-a*4*c
#if d <0:
#    print('pt vo nghiem')
#if d ==0:
#    print(f'pt co nghiem kep: x = {-b/(a*2):.2f}')
#if d >0:
#    print(f'pt co 2 nghiem pb: x1 = {(-b-math.sqrt(d))/(a*2):.2f}, x2 = {(-b+math.sqrt(d))/(a*2):.2f}')

#bai6
#a,b,c,d = map(float, input('nhap 4 so bat ki: ').split())
#print(f'so lon nhat la: {max(a,b,c,d)}')

#bai7
#a,b,c,d = map(float, input('nhap 4 so bat ki: ').split())
#print(f'so nho nhat la: {min(a,b,c,d)}')

#bai8
#a,b,c,d,m,n = map(float, input('nhap lan luot 6 so a,b,c,d,m,n cho he pt 2 an co dang ax+b=m va cx+d= n: ').split())
#if a*d-b*c ==0:
#    if a/c == m/n:
#        print('he pt co vo so nghiem')
#    else:
#        print('he pt vo nghiem')
#else:
#    x = (m*d-b*n)/(a*d-b*c)
#    y = (a*n-m*c)/(a*d-b*c)
#    print(f'he pt co nghiem duy nhat: x = {x:.2f}, y = {y:.2f}')

#bai9
#a = int(input('nhap vao so giay: '))
#h = a//3600
#b = a-h*3600
#m= b//60
#c = b-m*60
#s= c
#print(f'thoi gian la: {h}h{m}m{s}s')

#bai10
#a,b = map(float, input('nhap vao toa do tam I(a,b): ').split())
#r = float(input('nhap vao ban kinh r: '))
#x,y = map(float, input('nhap vao 1 diem A(x,y) bat ki: ').split())
#if (x-a)**2 + (y-b)**2 == r**2:
#    print(f'A thuoc duong tron tam I ban kinh {r}')
#else:
#    print(f'A khong thuoc duong tron tam I ban kinh {r}')

#bai11
#x,y = map(float, input('nhap vao 2 so thuc x va y bat ki: ').split())
#print(f'x^y = {x**y}')