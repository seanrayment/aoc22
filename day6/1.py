file = open('input.txt')
stream = file.readline().strip()

if (len(stream) < 4):
    print("Input too short")

start_idx = 4
window = set(stream[:start_idx])
if (len(window) == 4):
    print(start_idx)

for i in range(start_idx+1, len(stream)):
    window = set(stream[(i - 4):i])
    if (len(window) == 4):
        print(i)
        break
