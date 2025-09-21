import java.util.*;

class Solution {
    public long calc(long num1, long num2, char op) {
        if (op == '+') {
            return num1 + num2;
        } else if (op == '-') {
            return num1 - num2;
        } else {
            return num1 * num2;
        }
    }
    
    public void calculate(List<Long> nums, List<Character> ops, char operator) {
        int idx;
        while ((idx = ops.indexOf(operator)) != -1) {
            long num = calc(nums.get(idx), nums.get(idx + 1), operator);
            ops.remove(idx);
            nums.remove(idx);
            nums.remove(idx);
            nums.add(idx, num);
        }
        
//         for (int i = 0; i < ops.size(); i++) {
//             if (ops.get(i) == operator) {
//                 long num = calc(nums.get(i), nums.get(i + 1), operator);
                
//                 ops.remove(i);
//                 nums.remove(i);
//                 nums.remove(i);
//                 nums.add(i, num);
//                 i--;
//             }
//         }
    }
    
    public long operation(List<Long> numbers, List<Character> operations, char op1, char op2, char op3) {
        // 해당 케이스 연산자 순서 계산 위해 리스트 깊은 복사
        List<Long> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();
        
        for (int i = 0; i < numbers.size(); i++) {
            nums.add(numbers.get(i));
        }
        for (int i = 0; i < operations.size(); i++) {
            ops.add(operations.get(i));
        }
        
        // 우선순위에 따라 연산 진행
        calculate(nums, ops, op1);
        calculate(nums, ops, op2);
        calculate(nums, ops, op3);
        
        return nums.get(0);
    }
    
    public long solution(String expression) {
        long answer = 0;    // 정답 제출용
        List<Long> numbers = new ArrayList<>();
        List<Character> operations = new ArrayList<>();
        
        StringBuilder sb = new StringBuilder();
        // numbers 리스트와 operations 리스트에 expression 파싱
        for (char c : expression.toCharArray()) {
            if (c == '+' || c == '-' || c == '*') {
                numbers.add(Long.parseLong(sb.toString()));
                operations.add(c);
                sb = new StringBuilder();
            } else {
                sb.append(c);
            }
        }
        numbers.add(Long.parseLong(sb.toString()));
        
        long[] candidates = new long[6];
        candidates[0] = operation(numbers, operations, '+', '-', '*');
        candidates[1] = operation(numbers, operations, '+', '*', '-');
        candidates[2] = operation(numbers, operations, '-', '+', '*');
        candidates[3] = operation(numbers, operations, '-', '*', '+');
        candidates[4] = operation(numbers, operations, '*', '+', '-');
        candidates[5] = operation(numbers, operations, '*', '-', '+');
        
        for (long candidate : candidates) {
            answer = answer < Math.abs(candidate) ? Math.abs(candidate) : answer;
        }
        
        return answer;
    }
}