import java.util.*;

class Solution {
    public int[] solution(String s) {
        int convert = 0;
        int zeroCount = 0;
        
        StringBuilder sb;
        
        while (!s.equals("1")) {
            sb = new StringBuilder();
            
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '1') {
                    sb.append('1');
                } else {
                    zeroCount++;
                }
            }
            
            s = Integer.toBinaryString(sb.length());
            convert++;
        }
        
        return new int[]{convert, zeroCount};
    }
}