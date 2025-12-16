#bai1
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
m = []
for i in n:
    if i not in m:
        m.append(i)
print(m)

#bai2
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
m =[]
for i in range(len(n)):
    m.append(sum(n[:i+1]))
print(m)

#bai3
n = tuple(map(int, input('nhap vao cac so nguyen: ').split()))
m = ()
m += n[n[-1]:len(n)-1:]
m += n[:n[-1]:]
print(m)

#bai4
result_dict = {}
n = list(input('nhap vao cac cap key:value cach nhau boi dau cach: ').split())
for i in n:
    key,value = i.split(':')
    if key in result_dict:
        result_dict[key].append(value)
    else:
        result_dict[key] = [value]
print(result_dict)

#bai5
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
m = {'positive':[],'negative':[],'zero':[]}
for i in n:
    if i > 0:
        m['positive'].append(i)
    elif i < 0:
        m['negative'].append(i)
    else:
        m['zero'].append(i)
print(m)

#bai6
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
tong = sum(n)
print(f'tong: {tong}')

#bai7
n = tuple(input('nhap vao 1 tuple: ').split())
m = n[::-1]
print(f'''phan tu dau: {n[0]}
phan tu cuoi: {n[-1]}
tuple dao nguoc: {m}''')

#bai8
n = list(input('nhap vao cac chuoi: ').split())
m = {}
for i in n:
    if i in m.keys():
        continue
    else:
        m[i] = n.count(i)
print(m)

#bai9
n = list(input('nhap vao cac key:value cach nhau boi dau cach cho dictionary thu 1: ').split())
m = list(input('nhap vao cac key:value cach nhau boi dau cach cho dictionary thu 2: ').split())
dict_one = {}
dict_two = {}
for i in n:
    key, value = i.split(':')
    dict_one[key] = [value]
for j in m:
    key, value = j.split(':')
    dict_two[key] = value
for key, value in dict_two.items():
    if key in dict_one.keys():
        dict_one[key].append(value)
    else:
        dict_one[key] = [value]
print(dict_one)

#bai11
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
m = []
l = []
for i in n:
    if i%2==0:
        m.append(i)
    else:
        l.append(i)
m = tuple(m)
l = tuple(l)
print(m)
print(l)

#bai12
n = list(map(int, input('nhap vao cac so nguyen: ').split()))
count = 0
for i in n:
    if n.count(i) > count:
        result = i
        count = n.count(i)
print(f'so xuat hien nhieu nhat: {result}')

#bai13
n = list(input('nhap vao cac key:value cach nhau boi dau cach cho dictionary: ').split())
dict_one = {}
for i in n:
    key, value = i.split(':')
    dict_one[value] = key

#bai14 
n = list(map(int, input('nhap vao cac so nguyen cho danh sach 1: ').split()))
m = list(map(int, input('nhap vao cac so nguyen cho danh sach 2: ').split()))
dupe = []
for i in n:
    if i in m and i not in dupe:
        dupe.append(i)
print(dupe)

#bai15
n = list(input('nhap vao cac key:value voi key la 1 str, value la 1 so nguyen cach nhau boi dau cach: ').split())
m  = int(input('nhap vao 1 so nguyen k: '))
result = {}
for i in n:
    key, value = i.split(':')
    if int(value) > m:
        result[key] = int(value)
print(result)

#bai1
n = int(input('nhap vao n hang: '))
m = int(input('nhap vao m cot: '))
l = []
count = 0
for i in range(m*n):
    l.append(int(input(f'nhap vao phan tu thu {i+1}: ')))
for i in range(n):
    for j in range(m):
        print(f'{l[count]}',end = ' ')
        count += 1
    print()

#bai2
n = int(input('nhap vao n hang,cot: '))
m = n
l = []
count = 0
for i in range(m*n):
    l.append(int(input(f'nhap vao phan tu thu {i+1}: ')))
for i in range(n):
    for j in range(m):
        print(f'{l[count]}',end = ' ')
        count += 1
    print()
print('duong cheo chinh:',end = ' ')
for i in range(0,len(l),n+1):
    print(l[i],end = ' ')
print()
print('duong cheo phu:',end = ' ')
for i in range(n-1,len(l)-1,n-1):
    print(l[i],end = ' ')