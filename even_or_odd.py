#Function to determine if a number is even or odd

def even_or_odd(num):
    if num % 2 == 0:
        return "Even" #return exits the function immediately
    else:
        return "Odd"

even_or_odd(5)
result = even_or_odd(10)
even_or_odd(5423)
print(f"10 is {result}.")