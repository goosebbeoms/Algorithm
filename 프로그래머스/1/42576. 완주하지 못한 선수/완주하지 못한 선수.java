import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> book = new HashMap<>();
        for (String name : completion) {
            book.put(name, book.getOrDefault(name, 0) + 1);
        }
        
        for (String name : participant) {
            int count = book.getOrDefault(name, 0);
            if (count == 0) {
                return name;
            }
            book.put(name, count - 1);
        }
        
        return "";
    }
}