text = input().upper()
text_set = list(set(text))
text_count = [0 for i in text_set]
for c in text_set:
    temp = text.count(c)
    idx = text_set.index(c)
    text_count[idx] = temp

idx2 = text_count.index(max(text_count))
picked_str = text_set.pop(idx2)
picked_count = text_count.pop(idx2)

if picked_count in text_count:
    picked_str = '?'

print(picked_str)