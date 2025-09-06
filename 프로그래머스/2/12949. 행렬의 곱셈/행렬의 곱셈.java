class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int resRow = arr1.length;
        int resCol = arr2[0].length;
        int standard = arr1[0].length;
        int[][] result = new int[resRow][resCol];
        
        for (int row = 0; row < result.length; row++) {
            for (int col = 0; col < result[row].length; col++) {
                // 각 원소에 해당하는 값 계산
                int num = 0;
                for (int i = 0; i < standard; i++) {
                    num += arr1[row][i] * arr2[i][col];
                }
                result[row][col] = num;
            }
        }
        
        return result;
    }
}