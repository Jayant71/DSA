def next_greatest_letter(letters, target):
    for chr in letters:
        if (chr > target):
            return chr
    return letters[0]


letters = ['c', 'f', 'j']
target = 'k'
print(next_greatest_letter(letters, target))
