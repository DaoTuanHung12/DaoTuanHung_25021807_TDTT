#bai1
def binary_search(arr, x):
    return arr.index(x) if x in arr else -1

#bai2
def count_time(arr, x):
    return arr.count(x)

#bai3
def bubble_sort(x):
        for i in range(len(x)):
             flag = False
             for j in range(len(x)-i-1):
                  if x[i] > x[i+1]:
                       x[i],x[i+1] = x[i+1],x[i]
                       flag = True
                       if not flag:
                            break
        return x

def selection_sort(x):
     for i in range(len(x)):
          minidx = i
          for j in range(i+1,len(x)):
               if x[j] < x[minidx]:
                    minidx = j
          x[i],x[minidx] = x[minidx],x[i]
     return x

#bai4
def count_max(x):
     maxcount = 0
     for i in x:
          if x.count(i) > maxcount:
               maxcount = x.count(i)
     return maxcount

#bai5
def tongcantim(arr,x):
     ketqua = 0
     for i in range(len(arr)):
          for j in range(i+1,len(arr)):
               if arr[i] + arr[j] == x:
                    ketqua += 1
     return ketqua

#bai6
def lamphanglist(x):
     ketqua = []
     for i in x:
          for j in i:
               ketqua.append(j)
     return ketqua

def dddctnnn(x):
    l = [1]*len(x)
    for i in range(1,len(x)):
         for j in range(i):
              if x[i] > x[j] and l[i] < l[j] + 1:
                   l[i] = l[j] + 1
    return l.index(max(l)) - 1

print(dddctnnn([0,1,0,3,2,3]))




