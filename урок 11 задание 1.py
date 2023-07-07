def fac(n):
    if n>0:
        if n==1:
            return 1
        else:
            r=1
            for i in range(1,n+1):
                r*=i
            return r
while True:
    m=input('Введите число: ')
    m=int(m)
    if m>0:
        if m==1:
          print(f'{m} и в африке 1')
          break
        else:
            l=fac(m)
            ls=[]
            for i in range(l,1,-1):
                ls.append(fac(i))
            print(ls)
            break
    else:
        print('Число должно быть больше 0')
        continue