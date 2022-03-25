s=str(input('Введите строку:'))
smax=-1000
new=''
mass=s.split('')
print(mass)
if len(mass)>=3:
    for i in range(1,len(mass)-1):
        if len(mass[i])>smax:
            smax=len(mass[i])
            new=mass[i]
else:
    print('В строке меньше 2 *')
otvet=''
for i in range(len(new)):
    if i%2:
        otvet+=new[i].lower()
    else:
        otvet+=new[i].upper()
print(otvet,smax)