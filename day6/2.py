file = open('input.txt')
stream = file.readline().strip()

if (len(stream) < 14):
    print("Input too short")

start_idx = 14
window = set(stream[:start_idx])
if (len(window) == 14):
    print(start_idx)

for i in range(start_idx+1, len(stream)):
    window = set(stream[(i - 14):i])
    if (len(window) == 14):
        print(i)
        break
