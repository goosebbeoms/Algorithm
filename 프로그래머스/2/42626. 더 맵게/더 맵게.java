import java.util.PriorityQueue;


class Solution {
    public int solution(int[] scoville, int K) {        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int count = 0;
        
        for (int n : scoville) {
            pq.add(n);
        }
        
        while (pq.peek() < K) {
            if (pq.size() < 2) {
                return -1;
            }
            
            int first = pq.poll();
            int second = pq.poll();
            pq.add(first + second * 2);
            count++;
        }
        
        return count;
    }
}