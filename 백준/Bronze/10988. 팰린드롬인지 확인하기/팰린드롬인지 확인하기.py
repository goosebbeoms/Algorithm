text = input()

boolean = True
for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        boolean = False
        break

print(int(boolean))