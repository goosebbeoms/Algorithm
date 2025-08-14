import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String, Set<String>> singos = new HashMap<>();
        
        for (String s : report) {
            String[] names = s.split(" ");
            if (!singos.containsKey(names[1])) {
                singos.put(names[1], new HashSet<>());
            }
            singos.get(names[1]).add(names[0]);
        }
        
        Map<String, Integer> counts = new HashMap<>();
        for (Map.Entry<String, Set<String>> singo : singos.entrySet()) {
            if (singo.getValue().size() >= k) {
                for (String name : singo.getValue()) {
                    counts.put(name, counts.getOrDefault(name, 0) + 1);
                }
            }
        }
        
        int[] result = new int[id_list.length];
        for (int i = 0; i < id_list.length; i++) {
            result[i] = counts.getOrDefault(id_list[i], 0);
        }
        
        return result;
    }
}