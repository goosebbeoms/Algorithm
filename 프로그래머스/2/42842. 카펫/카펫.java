class Solution {
    public int[] solution(int brown, int yellow) {
        int[] result = {0, 0};
        
        int area = brown + yellow;
        for (int w = 3; w <= area / 3; w++) {
            int h = area / w;
            if (area % w != 0 || w < h) continue;
            
            int y = (w - 2) * (h - 2);
            int b = area - y;
            
            if (b == brown && y == yellow) {
                result[0] = w;
                result[1] = h;
                break;
            }
        }
        
        return result;
    }
}