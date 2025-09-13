class Solution {
    public String solution(String new_id) {
        // 1단계
        String first = new_id.toLowerCase();
        
        // 2단계
        String second = first.replaceAll("[^a-z0-9-_.]", "");
        
        // 3단계
        String third = second.replaceAll("\\.{2,}", ".");
        
        // 4단계
        String fourth = third.charAt(0) == '.' ? third.substring(1) : third;
        
        // 5단계
        String fifth = fourth.length() == 0 ? "a" : fourth;
        
        // 6단계
        String sixth = fifth.length() >= 16 ? fifth.substring(0, 15) : fifth;
        sixth = sixth.charAt(sixth.length() - 1) == '.' ? sixth.substring(0, sixth.length() - 1) : sixth;
        
        // 7단계
        String result = sixth;
        while (result.length() <= 2) {
            result += result.charAt(result.length() - 1);
        }
        
        return result;
    }
}