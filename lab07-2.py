N = int(input("Введіть кількільсть слів: "))
words = []
for i in range(N):
    word = input(f"Введіть слово {i + 1}: ")
    words.append(word.strip())
    result_string = ','.join(words)
    print(result_string)