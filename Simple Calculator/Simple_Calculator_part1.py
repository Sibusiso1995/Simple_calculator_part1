def add(*numbers):
    sumNumbers = sum(numbers)
    return sumNumbers

def multiply(*numbers):
    output = 1

    for each_number in numbers:
        output *= each_number
   
    return output
