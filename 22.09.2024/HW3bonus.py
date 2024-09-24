# START
numbers: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index: int = 0
while True:
    num: int = int(input("Enter a number between 1-100: "))
    if num == -999:
        print(f"updated list is: {numbers}")
        break

    for i in range(len(numbers)):
        if num >= numbers[i]:
            index = i+1

    numbers.insert(index,num)
# STOP
