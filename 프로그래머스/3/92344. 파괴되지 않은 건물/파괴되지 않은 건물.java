class Solution {
    public int solution(int[][] board, int[][] skill) {
        int N = board.length;
        int M = board[0].length;
        int[][] matrix = new int[N + 1][M + 1];     // 구간합 계산용 2차원 배열
        
        for (int[] s : skill) {
            // s[0] 값에 따라 공격 또는 회복
            int degree = s[5] * ((s[0] == 1) ? -1 : 1);
            
            matrix[s[1]][s[2]] += degree;                   // 상단 / 좌측
            matrix[s[1]][s[4] + 1] += (degree * -1);        // 상단 / 우측+1
            matrix[s[3] + 1][s[2]] += (degree * -1);        // 하단+1 / 좌측
            matrix[s[3] + 1][s[4] + 1] += degree;           // 하단+1 / 우측+1
        }
        
        // 누적합 계산
        // 좌우
        for (int i = 0; i < N; i++) {
            for (int j = 1; j < M; j++) {
                matrix[i][j] += matrix[i][j - 1];
            }
        }
        // 상하
        for (int j = 0; j < M; j++) {
            for (int i = 1; i < N; i++) {
                matrix[i][j] += matrix[i - 1][j];
            }
        }
        
        // 파괴되지 않은 건물 개수 계산
        int answer = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] + matrix[i][j] > 0) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
}