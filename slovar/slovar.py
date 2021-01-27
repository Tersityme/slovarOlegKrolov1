def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(f,list):
    fail=open(f,'w',encoding="utf-8-sig")
    for k in list:
        fail.write(k+"\n")
    fail.close()
    return list

def salvesta_failisse(f,text):
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(text+"\n")
    fail.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def uued_sonad():
    rus_sona=input("Введи слово на русском: ")
    eng_sona=input("Введи слово на английском: ")
    rus_list=salvesta_failisse("rus.txt",rus_sona)
    eng_list=salvesta_failisse("eng.txt",eng_sona)
    return rus_list, eng_list

def tolkimine(rus_list,eng_list):
    slovo=input("Введите слово для перевода: ")
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo}-{eng_list[ind]}")
    elif slovo in eng_list:
        ind=eng_list.index(slovo)
        print(f"{slovo}-{rus_list[ind]}")
    else:
        print(f"Слово: {slovo.upper()} отсутствует в словаре!")
        v=input("Желаете добавить новое слово? ")
        if v.lower()=="да": uued_sonad()

def parandus(rus_list,eng_list):
    viga=input("Введите слово с ошибкой: ")
    if viga in rus_list:
        ind=rus_list.index(viga)
        print(f"Будет исправлена пара слов {viga}-{eng_list[ind]}")
        rus_list.pop(ind)
        eng_list.pop(ind)
        rus_list=list_failisse("rus.txt",list)
        eng_list=list_failisse("eng.txt",list)
        uued_sonad()
    elif viga in eng_list:
        ind=eng_list.index(viga)
        print(f"Будет исправлена пара слов {viga}-{eng_list[ind]}")
        rus_list.pop(ind)
        eng_list.pop(ind)
        rus_list=list_failisse("rus.txt",list)
        eng_list=list_failisse("eng.txt",list)
        uued_sonad()
    else:
        print(f"Слово: {viga.upper()} отсутствует в словаре!")
    rus_list=loe_failist("rus.txt")
    eng_list=loe_failist("eng.txt")
    return rus_list,eng_list

rus_list=loe_failist("rus.txt")
eng_list=loe_failist("eng.txt")
print(rus_list)
print(eng_list)

while True:
    v=input("Перевод-1\nДобовление слова-2\nИсправление ошибки-3\nПроверка знаний-4\nВведите подходящий вариант: ")
    if v=="1":
        tolkimine(rus_list,eng_list)
    elif v=="2":
        rus_list, eng_list=uued_sonad()
    elif v=="3":
        print(rus_list,eng_list)
        rus_list,eng_list=parandus(rus_list,eng_list)
        print(rus_list,eng_list)
    elif v=="4":
        pass