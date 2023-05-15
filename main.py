## Recebe o número coringa
joker = int(input("Enter your joker number: "))

## Recebe a lista de números
numbersList = input("Enter your numbers: ")

## Converte a input de uma string "1 2 3" pra uma lista de inteiros
numbersList = list(map(int, numbersList.split()))

## Número mais próximo do coringa
numberClosestToJoker = None
## Index dos números mais próximos do coringa
numberClosestToJokerIndex = []

## Itera a lista de números
for i in range(len(numbersList)):
    ## Subtrai o número atual com o coringa
    ## Ex: 5 (número atual) - 3 (coringa) = 2 (distância absoluta)
    ## O abs serve pra converter o número pra positivo
    sub = abs(numbersList[i] - joker)

    ## Se for o primeiro número da lista ele é o mais próximo
    if numberClosestToJoker == None:
        numberClosestToJoker = numbersList[i]

        ## Adiciona o indice na lista de índices dos números mais próximos
        numberClosestToJokerIndex.append(i)
    
    ## Se a distância absoluta do número atual for menor ou igual 
    ## a distância absoluta do número mais próximo do coringa
    ## então esse número vira o mais próximo do coringa
    ## e seu índice é adicionado na lista de índices dos números mais próximos
    elif sub <= abs(numberClosestToJoker - joker):
        numberClosestToJokerIndex.append(i)
        numberClosestToJoker = numbersList[i]

## Remove da lista de índices todos os números que tenham uma distância absoluta maior do que o número mais próximo do coringa
numberClosestToJokerIndex = [x for x in numberClosestToJokerIndex if abs(numbersList[x] - joker) == abs(numberClosestToJoker - joker)]

print(f'menor distância absoluta: {abs(numberClosestToJoker - joker)}')
for i in numberClosestToJokerIndex:
    print(f'{i}:{numbersList[i]}')