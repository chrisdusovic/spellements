# List of chemical elements
names = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al',
    'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe',
    'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
    'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm',
    'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W',
    'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
    'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf',
    'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus', 'Uuo'
]

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
