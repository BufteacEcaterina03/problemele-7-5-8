t=['1','7','3','2','5','8','0','3','5','4','5','2','4','4','7','8','9','3','6','1','3','7','8','4']
ora=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
s=0
m=0
for i in t:
    s+=1
    m=s/len(t)
print(max(t),'maximul temperaturii:',min(t),'minimul temperaturii:')
max=t.index(max(t))
print('Temperatura maxima s-a inregistrat la ora:',ora[max])
min=t.index(min(t))
print('Temperatura minima s-a inregistrat la ora:',ora[min])