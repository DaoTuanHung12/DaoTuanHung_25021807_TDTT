#drink = [] dau la list
#drink.append("trasua") fake hon insert
#drink.pop(0) xin va ngan hon drink.remove()
#drink.sort() sap xep theo bang chu cai
#drink.clear()
#drink = ["coca","7up"]
#print(drink[0])

#funtion of list

#2d list
#me = ["handsome","tall"]
#you = ["beautiful","smart"]
#us = [me, you]
#us[0] = "coca"
#print(us)

#student = ("dao tuan hung", 18,"male")
#print(student.count(18))
#print(student.index(18))
#for x in student:
#    print(x,end = " ")
#if 18 in student:
#    print("hung is qualified")

#student = list(student)
#student[0] = "hung"
#student = tuple(student)
#print(type(student))

#set
#drink = {"coca","7up","pepsi","pepsi","pepsi","pepsi","pizza" }
#drink.add("sting")
#drink.remove()
#food = {"pizza","steak","candy"}
#drink.update(food)
#consume = drink.union(food)
#for x in consume:
#    print(x, end = " ")
#print(food.difference(drink))
#print(food.intersection(drink))

#line = input("nhap cac gia tri: ")
#a, b = map(int, line.split())
#print(f"{a}^{b} = {a**b}")

#char = input("nhap 1 ki tu: ")
#print(f"{char}: {ord(char)}")
#hoa = ord(char) - 32
#print(f"{chr(hoa)}: {hoa}")

#name = input("nhap ten 3 nguoi: ")
#a, b, c = name.split()
#print(f"hello {c}, {b}, {a}")

#print("hello, world\n"*10)

#gender = {'haianh':'girl',
#          'hung':'boy'}
#gender.update({'huyen':'girl'})
#friend = {'huy':'boy',
#          'long':'gay'}
#gender.update({'huy':'boy'})
#gender.update({'huy':'gay'})
#gender.pop('huy')
#print(gender.keys())
#print(gender['hung'])
#print(gender.get('huyen'))
#print(gender.values())
#print(gender.items())
#for key, val in gender.items():
#    print(key, val)

#x = ['hung'] #list
#print(type(x))

#name = "bro code"
#if (name[0].islower()):
#    name = name.capitalize()
#print(name)
#first_name =  name[0:3].upper()
#last_name = name[4:8].capitalize()
#print(first_name, last_name)
#last_name = name[-1]
#print(last_name)

def wtw(r,f):
    if r:
        if f:
            print("a")
        else:
            print('b')
    else:
        if f:
            print('c')
        else:
            print('d')
wtw(True, False)

n = int(input('nhap vao 1 so nguyen: '))
if n < 0:
    n = -n
n = str(n)
print(f'so chu so la: {len(n)}')
