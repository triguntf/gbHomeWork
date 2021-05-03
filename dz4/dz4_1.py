
from sys import argv

salary,second_param,third_param,foth_param= argv
salary=list()
for i in argv[1::]:
    salary.append(int(i))

print(" salary = ",salary[0]*salary[1]+salary[2])