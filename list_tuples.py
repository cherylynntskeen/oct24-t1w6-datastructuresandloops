# List - Array - ordered collection f values - mutable [list can be changed] -zero indexed
numbers = [13, 2, 23, 53]
print(numbers)
print(numbers[-2])

#will get rid of the 2nd index number (23) and replace with 17
numbers [2] = 17
print (numbers)

#puts number at the end of the array
numbers.append(42)
print(numbers)

#inserts number in where i want it to within the array
numbers.insert(3, 99)
print(numbers)

#removes last number from array 
numbers.pop()
print(numbers)

#will return the number which was popped off
popped_value = numbers.pop(2)
print(numbers)
print(popped_value)

#will remove the value within parenthesis
numbers.remove(13)
print(numbers)

#will put them in ascending order
numbers.sort(reverse=True)
print(numbers)

#will show how many times the number is in the array based on what number is being passed in the parenthesis
print(numbers.count(53))



# Tuple - an ordered collection of values - zero indexed - immutable (tuples can't be changed)
names = ("John", "Jane", "Mike", "Mary")
print(names)
print(type(names))

print(names.index("Mike"))

print(len(names))