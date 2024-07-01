import sys
# sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline().strip()

sum = 0
current_number = ''
is_negative = False
numbers = []

for char in input:
    if is_negative:
        if char.isdigit():
            current_number += char
        else: 
            sum -= int(current_number)
            current_number = ''
    elif char.isdigit():
        current_number += char
    elif char == '-' : 
        sum += int(current_number)
        current_number = ''
        is_negative = True
    else :
        sum += int(current_number)
        current_number = ''

#마지막 숫자 처리
if current_number:
    if is_negative:
        sum -= int(current_number)
    else:
        sum += int(current_number)
print(sum)

