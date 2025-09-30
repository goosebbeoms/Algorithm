def solution(brown, yellow):
    area = brown + yellow
    
    for w in range(3, area // 3 + 1):
        h = area // w
        
        if area % w != 0 or w < h:
            continue
                
        brown_cnt = (w + h) * 2 - 4
        yellow_cnt = area - brown_cnt
        
        if brown_cnt == brown and yellow_cnt == yellow:
            return [w, h]