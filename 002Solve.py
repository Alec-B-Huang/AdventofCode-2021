file = open('INSERT FILE PATH', 'r')
data = file.read()

Horizontal = 0
Depth = 0
data = data.splitlines()
for line in data:
    newLine = line.split()
    if newLine[0] == 'forward':
        Horizontal += int(newLine[1])
    elif newLine[0] == 'down':
        Depth += int(newLine[1])
    elif newLine[0] =='up':
        Depth -= int(newLine[1])

print('PART 1')
print('Horizontal position:' , Horizontal)
print('Final Depth:' , Depth)
print('The result is:' , Depth * Horizontal)

Horizontal = 0
Depth = 0
Aim = 0
for line in data:
    newLine = line.split()
    if newLine[0] == 'forward':
        Horizontal += int(newLine[1])
        Depth += int(newLine[1]) * Aim
    elif newLine[0] == 'down':
        Aim += int(newLine[1])
    elif newLine[0] =='up':
        Aim -= int(newLine[1])

print('PART 2')
print('Horizontal position:' , Horizontal)
print('Final Depth:' , Depth)
print('The result is:' , Depth * Horizontal)
