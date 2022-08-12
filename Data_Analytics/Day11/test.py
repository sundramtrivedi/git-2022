N = int(input())
while N < 1 and N > 500000:
    N = int(input())

allPossibleSets = list()

for i in range(0, N):
    mySet = set()
    product = 1
    for j in range(1, i):
        mySet.add(i)
        product *= j
    
    if product % N == 1:
        allPossibleSets.append(mySet)

totalLength = []
for i in allPossibleSets:
    totalLength.append(len(i))

# print(max(totalLength))