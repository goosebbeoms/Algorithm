import java.util.*;

class Solution {
    // "HH:MM" → 분
    private int toMinutes(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }

    // 누적 주차시간(min)에 대한 요금 계산
    private int calcFee(int min, int[] fees) {
        int baseTime = fees[0];
        int baseFee  = fees[1];
        int unitTime = fees[2];
        int unitFee  = fees[3];

        if (min <= baseTime) return baseFee;

        int extra = min - baseTime;
        int units = (extra + unitTime - 1) / unitTime; // 올림
        return baseFee + units * unitFee;
    }

    public int[] solution(int[] fees, String[] records) {
        // 입차 시각: 차량번호 -> 분
        Map<String, Integer> inTime = new HashMap<>();
        // 누적 주차시간: 차량번호 -> 분
        Map<String, Integer> totalMin = new HashMap<>();

        for (String record : records) {
            String[] log = record.split(" ");
            String time = log[0];
            String car  = log[1];
            String act  = log[2]; // "IN" or "OUT"

            if ("IN".equals(act)) {
                inTime.put(car, toMinutes(time));
            } else { // "OUT"
                int parked = toMinutes(time) - inTime.get(car);
                totalMin.put(car, totalMin.getOrDefault(car, 0) + parked);
                inTime.remove(car);
            }
        }

        // 출차 기록 없는 차량들 23:59 처리
        int endOfDay = toMinutes("23:59");
        for (String car : inTime.keySet()) {
            int parked = endOfDay - inTime.get(car);
            totalMin.put(car, totalMin.getOrDefault(car, 0) + parked);
        }

        // 차량번호 오름차순으로 요금 계산
        TreeMap<String, Integer> sorted = new TreeMap<>(totalMin);
        int[] answer = new int[sorted.size()];
        int i = 0;
        for (Map.Entry<String, Integer> e : sorted.entrySet()) {
            answer[i++] = calcFee(e.getValue(), fees);
        }
        return answer;
    }
}
