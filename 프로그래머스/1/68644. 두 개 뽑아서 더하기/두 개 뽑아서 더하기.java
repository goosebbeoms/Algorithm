import java.util.*;

class Solution {
    Set<Integer> bucket = new HashSet<>();
    
    public int[] solution(int[] numbers) {
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                bucket.add(numbers[i] + numbers[j]);
            }
        }
        
        List<Integer> list = new ArrayList<>(bucket);
        Collections.sort(list);
        
        int[] answer = new int[list.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}