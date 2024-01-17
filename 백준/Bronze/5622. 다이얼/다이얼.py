lst = list(input())
for i in range(len(lst)):
    if lst[i] in ['A', 'B', 'C']:
        lst[i] = 3
    elif lst[i] in ['D', 'E', 'F']:
        lst[i] = 4
    elif lst[i] in ['G', 'H', 'I']:
        lst[i] = 5
    elif lst[i] in ['J', 'K', 'L']:
        lst[i] = 6
    elif lst[i] in ['M', 'N', 'O']:
        lst[i] = 7
    elif lst[i] in ['P', 'Q', 'R', 'S']:
        lst[i] = 8
    elif lst[i] in ['T', 'U', 'V']:
        lst[i] = 9
    elif lst[i] in ['W', 'X', 'Y', 'Z']:
        lst[i] = 10
print(sum(lst))