numbers=[10,40,50,88,99,110,405,550]
for num in numbers:
    if num > 500:
        break

    elif num > 150:
        continue

    elif num%5==0:

        print(num)
        