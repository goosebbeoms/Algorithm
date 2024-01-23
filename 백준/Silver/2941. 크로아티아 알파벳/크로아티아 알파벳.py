text = input()

special_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alphabet_count = len(text)

i = 0
while i < len(text):
    if text[i] in ['c', 'd', 'l', 'n', 's', 'z']:
        if (text[i:i+2] in special_alphabet) or (text[i:i+3] == 'dz='):
            if text[i:i+3] == 'dz=':
                alphabet_count -= 2
                i += 2
                continue
            alphabet_count -= 1
    i += 1

print(alphabet_count)