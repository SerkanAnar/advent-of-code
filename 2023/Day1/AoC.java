import java.io.*;
import java.util.*;

public class AoC {
    static Map<String, Integer> mapping = new HashMap<String, Integer>(); 
    public static void main(String[] args) {
        
        setHashMap(); 
        String stringNumbers[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };
        BufferedReader reader; 
        int a = 0; 
        int b = 0; 
        int sum = 0; 
        String textNum = "";

        try {
            reader = new BufferedReader(new FileReader("/Users/serkan/Desktop/AoC 2023/Day1/input.txt")); 
            String line; 
            while ((line = reader.readLine()) != null) {
                String solveAnnoyingProblem[] = new String[100];
                char[] arr = line.toCharArray();
                textNum = ""; 
                outer : for (int i = 0; i < arr.length; i++) {
                    textNum += arr[i];
                    for (int j = 0; j < stringNumbers.length; j++) {
                        if (textNum.contains(stringNumbers[j])) {
                            a = mapping.get(stringNumbers[j]);
                            break outer; 
                        }
                        
                    }
                    // if yes, set a and break
                    if (Character.isDigit(arr[i])) {
                        a = arr[i] - '0';
                        break; 
                    }
                }
                int k = 0;
                outer2 : for (int i = arr.length - 1; i >= 0; i--) {
                    textNum = "";
                    solveAnnoyingProblem[k] = String.valueOf(arr[i]);
                    k++; 
                    for (int l = solveAnnoyingProblem.length - 1; l >= 0; l--) {
                        if (solveAnnoyingProblem[l] != null) 
                            textNum += solveAnnoyingProblem[l];
                    }
                    for (int l = 0; l < stringNumbers.length; l++) {
                        if (textNum.contains(stringNumbers[l])) {
                            b = mapping.get(stringNumbers[l]);
                            break outer2;
                        }
                    }
                    
                    // if yes, set a and break
                    if (Character.isDigit(arr[i])) {
                        b = arr[i] - '0';
                        break;
                    }
                }
                sum += (a*10 + b); 
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(sum);
    }

    private static void setHashMap() {
        mapping.put("one", 1); 
        mapping.put("two", 2); 
        mapping.put("three", 3);
        mapping.put("four", 4);
        mapping.put("five", 5);
        mapping.put("six", 6);
        mapping.put("seven", 7);
        mapping.put("eight", 8);
        mapping.put("nine", 9);

    }
}
