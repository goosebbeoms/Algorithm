import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        // 수포자 별 선택 패턴
        int[] p1 = {1, 2, 3, 4, 5};
        int[] p2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] cnt = new int[3];
        
        
        for (int i = 0; i < answers.length; i++) {
            if (p1[i % p1.length] == answers[i]) cnt[0]++;
            if (p2[i % p2.length] == answers[i]) cnt[1]++;
            if (p3[i % p3.length] == answers[i]) cnt[2]++;
        }
        
        List<Integer> result = new ArrayList<>();
        int maxValue = Arrays.stream(cnt).max().getAsInt();
        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] == maxValue) {
                result.add(i + 1);
            }
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}