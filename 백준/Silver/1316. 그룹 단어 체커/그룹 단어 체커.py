N = int(input())  # 단어의 개수
group_word = 0

for n in range(N):
    word = input()
    
    i = 0
    char_list = []
    is_group_word = True
    
    while i < len(word):
        if word[i] in char_list:
            if i > 0 and (word[i-1] == word[i]):
                i += 1
            else:
                is_group_word = False
                break
        else:
            char_list.append(word[i])
            i += 1
    
    if is_group_word:
        group_word += 1

print(group_word)