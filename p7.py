v=[3234,5678,4876,2340,3322,4545,3987]
zi=['Luni','Marti','Miercuri','Joi','Vineri','Sambata','Duminica']
s=sum(v)
m=0
for i in v:
    s+=1
    m=s/len(v)
print("Venitul saptamanal este:",s)
print("Media zilnica a venitului este:",m)
max=v.index(max(v))
print("Ziua in care s-a obtinut cel mai mare venit", zi[max])
min=v.index(min(v))
print("Ziua in care s-a obtinut cel mai mic venit", zi[min])     