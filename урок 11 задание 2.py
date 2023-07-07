pets={}
index={}
def find_index(name_p, name_v):
    n=len(index)
    r = -1
    for k,v in index.items():
        if (name_p in v) and (name_v in v):
            r=k
    return r

def add_index(name_p, name_v):
    index_name_pv=find_index(name_p, name_v)
    if index_name_pv==-1:
        index[len(index)]=[name_p, name_v]
        return True
    else:
        return False

def del_index(x):
    if index.get(x, -1)!=-1:
        index.pop(x)
        return True
    else:
        return False

def update_index(name_p, name_v,  new_name_p='', new_name_v=''):
    temp_index=find_index(name_p, name_v)
    r=[False, False]
    if temp_index!=-1:
        temp = index[temp_index]
        if new_name_p!='':
            temp[temp.index(name_p)]=new_name_p
            r[0]=True
        if new_name_v!='':
            temp[temp.index(name_v)] = new_name_v
            r[1] = True
    return r


def get_suffix(age):
    god = str(age)
    r=''
    n = len(god)
    v = ['год', 'года', 'лет']
    if n == 1:
        temp = int(god)
    if n == 2:
        temp = int(god[1])
    if n == 3:
        temp = int(god[2])
    if temp == 1:
        r = v[0]
    if temp in [2, 3, 4]:
        r = v[1]
    if temp in range(5, 10):
        r = v[2]
    return r
def create(ls_in):
    name_p=ls_in[1]
    name_v=ls_in[3]
    ls_in[2]=int(ls_in[2])
    if add_index(name_p, name_v):
        temp={}
        temp['Вид питомца']=ls_in[0]
        temp['Имя питомца'] = ls_in[1]
        temp['Возраст питомца'] = ls_in[2]
        temp['Имя владельца'] = ls_in[3]
        pets[len(pets)]=temp
        return True
    else:
        return False
def read(ls_in):
    n=len(ls_in)
    if n==2:
        name_p = ls_in[0]
        name_v = ls_in[1]
        resp = find_index(name_p, name_v)
        if resp == -1:
            return -1
        else:
            temp = pets[resp]
            x = get_suffix(temp['Возраст питомца'])
            return f'Это {temp["Вид питомца"]} по кличке "{temp["Имя питомца"]}". Возраст питомца: {temp["Возраст питомца"]} {x}. Имя владельца: {temp["Имя владельца"]}'
    if ls_in=='всё':
        r_ls=[]
        for k,temp in pets.items():
            x = get_suffix(temp['Возраст питомца'])
            r_ls.append(f'Это {temp["Вид питомца"]} по кличке "{temp["Имя питомца"]}". Возраст питомца: {temp["Возраст питомца"]} {x}. Имя владельца: {temp["Имя владельца"]}\n')
        return r_ls
#name_p, name_v, new_name_p, new_name_v, new_age, new_vid_p
def update(ls_in):
    if len(ls_in)<=2:
        return False
    else:
        name_p = ls_in[0].strip()
        name_v = ls_in[1].strip()
        resp=find_index(name_p,name_v)
        if resp==-1:
            return False
        else:
            temp_pets=pets[resp]
            for v in ls_in:
                if '=' in v:
                    temp01=v.split('=')
                    if (temp01[0]=='новое имя питомца') and (update_index(name_p,name_v,temp01[1]),''):
                        temp_pets['Имя питомца']=temp01[1]
                    if (temp01[0]=='новое имя владельца') and update_index(name_p,name_v,'',temp01[1]):
                        temp_pets['Имя владельца']=temp01[1]
                    if temp01[0]=='новый возраст питомца':
                        temp_pets['Возраст питомца']=int(temp01[1])
                    if temp01[0]=='новый вид питомца':
                        temp_pets['Вид питомца']=temp01[1]
            pets[resp]=temp_pets
            return True
def delete(ls_in):
    name_p=ls_in[0]
    name_v=ls_in[1]
    resp=find_index(name_p,name_v)
    if resp!=-1:
        pets.pop(resp)
        del_index(resp)
        return True
    else:
        return False
while True:
    print('Введите команду: ')
    print('Создать запись(1): ')
    print('Прочитать запись(2): ')
    print('Обновить запись(3): ')
    print('Удалить запись(4): ')
    print('Выйти из программы(stop/стоп): ')
    komanda=input()
    if (komanda=='stop') or (komanda=='стоп'):
        break
    if komanda=='1':
        print('Введите (вид питомца, имя питомца, возраст питомца, имя владельца )')
        ls_in=[s.strip() for  s in input().split(',')]
        if len(ls_in)==4:
            resp=create(ls_in)
            if resp:
                print('Запись успешно создана!')
            else:
                print('Создать запись не удалось!')
        else:
            continue
    if komanda=='2':
        print('Введите имя питомца и имя владельца(имя питомца, имя владельца)')
        ls_in = [s.strip() for  s in input().split(',')]
        if len(ls_in)==2:
            resp=read(ls_in)
            print(resp)
            if resp==-1:
                print('Запись не найдена')
                continue

        if len(ls_in)==1:
            resp = read('всё')
            print(*resp)
    if komanda=='3':
        print('Введите имя питомца и имя владельца(имя питомца, имя владельца, [новое имя питомца=значение], [новое имя владельца=значение], [новый возраст питомца=значение], [новый вид питомца=значение])')
        ls_in = [s.strip() for  s in input().split(',')]
        if len(ls_in)>2:
            resp=update(ls_in)
            if resp:
                print('Запись обновлена')
            else:
                print('Запись не найдена')
    if komanda=='4':
        print('Введите имя питомца и имя владельца(имя питомца, имя владельца)')
        ls_in = [s.strip() for  s in input().split(',')]
        resp=delete(ls_in)
        if resp:
            print('Запись удалена')
        else:
            print('Запись не найдена')