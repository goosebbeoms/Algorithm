import math

lst = []
visited = [False] * 7

def dfs(numbers, num_str):
    if len(num_str) == len(numbers):
        lst.append(int(num_str))
        return
    
    for i in range(len(numbers)):
        if visited[i]:
            continue
        lst.append(int(num_str + numbers[i]))
        visited[i] = True
        dfs(numbers, num_str + numbers[i])
        visited[i] = False

def is_prime(number):
    if number < 2:
        return False
    
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
        
    return True

def solution(numbers):
    for i in range(1, len(numbers)):
        dfs(numbers, "")
    
    result = 0;
    for num in set(lst):
        if is_prime(num):
            result += 1
    
    return result