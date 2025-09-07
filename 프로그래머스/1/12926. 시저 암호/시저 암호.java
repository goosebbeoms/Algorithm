import java.util.*;

class Solution {
    public char[] encoding(char[] plain, int n) {
        for (int i = 0; i < plain.length; i++) {
            // 공백인 경우 pass
            if (plain[i] == ' ') {
                continue;
            }
            
            if (plain[i] >= 'A' && plain[i] <= 'Z') {
                // 대문자 알파벳
                plain[i] = (char) ('A' + (plain[i] - 'A' + n) % 26);
            } else if (plain[i] >= 'a' && plain[i] <= 'z') {
                // 소문자 알파벳
                plain[i] = (char) ('a' + (plain[i] - 'a' + n) % 26);
            }
        }
        
        return plain;
    }
    
    public String solution(String s, int n) {
        char[] conv = s.toCharArray();
        
        return new String(this.encoding(conv, n));
    }
}