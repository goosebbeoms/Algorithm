import java.util.*;

class Solution {
    public int solution(int n) {
        StringBuilder sb = new StringBuilder();
        
        // 3진법으로 변환(순서 반전)
        while (n > 0) {
            int q = n / 3;  // 몫
            int r = n % 3;  // 나머지
            sb.append(r);
            n = q;
        }
        
        // 3진법 -> 10진법 변환 후 반환
        return Integer.parseInt(sb.toString(), 3);
    }
}