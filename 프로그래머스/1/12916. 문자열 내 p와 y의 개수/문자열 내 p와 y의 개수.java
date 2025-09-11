class Solution {
    boolean solution(String s) {
        int countP = 0;
        int countY = 0;
        
        for (int i = 0; i < s.length(); i++) {
            char target = s.charAt(i);
            if (target == 'p' || target == 'P') countP++;
            if (target == 'y' || target == 'Y') countY++;
        }
        
        return countP == countY ? true : false;
    }
}