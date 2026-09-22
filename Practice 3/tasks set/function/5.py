def permutations(text, current=""):
    if len(text) == 0:
        print(current)
        return

    for i in range(len(text)):
        new_text = text[:i] + text[i + 1:]
        permutations(new_text, current + text[i])


text = input("Enter a string: ")
permutations(text)