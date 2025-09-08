import java.util.*;

class Solution {
    public int solution(String s) {
        int len = s.length();
        if (len == 1) return 1;
        
        int answer = Integer.MAX_VALUE;
        
        // 패턴 길이 증가 반복
        for (int r = 1; r <= len / 2; r++) {
            String pattern = s.substring(0, r);
            int cnt = 1;
            StringBuilder sb = new StringBuilder();
            
            for (int i = r; i <= len - r; i += r) {
                String cur = s.substring(i, i+r);
                
                if (pattern.equals(cur)) {
                    cnt++;
                } else {
                    if (cnt > 1) sb.append(cnt);
                    sb.append(pattern);
                    pattern = cur;
                    cnt = 1;
                }
            }
            
            if (cnt > 1) sb.append(cnt);
            sb.append(pattern);
            
            int leftover = len % r;
            answer = Math.min(answer, sb.length() + leftover);
        }
        
        return answer;
    }
}