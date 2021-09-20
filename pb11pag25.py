n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,'elemente pentru vectorul creat')
for i in range(0, n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)

