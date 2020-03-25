import sys
input = []

while True:
    line = sys.stdin.readline().strip()
    if line == '':
        break 
    input.append(line)
        
print(input)