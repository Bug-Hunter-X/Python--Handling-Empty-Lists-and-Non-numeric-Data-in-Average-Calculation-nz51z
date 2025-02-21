def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average}")

my_list_with_zero = [10, 0, 30, 40, 50]
average = calculate_average(my_list_with_zero)
print(f"The average is: {average}")

my_list_with_strings = [10, 20, '30', 40, 50]
average = calculate_average(my_list_with_strings)
print(f"The average is: {average}") #This will return the average of numeric values only 