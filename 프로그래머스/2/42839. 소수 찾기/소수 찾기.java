import java.util.*;

class Solution {
    List<Integer> list = new ArrayList<>();
    boolean[] visited = new boolean[7];
    
    public boolean isPrime(int num) {
        if (num < 2) return false;
        
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    public void dfs(String numbers, String numStr, int length) {
        if (numStr.length() == length) {
            int n = Integer.parseInt(numStr);
            
            if (list.contains(n)) return;
            
            list.add(n);
            return;
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (visited[i]) continue;
            
            visited[i] = true;
            dfs(numbers, numStr + numbers.charAt(i), length);
            visited[i] = false;
        }
    }
    
    public int solution(String numbers) {
        for (int i = 1; i <= numbers.length(); i++) {
            dfs(numbers, "", i);
        }
        
        // 전역 변수 list에서 소수만 카운트
        int result = 0;
        for (int num : list) {
            if (isPrime(num)) result++;
        }
        
        return result;
    }
}