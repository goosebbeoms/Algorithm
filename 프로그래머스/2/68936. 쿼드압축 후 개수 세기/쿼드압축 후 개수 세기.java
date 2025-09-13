class Solution {
    
    public int[] result = new int[2];
    
    public boolean isCompressable(int[][] arr, int r, int c, int size) {
        int val = arr[r][c];
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (arr[i][j] != val) return false;
            }
        }
        
        return true;
    }
    
    public void quard(int[][] arr, int r, int c, int size) {
        
        // 쿼드압축 가능한 경우
        if (isCompressable(arr, r, c, size)) {
            result[arr[r][c]]++;
            
            return;
        }
        
        // 압축 불가능한 경우 재귀
        quard(arr, r, c, size / 2);
        quard(arr, r, c + size / 2, size / 2);
        quard(arr, r + size / 2, c, size / 2);
        quard(arr, r + size / 2, c + size / 2, size / 2);
    }
    
    public int[] solution(int[][] arr) {
        quard(arr, 0, 0, arr.length);
        
        return result;
    }
}