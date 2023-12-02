out = 0
numbers = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', '0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
with open('input') as calibration:
    for line in calibration.readlines():
        numbers_from_input = {index:v for k, v in numbers.items() if (index := line.find(k)) != -1}
        numbers_from_input.update({index:v for k, v in numbers.items() if (index := line.rfind(k)) != -1})
        sorted_indices = sorted(numbers_from_input)
        out += int(numbers_from_input[sorted_indices[0]]+numbers_from_input[sorted_indices[-1]])
print(out)