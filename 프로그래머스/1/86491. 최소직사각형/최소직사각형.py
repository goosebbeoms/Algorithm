def check(w, h, sizes):
    for wide, height in sizes:
        if not ((w >= wide and h >= height) or (w >= height and h >= wide)):
            return False
    return True


def solution(sizes):
    w_lst, h_lst = [], []
    for w, h in sizes:
        w_lst.append(w)
        h_lst.append(h)
    w_lst.sort()
    h_lst.sort()
    
    total_min = min(min(w_lst), min(h_lst))
    total_max = max(max(w_lst), max(h_lst))
    
    answer = max(w_lst) * max(h_lst)
    
    for w in range(total_min, total_max+1):
        for h in range(total_min, total_max+1):
            if check(w, h, sizes) and (answer > (w * h)):
                answer = w * h
    
    return answer