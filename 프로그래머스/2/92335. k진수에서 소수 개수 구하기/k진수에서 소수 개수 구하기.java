import java.util.*;

class Solution {
    public boolean isPrime(long num) {
        if (num == 1) {
            return false;
        }
        
        for (int i = 3; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        
        return true;
    }
    
    public int solution(int n, int k) {
        Deque<String> stack = new ArrayDeque<>();
        int remainder;
        while (n != 0) {
            remainder = n % k;
            n /= k;
            stack.push(Integer.toString(remainder));
        }
        
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        
        int answer = 0;
        for (String s : sb.toString().split("0")) {
            if (s.equals("")) {
                continue;
            }
            
            if (isPrime(Long.valueOf(s))) {
                answer++;
            }
        }
        
        return answer;
    }
}