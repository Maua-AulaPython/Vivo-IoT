n=0
i=0
l=[]
while(n>= 0):
        a= float(raw_input('digite uma nota:  '))
        
        if(a>=0):
                l.append(a)
                i+=1
        else:
                n=-1
soma=0
media=0.0
for j in range(i):
    soma += l[j]
    media = soma/i
print ('sua media eh {0}'.format(media))

#Nota: 1.0
#Comentario: Bom uso do .format()
