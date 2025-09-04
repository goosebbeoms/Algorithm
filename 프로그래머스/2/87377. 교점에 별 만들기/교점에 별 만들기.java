import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        int top = Integer.MIN_VALUE;     // 최대 y
        int bottom = Integer.MAX_VALUE;  // 최소 y
        int left = Integer.MAX_VALUE;    // 최소 x
        int right = Integer.MIN_VALUE;   // 최대 x
        
        List<long[]> points = new ArrayList<>();
        
        // 완전탐색으로 두 직선 교점 구하기
        for (int i = 0; i < line.length - 1; i++) {
            long A = line[i][0], B = line[i][1], E = line[i][2];
            for (int j = i + 1; j < line.length; j++) {
                long C = line[j][0], D = line[j][1], F = line[j][2];
                
                long den = (A * D) - (B * C);     // 분모
                
                // 두 직선이 평행 또는 일치하는 경우 pass
                if (den == 0) {
                    continue;
                }
                
                long dx = (B * F) - (E * D);
                long dy = (E * C) - (A * F);
                
                // 계산한 교점이 정수로 표현될 때만 작업 진행
                if (dx % den != 0 || dy % den != 0) {
                    continue;
                }
                
                long xL = dx / den;
                long yL = dy / den;
                
                // 교점 리스트에 삽입
                points.add(new long[]{xL, yL});
                
                // 격자판 사이즈 재정의
                int x = (int) xL;
                int y = (int) yL;
                top = Math.max(top, y);
                bottom = Math.min(bottom, y);
                left = Math.min(left, x);
                right = Math.max(right, x);
            }
        }
        
        // 교점이 없을 때
        if (points.isEmpty()) return new String[]{"."};
        
        int height = top - bottom + 1;
        int width = right - left + 1;
        
        // 보드 초기화
        char[][] board = new char[height][width];
        for (int r = 0; r < board.length; r++) {
            Arrays.fill(board[r], '.');
        }
        
        for (long[] point : points) {
            board[top - (int) point[1]][(int) point[0] - left] = '*';
        }
        
        String[] result = new String[height];
        for (int h = 0; h < result.length; h++) {
            result[h] = new String(board[h]);
        }
        
        return result;
    }
}