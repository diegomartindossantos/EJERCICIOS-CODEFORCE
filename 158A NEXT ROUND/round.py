
#N K    N= NUMERO PARTICIPANTES 

# K = POSICION DEL PARTICIPANTE DEL CUAL SE TIENE QUE IGUALAR O SUPERAR LA NOTA
#SCORE TIENE QUE SER POSITIVO si o si

participantes, posicion_score = input().split(" ")
posicion_score = int(posicion_score)
notas = input().split(" ")
pasan = 0
corte = int(notas[posicion_score-1])

for nota in notas:
    if int(nota) > 0:
        if int(nota) >= corte:
            pasan += 1
        else:
            pass
    else:
        pass
print (pasan)
