
n = int(input("How many numbers do you want to enter? "))
numbers = []
evenCount = 0
oddCount = 0
index = 1

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

for value in numbers:
    print(f"index {index}: {value}")
    index += 1
    if value % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(f"Total even numbers: {evenCount}")
print(f"Total odd numbers: {oddCount}")

index = int(input("Enter the index of the number you want to replace: "))
numbers[index - 1] = int(input("Enter the new number: "))

