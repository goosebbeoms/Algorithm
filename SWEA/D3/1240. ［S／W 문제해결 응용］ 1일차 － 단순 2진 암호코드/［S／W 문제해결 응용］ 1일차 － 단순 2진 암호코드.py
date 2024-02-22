code_book = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 배열의 세로 크기 N, 배열의 가로크기 M
    arr = [input() for _ in range(N)]
    code = ''
    for line in arr:
        if '1' in line:
            code = line
            break

    for idx in range(M-1, -1, -1):
        if code[idx] == '1':
            code = code[idx-55:idx+1]
            break

    decoding = ''
    for num in range(0, len(code), 7):
        decoding += code_book[code[num:num+7]]

    even_idx_v = 0
    odd_idx_v = 0
    total_num_sum = 0
    for idx in range(len(decoding)):
        num = int(decoding[idx])
        if idx % 2 == 0:
            odd_idx_v += num
            total_num_sum += num
        else:
            even_idx_v += num
            total_num_sum += num

    result = odd_idx_v * 3 + even_idx_v
    if result % 10 == 0:
        print(f'#{tc}', total_num_sum)
    else:
        print(f'#{tc}', 0)