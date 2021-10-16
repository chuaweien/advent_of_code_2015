f = open ("Day5Challenge.txt", "r")
nice = 0
for line in f:
    line = line.strip()
    vowelcount = line.count("a")+line.count("e")+line.count("i")+line.count("o")+line.count("u")
    twice = 0
    forbidden = 0
    
    for i in range (0, len(line)-1):
        if line[i]==line[i+1]:
            twice += 1
        if line[i]+line[i+1] in ["ab","cd","pq","xy"]:
            forbidden += 1
    
    if vowelcount >2 and twice >= 1 and forbidden == 0:
        nice += 1
        print (line , vowelcount,twice, "nice")

print nice