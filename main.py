joker = int(input("Enter your joker number: "))
numbersList = input("Enter your numbers: ")

numbersList = list(map(int, numbersList.split()))

numberClosestToJoker = None
numberClosestToJokerIndex = []

for i in range(len(numbersList)):
    sub = abs(numbersList[i] - joker)
    if numberClosestToJoker == None:
        numberClosestToJoker = numbersList[i]
        numberClosestToJokerIndex.append(i)
    elif sub <= abs(numberClosestToJoker - joker):
        numberClosestToJokerIndex.append(i)
        numberClosestToJoker = numbersList[i]

numberClosestToJokerIndex = [x for x in numberClosestToJokerIndex if abs(numbersList[x] - joker) == abs(numberClosestToJoker - joker)]

print(f'menor distância absoluta: {abs(numberClosestToJoker - joker)}')
for i in numberClosestToJokerIndex:
    print(f'{i}:{numbersList[i]}')