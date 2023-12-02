numbs = [str(i) for i in range(10)]
out = 0
with open('input') as calibration:
    for line in calibration.readlines():
        numbers_from_input = [character for character in line if character in numbs]
        out += int(numbers_from_input[0]+numbers_from_input[-1])
print(out)