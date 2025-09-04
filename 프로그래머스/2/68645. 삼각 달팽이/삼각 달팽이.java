import java.util.*;

class Solution {
    public int[] solution(int n) {
        // 배열 초기화
        int[] answer = new int[(n * (n + 1)) / 2];
        int[][] matrix = new int[n][n];
        
        int x = -1, y = 0;
        int num = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (i % 3 == 0) {
                    // 아래
                    x++;
                } else if (i % 3 == 1) {
                    // 우측
                    y++;
                } else if (i % 3 == 2) {
                    // 좌상
                    x--;
                    y--;
                }
                matrix[x][y] = num++;
            }
        }
        
        int k = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    break;
                }
                answer[k++] = matrix[i][j];
            }
        }
        
        return answer;
    }
}