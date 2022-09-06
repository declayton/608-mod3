# Deanna Clayton mod3 File2
## Rolling 2 six sided dice
import random
## face frequency counters
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0
frequency7 = 0
frequency8 = 0
frequency9 = 0
frequency10 = 0
frequency11 = 0
frequency12 = 0
## 6,000,000 dice rolls
for roll in range(6_000_000):
    face = random.randrange(1, 7) + random.randrange(1, 7)
    if face == 2:
        frequency2 += 1
    elif face == 2:
        frequency2 += 1
    elif face == 3:
        frequency2 += 1
    elif face == 4:
        frequency2 += 1
    elif face == 5:
        frequency2 += 1
    elif face == 6:
        frequency2 += 1
    elif face == 7:
        frequency2 += 1
    elif face == 8:
        frequency2 += 1
    elif face == 9:
        frequency2 += 1
    elif face == 10:
        frequency2 += 1
    elif face == 11:
        frequency2 += 1
    elif face == 12:
        frequency2 += 1

print(f'Face{"Frequency":>13}')
print(f'{2:>4}{frequency2:>13}')
print(f'{3:>4}{frequency2:>13}')
print(f'{4:>4}{frequency2:>13}')
print(f'{5:>4}{frequency2:>13}')
print(f'{6:>4}{frequency2:>13}')
print(f'{7:>4}{frequency2:>13}')
print(f'{8:>4}{frequency2:>13}')
print(f'{9:>4}{frequency2:>13}')
print(f'{10:>3}{frequency2:>13}')
print(f'{11:>3}{frequency2:>13}')
print(f'{12:>3}{frequency2:>13}')
