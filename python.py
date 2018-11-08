numbers = [1,2,3]
print(numbers[1])

testnumbers = [1,5,3,7,9,5,3]
len(testnumbers)
max = 0
min = 100
for i in range(len(testnumbers)):
    if testnumbers[i] >= max:
        max=testnumbers[i]

    if testnumbers[i]< min:
        min=testnumbers[i]

print(max)
print(min)

