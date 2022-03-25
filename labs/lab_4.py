f=open('../text.txt')
len_f=f.read()
len_f=len_f.lower()
print('Длина файла:',len(len_f),'символов')
file=open('../text.txt')
s=file.readlines()
print(type(s))
alp=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
alp=sorted(alp)
ans=[0]*26
fmax=-10
answer=''
glas=0
for i in range(len(len_f)):
    if len_f[i] in ['a', 'e', 'y', 'u', 'i', 'o']:
        glas += 1
    for j in range(26):
        if len_f[i]==alp[j]:
            ans[j]+=1
        if ans[j]>fmax:
            fmax=ans[j]
            answer=j
print('Количество гласных:',glas)
print('Самая часто встречаемся буква',alp[answer])
print(f"Количество строк {len(s)}")

