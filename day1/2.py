cals = []
rations = open('input.txt', 'r')
lines = rations.readlines()
currCal = 0
for line in lines:
    if line == '\n':
        cals.append(currCal)
        currCal = 0
    else:
        currCal += int(line)
print(sum(sorted(cals)[-3:]))
