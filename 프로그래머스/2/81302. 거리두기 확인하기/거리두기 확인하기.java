import java.util.*;

class Solution {
    int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};     // 동, 서, 남, 북
    
    public int checker(String[] board, int r, int c) {
        // BFS
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{r, c});
        
        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            
            for (int[] direction : directions) {
                int nr = direction[0] + position[0];
                int nc = direction[1] + position[1];
                
                // 대기실 범위 초과 pass
                if (nr < 0 || nr >= 5 || nc < 0 || nc >= 5 || (nr == r && nc == c)) continue;
                
                // 맨해튼 거리
                int distance = Math.abs(nr - r) + Math.abs(nc - c);
                
                if (board[nr].charAt(nc) == 'P' && distance <= 2) {
                    return 0;
                } else if (board[nr].charAt(nc) == 'O' && distance < 2) {
                    queue.offer(new int[] {nr, nc});
                }
            }
        }
        
        return 1;
    }
    
    public int rotater(String[] board) {
        for (int r = 0; r < board.length; r++) {
            for (int c = 0; c < board[r].length(); c++) {
                if (board[r].charAt(c) != 'P') continue;
                
                if (this.checker(board, r, c) == 0) return 0;
            }
        }
        
        return 1;
    }
    
    public int[] solution(String[][] places) {
        // 결과 제출용 배열 선언
        int[] result = {0, 0, 0, 0, 0};
        
        for (int i = 0; i < places.length; i++) {
            result[i] = this.rotater(places[i]);
        }
        
        return result;
    }
}