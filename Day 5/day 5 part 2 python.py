f = open ("Day5ChallengePart2.txt", "r")
nice = 0
for line in f:
    line = line.strip()
    pair = []
    repeat = 0
    for i in range (0,len(line)-1):
        pair.append (line.count(line[i]+line[i+1]))
    for j in range (0,len(line)-2):
        if line[j]==line[j+2]:
            repeat += 1
    #print line, max(pair), repeat
    if max(pair) >= 2 and repeat >= 1:
        nice += 1

print nice