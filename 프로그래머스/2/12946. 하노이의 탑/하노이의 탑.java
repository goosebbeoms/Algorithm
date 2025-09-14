import java.util.*;

class Solution {
    
    List<int[]> answer = new ArrayList<>();
    
    public void hanoi(int n, int from, int to, int via) {
        int[] move = {from, to};
        
        if (n == 1) {
            answer.add(move);
            return;
        }
        
        hanoi(n - 1, from, via, to);
        answer.add(move);
        hanoi(n - 1, via, to, from);
    }
    
    public int[][] solution(int n) {
        hanoi(n, 1, 3, 2);
        
        return answer.toArray(new int[0][0]);
    }
}