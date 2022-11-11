s = ((1 + 237_567_892) / 2) * 237_567_892
counter = int(s % 3 != 0)
for i in range(237_567_892 + 1, 1_134_567_004 + 1):
    s += i
    counter += int(s % 3 != 0)
print(counter)
