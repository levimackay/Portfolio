''' def greet(name):
    return "Hello " + name

print(greet(5)) '''
'''
def multiply_by_two(x):
    result = x + 2
    return result

print(multiply_by_two(5))  # Expected: 10'''
def remove_odd_numbers(numbers):

    for i in range(1, len(numbers)):

        if numbers[i] % 2 == 1:

            numbers.pop(i)

    return numbers

print(remove_odd_numbers([1, 2, 3, 4, 5]))  # Expected: [2, 4]