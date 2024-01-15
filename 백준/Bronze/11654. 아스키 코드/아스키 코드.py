ascii = input()

if type(ascii) == str:
    print(ord(ascii))
elif type(ascii) == int:
    print(chr(ascii))