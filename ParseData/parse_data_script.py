#: ([^:\s]+)
import re

list_to_regex = []

with open("run2.stat.txt", "r") as ifile:
    for line in ifile:
        list_to_regex.append(line)

'''
for line in list_to_regex:
    x = re.search(r": ([^:\s]+)", line)
    fitness.append(x.string)
'''

switcher = 0

#generations = []
			
fitness = []

counter = 0

for line in list_to_regex:
    if counter > 13: 
        if switcher == 1:
            #generations.append(line[-19:])
            switcher = 0
        elif switcher == 0:
            fitness.append(re.sub("[^1234567890.]", "", line[-19:]) + "\n")
            switcher = 1
    counter = counter + 1
        
#print(generations)

counter = 0

f= open("test2.txt","w+")

for fit in fitness:
    if counter >  5:
        print("Generation " + str(counter-5))
        print(fit)
        f.write(str(counter-5) + ",")
        f.write(str(fit) + ",")
    counter = counter + 1
    

f.flush()
f.close
