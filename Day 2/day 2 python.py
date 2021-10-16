f = open("Day2Challenge.txt","r")
area=[]
i = 0
for line in f:
    line = line.strip()
    newline = line.split('x')
    l = int(newline[0])
    w = int(newline[1])
    h = int(newline [2])
    minArea = min(l*w,w*h,h*l)
    eachArea = 2*l*w + 2*w*h + 2*h*l + minArea
    area.append(eachArea)

print sum(area)


        