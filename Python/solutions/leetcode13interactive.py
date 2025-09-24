#13 Roman to Integer
roman = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

roman_number = input("Enter roman number: ")
number = roman[roman_number[0]]

for i in range(1, len(roman_number)):
    current = roman[roman_number[i]]
    previous = roman[roman_number[i - 1]]
    if current <= previous:
        number += current
    elif current / previous == 5 or current / previous == 10:
        number += current - (2 * previous)
    else:
        print("Invalid roman number")
print(f"Number: {number}")