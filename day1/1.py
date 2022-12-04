maxCal = 0
rations = open('input.txt', 'r')
lines = rations.readlines()
currCal = 0
for line in lines:
    if line == '\n':
        currCal = 0
    else:
        currCal += int(line)
        if currCal > maxCal:
            maxCal = currCal

print(maxCal)
