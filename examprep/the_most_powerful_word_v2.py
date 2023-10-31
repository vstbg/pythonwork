powerful_word = ""
powerful_word_sum = 0

while True:
    word = input()
    if word == "End of words":
        break

    first_letter = ''
    letters_sum = 0

    for index, letter in enumerate(str(word)):
        letters_sum += ord(letter)

        if index == 0:
            first_letter = letter.lower()

    if first_letter in "aeiouy":
        letters_sum *= len(word)
    else:
        letters_sum //= len(word)

    if letters_sum > powerful_word_sum:
        powerful_word = word
        powerful_word_sum = letters_sum

print(f"The most powerful word is {powerful_word} - {powerful_word_sum}")
