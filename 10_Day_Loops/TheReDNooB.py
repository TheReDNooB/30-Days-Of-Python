# Exercises: Level 1
#
## 1. Iterate 0 to 10 using for loop, do the same using while loop
for i in range(11):
    print("For Loop ", i)

counter = 0
while counter < 11:
    print("While Loop ",counter)
    counter += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop
for i in range(10, -1 , -1):
    print("For Loop ", i)

counter = 10
while counter >= 0:
    print("While Loop ",counter)
    counter -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(8):
    print("#" * i)


# 4. Use nested loops to create the following:
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

print("------------------------------------")
number = 8
while number > 0:
    print("# " * 8)
    number -= 1

# 5. Print the following pattern:
for i in range(11):
    print(f"{i} x {i} = {i*i}")

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lst:
    print(i)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print("even numbers ",i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 3 == 0:
        print("odd numbers ",i)
