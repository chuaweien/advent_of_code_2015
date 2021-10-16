f = open("Day2ChallengeRibbon.txt","r")
totalribbon=[]
for line in f:
    line = line.strip()
    newline = line.split('x')
    length =[]
    l = int(newline[0])
    w =int(newline[1])
    h =int(newline [2])
    #length.append(l)
    #length.append(w)
    #length.append(h)
    lengthUsed = 2*min(l+w,l+h,w+h)
    bow = l*w*h
    total = lengthUsed + bow
    totalribbon.append(total)

print sum(totalribbon)
