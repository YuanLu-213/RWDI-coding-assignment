
##Extract data from downloaded text file
with open('input_day1.txt') as file:
    lines = file.readlines()
    data = []
    for line in lines:
        data.append(int(line.strip()))

##Part-1:
##Function for counting the increment times    
def findMeasurementIncrease(data):
    ans = 0
    prev = data[0]
    
    for num in data[1::]:
        if num > prev:
            ans += 1
        prev = num

    return ans

print(f'Answer is: {findMeasurementIncrease(data)}')

##Part-2:
##Function for counting the increment times of the sum
def findSumIncrease(data):
    ans = 0
    prev = float('inf')

    for i in range(2, len(data)):
        three_sum = data[i-2] + data[i-1] + data[i]
        if three_sum > prev:
            ans += 1
        prev = three_sum

    return ans

print(f'Answer is: {findSumIncrease(data)}')