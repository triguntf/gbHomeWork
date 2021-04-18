print("Введите врмя в секундах")
user_time = int(input())
sec=user_time%3600%60
min=user_time%3600/60
hour=user_time/3600
print(int(hour),int(min),int(sec),sep=":")

print("Веедите чимсло n")
user_num=input()
user_num1=user_num
user_num2=user_num+user_num1
user_num3=user_num1+user_num2
print(int(user_num1)+int(user_num2)+int(user_num3))

print("Введите число")
list_0=(input())
list_0=list(str(list_0))
i=1
max_number=0
while i < len(list_0):
    if list_0[i]>list_0[i-1]:
        max_number=list_0[i]
    else:
        max_number=list_0[i-1]
    i=i+1
print("Самая большая цифра в числе:",max_number)

print("Введите выручку")
proceeds= int(input())
print("Введите издержки")
costs= int(input())
if proceeds > costs:
    print("Прибыль")
    profit=proceeds-costs
    print("Рентабильность =", profit/proceeds)
    print("введите количество сотрудников")
    workers_count=int(input())
    print("прибыль на 1 рабочего составляет:",profit/workers_count)
else:
    print("Убыток")

print("введите первый результат пробежки")
first_run=int(input())
print("введите планируемый результат пробежки")
last_run=int(input())
day_num=0
while first_run < last_run:
    day_num=day_num+1
    first_run=first_run*1.1
print("на ",day_num,"-й день спортсмен достиг результата — не менее ",last_run," км.")
