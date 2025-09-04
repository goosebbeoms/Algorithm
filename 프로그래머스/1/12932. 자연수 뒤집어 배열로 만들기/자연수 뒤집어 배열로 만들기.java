import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Integer> nums = new ArrayList<>();
        
        while (n > 0) {
            nums.add((int) (n % 10));
            n /= 10;
        }
        
        return nums.stream().mapToInt(Integer::intValue).toArray();
    }
}