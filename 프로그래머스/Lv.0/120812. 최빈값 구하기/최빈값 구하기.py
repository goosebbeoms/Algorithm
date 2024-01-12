def solution(array):
    array_to_set = set(array)
    tmp = dict.fromkeys(array_to_set, 0)

    for i in array:
        tmp[i] += 1

    max_value = max(list(tmp.values()))

    keys = []
    for key, value in tmp.items():
        if value == max_value:
            keys.append(key)
        else:
            continue

    if len(keys) != 1:
        answer = -1
    else:
        answer = keys[0]
    return answer