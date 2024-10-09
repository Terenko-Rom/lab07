input_string = input("Введіть рядок: ")
letter_count = 0
digit_count = 0
for char in input_string:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print(f"Кількість літер: {letter_count}")
print(f"Кількість цифр: {digit_count}")