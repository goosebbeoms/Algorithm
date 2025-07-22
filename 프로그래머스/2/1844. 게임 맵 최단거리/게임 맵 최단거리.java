import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;
        
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0, 1});
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            int row = cur[0];
            int col = cur[1];
            int dist = cur[2];
            
            if (row == rows - 1 && col == cols - 1) {
                return dist;
            }
            
            for (int[] d : directions) {
                int newRow = row + d[0];
                int newCol = col + d[1];
                
                if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols && maps[newRow][newCol] == 1) {
                    maps[newRow][newCol] = 0;
                    q.offer(new int[]{newRow, newCol, dist + 1});
                }
            }
        }
        
        return -1;
    }
}