# Get element symbols from list
with open('elements.txt', 'r') as f:
    names = [line.rstrip() for line in f]

# Get desired word from user
target = input('Enter desired word: ').lower()

results = []

# Determines the amount of letters matched up last run
skip = 0
for i in range(0, len(target)):
    # Check if character has been included already.
    if skip > 0:
        skip -= 1
    else:
        chars_left = len(target) - i
        if chars_left > 3:
            max_chars = 3
        else:
            max_chars = chars_left
        if chars_left > 0:
            # Slice into three characters, two characters, one character
            for x in range(max_chars, 0, -1):
                piece = target[i:i + x]
                result = -1
                for index, name in enumerate(names):
                    # Checks for symbol match
                    if piece == name.lower():
                        result = index
                        skip = x - 1
                        break
                if result != -1:
                    break

            results.append(result)

# Fail
if -1 in results:
    print("Your input could not be spelled.")
# Success
else:
    final = []
    for result in results:
        # Atomic number
        z = result + 1
        # Aligns atomic numbers
        spacing = ' ' * (3 - len(str(z)))
        print(spacing + str(z) + ' - ' + str(names[result]))
        final.append(names[result])
    print(''.join(final))
