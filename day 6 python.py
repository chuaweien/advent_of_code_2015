f = open ("Day6Challenge.txt", "r")

light=[]
total = 0

for i in range (0,1000):
    light.append([])
    
for j in range (0,1000):
    for i in range (0,1000):
        light[j].append(0)

for line in f:
    line = line.strip()  
    element = line.split()
    
    if element[0] == "turn":
        start = element[2].split(",")
        for i in range (0,len(start)):
            start[i] = int(start[i])
                
        ending = element[4].split(",")
        for j in range (0,len(ending)):
            ending[j]= int(ending[j])
                        
        if element[1]== "on":
            for j in range (start[1],ending[1]+1):
                for i in range (start[0],ending[0]+1):
                    light[j][i] = 1
        
        if element[1] == "off":
            for j in range (start[1],ending[1]+1):
                for i in range (start[0],ending[0]+1):
                    light[j][i] = 0
        
    if element[0] == "toggle":
        start = element[1].split(",")
        for i in range (0,len(start)):
            start[i] = int(start[i])
            
        ending = element[3].split(",")
        for j in range (0,len(ending)):
            ending[j]= int(ending[j])
                
        for j in range (start[1],ending[1]+1):
            for i in range (start[0],ending[0]+1):
                if light[j][i] == 1:
                    light[j][i] = 0
                elif light[j][i] == 0:
                    light[j][i] =1

for i in range(0,len(light)):
    total += sum(light[i])

print total 
