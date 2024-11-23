# while loop
number = 1
while number <= 5:
    print(number)
    number = number + 1 #increment

#for loop
names = ["John", "Jane", "Mike", "Mary"]

#will add 
for name in enumerate(names):
    print(name)

for index, name in enumerate(names):
    print(name)

for index, name in enumerate(names):
    print(f"{index+1}. {name}")

# List all numbers between 10 and 100 and state whether they are odd or even
for num in range(10, 101):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#ternary option of the above code
for num in range(10, 101):
    print(f"{num} is {"even" if num % 2 == 0 else "odd"}")

#for else
for i in range(10):
    print(i)
    if i == 6:
        break
else:
    print("loop finished")
